from asyncpixel.hypixel import Hypixel
import asyncio

api_key = "Your key"


async def main(key):
    client = Hypixel(key)
    auctions = await client.auctions()

    for bin in filter(lambda x: x.bin, auctions.auctions):
        print(bin.starting_bid)
    await client.close()


asyncio.run(main(api_key))
