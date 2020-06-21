import datetime


class Booster:
    def __init__(
        self,
        _id: str,
        purchaserUuid: str,
        amount: int,
        originalLength: int,
        length: int,
        gameType: int,
        dateActivated: datetime.datetime,
        stacked: bool,
    ):

        self._id = _id
        self.purchaserUuid = purchaserUuid
        self.amount = amount
        self.originalLength = originalLength
        self.length = length
        self.gameType = gameType
        self.dateActivated = dateActivated
        self.stacked = stacked


class Boosters:
    def __init__(
        self, boosterStatedecrementing: bool, boosters: list[Booster]
    ):
        self.boosterStatedecrementing = boosterStatedecrementing
        self.boosters = boosters
