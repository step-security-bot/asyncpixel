"""Data objects for boosters."""
import datetime
import uuid
from typing import List
from typing import Union

from asyncpixel.constants import GameType
from asyncpixel.utils import validate_game_type
from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field
from pydantic import field_validator

from .utils import to_camel


class Booster(BaseModel):
    """Main booster class.

    Args:
        id (str): ID
        purchaser_uuid (uuid.UUID): UUID of booster.
        amount (int): Amount of boosters.
        original_length (int): Original length of booster.
        length (int): Length of booster.
        game_type (GameType): Game type.
        date_activated (datetime.datetime): Date boost activated.
        stacked (Union[List[uuid.UUID], bool]): Wether boosters stacked.
    """

    id: str = Field(alias="_id")
    purchaser_uuid: uuid.UUID
    amount: float
    original_length: int
    length: int
    game_type: GameType

    @field_validator("game_type", mode="before")
    @classmethod
    def _validate_game_type(cls, v: int) -> GameType:
        """Validate game type."""
        return validate_game_type(v)

    date_activated: datetime.datetime
    stacked: Union[List[uuid.UUID], bool] = False
    model_config = ConfigDict(alias_generator=to_camel)


class Boosters(BaseModel):
    """Object containing boosters.

    Args:
        booster_state_decrementing (bool): Wether booster state decrementing.
        boosters (List[Booster]): List of boosters online.
    """

    booster_state_decrementing: bool = Field(alias="decrementing")
    boosters: List[Booster]
