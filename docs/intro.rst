Introduction!
======================================

Asyncpixel is an asyncronous python wrapper for the Hypixel api with 100% coverage. It uses
Pydantic models to store the data presenting an easy to use and reliable interface.

Requirements
------------

- Python 3.8+
- Pydantic
- Aiohttp

Installation
------------

To install Asyncpixel,
run this command in your terminal or use your favourite package manager:

.. code-block:: console

   $ pip install asyncpixel

Basic Example
-------------

.. code-block:: python

   import asyncpixel
   import asyncio

   async def main():
      hypixel = asyncpixel.Hypixel("hypixel_api_key")
      player = await hypixel.player("405dcf08b80f4e23b97d943ad93d14fd")
      print(player.stats.bedwars)
      await hypixel.close()


   asyncio.run(main())
