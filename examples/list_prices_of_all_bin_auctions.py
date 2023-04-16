"""Simple example of listing all bin auctions with prices."""
import asyncio

from asyncpixel.hypixel import Hypixel


async def main() -> None:
    """Prints price of all bin auctions on first page."""
    client = Hypixel()  # This call does not require an api key
    auctions = await client.auctions()

    for bin in filter(lambda x: x.bin, auctions.auctions):
        print(bin.starting_bid)
    await client.close()


asyncio.run(main())
