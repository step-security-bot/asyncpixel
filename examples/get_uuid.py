"""Get uuid."""
import asyncio

import asyncpixel


async def main():
    """Get uuid."""
    hypixel = asyncpixel.Hypixel("hypixel_api_key")
    print(await hypixel.uuid_from_name("Darkflame72"))
    await hypixel.close()


asyncio.run(main())
