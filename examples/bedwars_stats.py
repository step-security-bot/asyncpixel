"""Bedwars Stats."""
import asyncio

import asyncpixel


async def main():
    """Bedwars stats of a player."""
    hypixel = asyncpixel.Hypixel("hypixel_api_key")
    print((await hypixel.player("b876ec32-e396-476b-a115-8438d83c67d4")).stats.bedwars)
    await hypixel.close()


asyncio.run(main())
