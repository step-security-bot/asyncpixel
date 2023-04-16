"""Simple example of listing all auctions that have ended in the last minute."""
import asyncio

from asyncpixel.hypixel import Hypixel


async def main() -> None:
    """Prints price of all recently ended auctions."""
    client = Hypixel()
    auctions_ended = await client.auctions_ended()
    for auction in auctions_ended.auctions:
        print(auction.price)

    await client.close()


if __name__ == "__main__":
    asyncio.run(main())
