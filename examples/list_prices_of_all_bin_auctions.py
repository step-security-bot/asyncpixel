"""Simple example of listing all bin auctions with prices."""
import asyncio

from asyncpixel.hypixel import Hypixel

api_key = "Your key"


async def main(key):
    """Prints price of all bin auctions on first page."""
    client = Hypixel(key)
    auctions = await client.auctions()

    for bin in filter(lambda x: x.bin, auctions.auctions):
        print(bin.starting_bid)
    await client.close()


asyncio.run(main(api_key))
