"""Test player count."""
from uuid import UUID

import pytest
from aioresponses import aioresponses
from asyncpixel import Hypixel


@pytest.mark.asyncio
async def test_player_count(hypixel_client: Hypixel, key: UUID) -> None:
    """Test to check the player_count method returns correct data."""
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/playerCount?key={str(key)}",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "playerCount": 75612},
        )
        data = await hypixel_client.player_count()

        assert data == 75612
