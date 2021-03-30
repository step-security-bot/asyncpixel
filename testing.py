import asyncpixel
import asyncio

async def main():
   hypixel = asyncpixel.Hypixel("e817e297-5891-465c-be8d-00be59cc915d")
   profile = await hypixel.guild_by_name("Overslept")
   print(profile)
   await hypixel.close()


asyncio.run(main())