"""Pet objects."""
import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .utils import to_upper


class PetStat(BaseModel):
    """Pet State

    Parameters
    ----------
    timestamp : datetime.datetime
        Timestamp of the stat
    value : int
        Value of the stat
    """

    timestamp: datetime.datetime
    value: int


class Pet(BaseModel):
    """Pet

    Parameters
    ----------
    thirst : Optional[PetStat]
        Thirst stat
    exercise : Optional[PetStat]
        Exercise stat
    hunger : Optional[PetStat]
        Hunger stat
    experience : Optional[int]
        Experience of the pet
    name : Optional[str]
        Name of the pet
    """

    thirst: Optional[PetStat]
    exercise: Optional[PetStat]
    hunger: Optional[PetStat]
    experience: Optional[int] = Field(alias="experience")
    name: Optional[str] = Field(alias="name")

    class Config:
        """Config."""

        alias_generator = to_upper
