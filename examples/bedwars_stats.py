"""Bedwars Stats."""
import asyncio

import asyncpixel


async def main() -> None:
    """Bedwars stats of a player."""
    hypixel = asyncpixel.Hypixel("hypixel_api_key")
    player = await hypixel.player("b876ec32-e396-476b-a115-8438d83c67d4")
    if player:
        print(player.stats.bedwars)
    await hypixel.close()


asyncio.run(main())
