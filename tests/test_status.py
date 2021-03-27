"""Test status."""
from uuid import UUID

import pytest
from aioresponses import aioresponses
from asyncpixel import Hypixel
from asyncpixel.models import gametype


@pytest.mark.asyncio
async def test_online_status(hypixel_client: Hypixel, key: UUID) -> None:
    """Test to check the online_status method returns correct data."""
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/status?key={str(key)}&uuid=74"
            + "86aa03aca5470e888dde8a43eb8c10",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={
                "success": True,
                "session": {
                    "online": True,
                    "gameType": "SKYWARS",
                    "mode": "ranked_normal",
                },
            },
        )
        client = hypixel_client
        data = await client.player_status("7486aa03aca5470e888dde8a43eb8c10")

        assert data.online is True
        assert data.game_type == gametype("SKYWARS", "SkyWars", "SkyWars", 51)
        assert data.mode == "ranked_normal"


@pytest.mark.asyncio
async def test_offline_status(hypixel_client: Hypixel, key: UUID) -> None:
    """Test to check the offline_status method returns correct data."""
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/status?key={str(key)}&uuid=74"
            + "86aa03aca5470e888dde8a43eb8c10",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={
                "success": True,
                "session": {
                    "online": False,
                },
            },
        )
        client = hypixel_client
        data = await client.player_status("7486aa03aca5470e888dde8a43eb8c10")

        assert data.online is False
