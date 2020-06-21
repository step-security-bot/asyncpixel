from random import choice
from typing import Union

import aiohttp

from .exceptions.exceptions import RateLimitError

# models
from .models.key import Key
from .models.status import Status
from .models.watchdog import WatchDog


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
            params (dict, optional): parameters to pass into request. Defaults to {}.

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
