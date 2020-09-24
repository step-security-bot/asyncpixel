"""Bazaar classes."""

import datetime
from typing import List


class Bazaar_buy_summary:
    """Bazaar buy object."""

    def __init__(self, amount: int, pricePerUnit: int, orders: int) -> None:
        """Init object.

        Args:
            amount (int): [description]
            pricePerUnit (int): [description]
            orders (int): [description]
        """
        self.amount = amount
        self.pricePerUnit = pricePerUnit
        self.orders = orders


class Bazaar_sell_summary:
    """Bazaar sell object."""

    def __init__(self, amount: int, pricePerUnit: int, orders: int) -> None:
        """Init object.

        Args:
            amount (int): [description]
            pricePerUnit (int): [description]
            orders (int): [description]
        """
        self.amount = amount
        self.pricePerUnit = pricePerUnit
        self.orders = orders


class Bazaar_quick_status:
    """Bazaar quick status."""

    def __init__(
        self,
        productId: str,
        sellPrice: float,
        sellVolume: int,
        sellMovingWeek: int,
        sellOrders: int,
        buyPrice: float,
        buyVolume: int,
        buyMovingWeek: int,
        buyOrders: int,
    ) -> None:
        """Init object.

        Args:
            productId (str): [description]
            sellPrice (float): [description]
            sellVolume (int): [description]
            sellMovingWeek (int): [description]
            sellOrders (int): [description]
            buyPrice (float): [description]
            buyVolume (int): [description]
            buyMovingWeek (int): [description]
            buyOrders (int): [description]
        """
        self.productId = productId
        self.sellPrice = sellPrice
        self.sellVolume = sellVolume
        self.sellMovingWeek = sellMovingWeek
        self.sellOrders = sellOrders
        self.buyPrice = sellPrice
        self.buyVolume = sellVolume
        self.buyMovingWeek = sellMovingWeek
        self.buyOrders = sellOrders


class Bazaar:
    """Bazaar object."""

    def __init__(self, lastUpdated: datetime.datetime, bazaar_items: List) -> None:
        """Init object.

        Args:
            lastUpdated (datetime.datetime): [description]
            bazaar_items (List): [description]
        """
        self.lastUpdated = lastUpdated
        self.bazaar_items = bazaar_items


class Bazaar_item:
    """Bazaar item."""

    def __init__(
        self,
        name: str,
        product_id: str,
        sell_summary: Bazaar_sell_summary,
        buy_summary: Bazaar_buy_summary,
        quick_status: List[Bazaar_quick_status],
    ) -> None:
        """Init object.

        Args:
            name (str): [description]
            product_id (str): [description]
            sell_summary (Bazaar_sell_summary): [description]
            buy_summary (Bazaar_buy_summary): [description]
            quick_status (List[Bazaar_quick_status]): [description]
        """
        self.name = name
        self.product_id = product_id
        self.sell_summary = sell_summary
        self.buy_summary = buy_summary
        self.quick_status = quick_status
