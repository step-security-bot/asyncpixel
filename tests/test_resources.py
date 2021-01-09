"""Test guild."""
import pytest
from aioresponses import aioresponses
from asyncpixel import Hypixel


@pytest.mark.asyncio
async def test_resources_achievements(hypixel_client: Hypixel) -> None:
    """Test to check the resources_achievements method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/achievements",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_achievements()

        assert data["lastUpdated"] == 1608480930882


@pytest.mark.asyncio
async def test_resources_challenges(hypixel_client: Hypixel) -> None:
    """Test to check the resources_challenges method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/challenges",
            status=200,
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_challenges()

        assert data["lastUpdated"] == 1608480930882


@pytest.mark.asyncio
async def test_resources_quests(hypixel_client: Hypixel) -> None:
    """Test to check the resources_quests method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/quests",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_quests()

        assert data["lastUpdated"] == 1608480930882


@pytest.mark.asyncio
async def test_resources_guilds_achievements(hypixel_client: Hypixel) -> None:
    """Test to check the resources_guilds_achievements method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/guilds/achievements",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_guilds_achievements()

        assert data["lastUpdated"] == 1608480930882


@pytest.mark.asyncio
async def test_resources_guilds_permissions(hypixel_client: Hypixel) -> None:
    """Test to check the resources_guilds_permissions method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/guilds/permissions",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_guilds_permissions()

        assert data["lastUpdated"] == 1608480930882


@pytest.mark.asyncio
async def test_resources_skyblock_collections(hypixel_client: Hypixel) -> None:
    """Test to check the resources_skyblock_collections method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/skyblock/collections",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_skyblock_collections()

        assert data["lastUpdated"] == 1608480930882


@pytest.mark.asyncio
async def test_resources_skyblock_skills(hypixel_client: Hypixel) -> None:
    """Test to check the resources_skyblock_skills method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/resources/skyblock/skills",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "lastUpdated": 1608480930882},
        )
        data = await hypixel_client.resources_skyblock_skills()

        assert data["lastUpdated"] == 1608480930882
