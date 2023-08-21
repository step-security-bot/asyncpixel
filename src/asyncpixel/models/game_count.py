"""Game Count related objects."""
from typing import Dict, Optional

from pydantic import BaseModel, ConfigDict

from .utils import to_camel


class GameCountsGame(BaseModel):
    """Game count game.

    Args:
        players (int): Number of players in a game.
        uuid_sender (Optional[Dict[str, int]]): Dict of game modes and people in them.
    """

    players: int
    modes: Optional[Dict[str, int]] = None


class GameCounts(BaseModel):
    """Game Count class.

    Args:
        games (Dict[str, GameCountsGame]): dict of all game and their game counts.
        player_count (int): total number of players online.
    """

    games: Dict[str, GameCountsGame]
    player_count: int
    model_config = ConfigDict(alias_generator=to_camel)
