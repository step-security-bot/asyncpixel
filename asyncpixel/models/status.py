"""Status data class."""
from typing import Optional

from asyncpixel.constants import GameType
from asyncpixel.utils import validate_game_type
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import field_validator

from .utils import to_camel


class Status(BaseModel):
    """Status data object.

    Args:
        online (bool): Wether player is online.
        game_type (Optional[GameType]): Current game player is playing.
            Defaults to None.
        mode (Optional[str]): Mode of current game. Defaults to None.
    """

    online: bool = False
    game_type: Optional[GameType] = None
    mode: Optional[str] = None

    @field_validator("game_type", mode="before")
    @classmethod
    def _validate_game_type(cls, v: str) -> GameType:
        """Validate game type."""
        return validate_game_type(v)

    model_config = ConfigDict(alias_generator=to_camel)
