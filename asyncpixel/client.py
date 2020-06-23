import datetime as dt
from random import choice
from typing import Union

import aiohttp

from .exceptions.exceptions import RateLimitError
from .models.booster import Booster, Boosters
from .models.friends import Friend
from .models.key import Key
from .models.status import Status
from .models.watchdog import WatchDog
from .models.games import Game
from .models.player import Player


class Client:
    """client class for hypixel wrapper"""

    def __init__(self, api_keys: Union[list, str]):
        """Initialise base class by storing keys and creating session

        Args:
            api_keys (Union[list, str]): list or signle api key to use
        """

        # Handles the instance of a singular key
        if not isinstance(api_keys, list):
            api_keys = [api_keys]

        self.api_keys = api_keys

        self.base_url = "https://api.hypixel.net/"

        self.session = aiohttp.ClientSession()

    async def close(self):
        """used for safe client cleanup and stuff"""
        await self.session.close()

    async def get(self, path: str, params: dict = {}) -> dict:
        """Base function to get raw data from hypixel

        Args:
            path (str): path that you wish to request from
            params (dict, optional): parameters to pass into request. 
            Defaults to empty dictionary.

        Raises:
            RateLimitError: error if ratelimit has been reached

        Returns:
            dict: returns a dictionary of the json response
        """
        params["key"] = choice(self.api_keys)

        response = await self.session.get(
            f"{self.base_url}{path}", params=params,
        )

        if response.status == 429:
            raise RateLimitError("Hypixel")

        return await response.json()

    async def KeyData(self, key: str = None) -> Key:
        """Get information about an api key.

        Args:
            key (str, optional): api key. Defaults tokey provided in class.

        Returns:
            Key: Key object
        """

        if key is None:
            key = choice(self.api_keys)

        data = await self.get("key")

        return Key(
            success=data["success"],
            key=data["record"]["key"],
            owner=data["record"]["owner"],
            limit=data["record"]["limit"],
            queriesInPastMin=data["record"]["queriesInPastMin"],
            totalQueries=data["record"]["totalQueries"],
        )

    async def WatchdogStats(self) -> WatchDog:
        """Get current watchdog stats.

        Returns:
            WatchDog: WatchDog stats object
        """
        data = await self.get("watchdogstats")

        return WatchDog(
            watchdog_lastMinute=data["watchdog_lastMinute"],
            staff_rollingDaily=data["staff_rollingDaily"],
            watchdog_total=data["watchdog_total"],
            watchdog_rollingDaily=data["watchdog_rollingDaily"],
            staff_total=data["staff_total"],
        )

    async def PlayerStatus(self, uuid: str) -> Status:
        """Get current online status about a player.

        Args:
            uuid (str): uuid of player

        Returns:
            Status: Status object of player
        """

        data = await self.get("status", params={"uuid": uuid})
        if data["session"]["online"]:
            return Status(
                online=True,
                gameType=data["session"]["gameType"],
                mode=data["session"]["mode"],
                map=data["session"],
            )
        return Status(online=False)

    async def PlayerCount(self) -> int:
        """Get the current amount of players online.

        Returns:
            int: number of online players
        """
        data = await self.get("playerCount")

        return data["playerCount"]

    async def GetBoosters(self) -> Boosters:
        """Get the current online boosters.

        Returns:
            Boosters: object containing boosters
        """
        data = await self.get("boosters")
        boosterlist = []

        for boost in data["boosters"]:
            boosterlist.append(
                Booster(
                    _id=boost["_id"],
                    purchaserUuid=boost["purchaserUuid"],
                    amount=boost["amount"],
                    originalLength=boost["originalLength"],
                    length=boost["length"],
                    gameType=boost["gameType"],
                    dateActivated=dt.datetime(boost["dateActivated"]),
                    stacked=boost["stacked"],
                )
            )
        return Boosters(
            boosterStatedecrementing=data["boosterState"]["decrementing"],
            boosters=boosterlist,
        )

    async def FindGuild(self, guildname: str, isuuid: bool = False) -> str:
        """Get guild uuid from name.

        Args:
            guildname (str): name fo guild
            isuuid (bool): if a uuid is provided

        Returns:
            str: uuid of guild
        """

        if isuuid:
            data = await self.get("findGuild", params={"byUuid": guildname})
        else:
            data = await self.get("findGuild", params={"byName": guildname})
        if data["success"]:
            return data["guild"]
        return False

    async def PlayerFriends(self, uuid: str) -> list[Friend]:
        """Get a list of a players friends

        Args:
            uuid (str): the uuid of the player you wish to get friends from

        Returns:
            list[Friend]: returns a list of friend elements
        """

        params = {"uuid": uuid}
        data = await self.get("friends", params=params)

        if not data["success"]:
            return None

        friend_list = []
        for friend in data["records"]:
            friend_list.append(
                Friend(
                    _id=friend["id"],
                    uuidSender=data["uuidSender"],
                    uuidReceiver=data["uuidReceiver"],
                    started=dt.datetime(data["started"]),
                )
            )

        return friend_list

    async def RecentGames(self, uuid: str) -> [Game]:
        """Gets a list of the most recent games over the last 3 days

        Args:
            uuid (str): uuid of player

        Returns:
            [Game]: a list of game objects
        """

        params = {"uuid": uuid}
        data = await self.get("recentGames", params=params)

        if not data["success"]:
            return None

        games_list = []
        for game in data["games"]:
            if "ended" in game:
                games_list.append(
                    Game(
                        data=dt.datetime(game["date"]),
                        gameType=game["gameType"],
                        mode=game["Mode"],
                        _map=game["map"],
                        ended=dt.datetime(game["ended"]),
                    )
                )
            else:
                games_list.append(
                    Game(
                        data=dt.datetime(game["date"]),
                        gameType=game["gameType"],
                        mode=game["Mode"],
                        _map=game["map"],
                    )
                )

        return games_list

    async def Player(self, uuid: str):
        """Get information about a player from their uuid

        Args:
            uuid (str): uuid of player

        Returns:
            Player: player object
        """
        params = {"uuid": uuid}
        data = await self.get("player", params=params)

        if not data["success"]:
            return None

        return Player(
            _id=data["player"]["_id"],
            uuid=data["player"]["uuid"],
            firstLogin=dt.datetime(data["player"]["firstLogin"]),
            playername=data["player"]["playername"],
            lastLogin=dt.datetime(data["player"]["lastLogin"]),
            displayname=data["player"]["displayname"],
            knownAliases=data["player"]["knownAliases"],
            knownAliasesLower=data["player"]["knownAliasesLower"],
            achievementsOneTime=data["player"]["achievementsOneTime"],
            mcVersionRp=data["player"]["mcVersionRp"],
            networkExp=data["player"]["networkExp"],
            karma=data["player"]["karma"],
            spec_always_flying=data["player"]["spec_always_flying"],
            lastAdsenseGenerateTime=data["player"]["lastAdsenseGenerateTime"],
            lastClaimedReward=data["player"]["lastClaimedReward"],
            totalRewards=data["player"]["totalRewards"],
            totalDailyRewards=data["player"]["totalDailyRewards"],
            rewardStreak=data["player"]["rewardStreak"],
            rewardScore=data["player"]["rewardScore"],
            rewardHighScore=data["player"]["rewardHighScore"],
            lastLogout=dt.datetime(data["player"]["lastLogout"]),
            friendRequestsUuid=data["player"]["friendRequestsUuid"],
            network_update_book=data["player"]["network_update_book"],
            achievementTracking=data["player"]["achievementTracking"],
            achievementPoints=data["player"]["achievementPoints"],
            currentGadget=data["player"]["currentGadget"],
            channel=data["player"]["channel"],
            mostRecentGameType=data["player"]["mostRecentGameType"],
            level=self.calcPlayerLevel(data["player"]["networkExp"]),
        )

    @staticmethod
    async def calcPlayerLevel(xp: int) -> int:
        """Calculate player level from xp.

        Args:
            xp (int): amount of xp a player has

        Returns:
            int: currentl level of player
        """
        return int(1 + (-8750.0 + (8750 ** 2 + 5000 * xp) ** 0.5) / 2500)

    async def GameCount(self) -> dict:
        """Get the current game count

        Returns:
            dict: raw json response 
        """

        data = await self.get("gameCounts")
        if not data["success"]:
            return False
        return data["games"]

