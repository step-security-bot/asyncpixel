"""Test boosters."""
import datetime

import pytest
from aioresponses import aioresponses
from asyncpixel import Hypixel
from asyncpixel.models import gametype
from tests.utils import generate_key


@pytest.mark.asyncio
async def test_boosters() -> None:
    """Test to check the boosters method returns correct data."""
    key = generate_key()
    purchaseruuid1 = generate_key()
    purchaseruuid2 = generate_key()
    stacked1 = generate_key()
    stacked2 = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/boosters?key={str(key)}",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={
                "success": True,
                "boosters": [
                    {
                        "_id": "5c197fadc8f245280926413d",
                        "purchaserUuid": str(purchaseruuid1),
                        "amount": 2,
                        "originalLength": 3600,
                        "length": 3595,
                        "gameType": 24,
                        "dateActivated": 1545244519133,
                        "stacked": True,
                    },
                    {
                        "_id": "5de1bf590cf2544cd01a7e04",
                        "purchaserUuid": str(purchaseruuid2),
                        "amount": 2.2,
                        "originalLength": 3600,
                        "length": 2074,
                        "gameType": 13,
                        "dateActivated": 1590842991659,
                        "stacked": [
                            str(stacked1),
                            str(stacked2),
                        ],
                    },
                ],
                "boosterState": {"decrementing": True},
            },
        )
        client = Hypixel(api_key=str(key))
        data = await client.boosters()

        assert len(data.boosters) == 2
        assert data.booster_state_decrementing is True

        assert data.boosters[0].id == "5c197fadc8f245280926413d"
        assert data.boosters[0].purchaser_uuid == purchaseruuid1
        assert data.boosters[0].amount == 2.0
        assert data.boosters[0].original_length == 3600
        assert data.boosters[0].length == 3595
        assert data.boosters[0].game_type == gametype(
            "SUPER_SMASH", "SuperSmash", "Smash Heroes", 24
        )
        assert data.boosters[0].date_activated == datetime.datetime.fromtimestamp(
            1545244519.133, tz=datetime.timezone.utc
        )
        assert data.boosters[0].stacked is True

        assert data.boosters[1].id == "5de1bf590cf2544cd01a7e04"
        assert data.boosters[1].purchaser_uuid == purchaseruuid2
        assert data.boosters[1].amount == 2.2
        assert data.boosters[1].original_length == 3600
        assert data.boosters[1].length == 2074
        assert data.boosters[1].game_type == gametype(
            "WALLS3", "Walls3", "Mega Walls", 13
        )
        assert data.boosters[1].date_activated == datetime.datetime.fromtimestamp(
            1590842991.659, tz=datetime.timezone.utc
        )
        assert data.boosters[1].stacked == [
            stacked1,
            stacked2,
        ]
        await client.close()
