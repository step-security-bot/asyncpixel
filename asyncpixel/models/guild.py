"""Guild objects."""

import datetime
from typing import List, Dict


class Guild:
    """Guild object."""

    def __init__(
        self,
        _id: str,
        created: datetime.datetime,
        name: str,
        name_lower: str,
        description: str,
        tag: str,
        tagColor: str,
        exp: int,
        members: List,
        achievements: Dict,
        ranks: List,
        joinable: bool,
        legacyRanking: int,
        publiclyListed: bool,
        hideGmTag: bool,
        preferredGames: List[str],
        chatMute: datetime.datetime,
        guildExpByGameType: Dict,
        banner: Dict,
    ) -> None:
        """Init object.

        Args:
            _id (str): [description]
            created (datetime.datetime): [description]
            name (str): [description]
            name_lower (str): [description]
            description (str): [description]
            tag (str): [description]
            tagColor (str): [description]
            exp (int): [description]
            members (List): [description]
            achievements ([type]): [description]
            ranks ([type]): [description]
            joinable (bool): [description]
            legacyRanking (int): [description]
            publiclyListed (bool): [description]
            hideGmTag (bool): [description]
            preferredGames (List[str]): [description]
            chatMute (datetime.datetime): [description]
            guildExpByGameType ([type]): [description]
            banner ([type]): [description]
        """
        self._id = _id
        self.created = created
        self.name = name
        self.name_lower = name_lower
        self.description = description
        self.tag = tag
        self.tagColour = tagColor
        self.exp = exp
        self.members = members
        self.achievements = achievements
        self.ranks = ranks
        self.joinable = joinable
        self.legacyRanking = legacyRanking
        self.publiclyListed = publiclyListed
        self.hideGmTag = hideGmTag
        self.prefferedGames = preferredGames
        self.chatMute = chatMute
        self.guildExpByGameTYpe = guildExpByGameType
        self.banner = banner
