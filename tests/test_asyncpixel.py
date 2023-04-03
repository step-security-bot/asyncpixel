"""Main tests."""
from uuid import UUID

import asyncpixel
import pytest
from aioresponses import aioresponses

from .utils import generate_key


def test_version() -> None:
    """Mock version."""
    assert asyncpixel.__version__ == "1.6.0"


def test_author() -> None:
    """Test author."""
    assert asyncpixel.__author__ == "Leon Bowie"


def test_title() -> None:
    """Test title."""
    assert asyncpixel.__title__ == "asyncpixel"


def test_copyright() -> None:
    """Test copyright."""
    assert asyncpixel.__copyright__ == "Copyright 2020-2023 Leon Bowie"


def test_license() -> None:
    """Test license."""
    assert (
        asyncpixel.__license__
        == """Copyright (C) 2020 Leon Bowie

This program is free software: you can redistribute it
and/or modify it under the terms of the GNU General Public
License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License a
long with this program. If not, see <https://www.gnu.org/licenses/>."""
    )


@pytest.mark.asyncio
async def test_get() -> None:
    """Test get method."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "Test_value": "Random string"},
        )
        client = asyncpixel.Hypixel(api_key=str(key))
        data = await client._get("test")
        assert data == {"success": True, "Test_value": "Random string"}
        await client.close()


@pytest.mark.asyncio
async def test_safe_ratelimit() -> None:
    """Test get method."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "0",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "Test_value": "Random string"},
        )
        client = asyncpixel.Hypixel(api_key=str(key))
        await client._get("test")
        with pytest.raises(asyncpixel.exceptions.RateLimitError):
            await client._get("test")
        await client.close()


@pytest.mark.asyncio
async def test_safe_no_key() -> None:
    """Test no key method."""
    client = asyncpixel.Hypixel()
    with pytest.raises(asyncpixel.exceptions.InvalidApiKeyError):
        await client._get("test")
    await client.close()


@pytest.mark.asyncio
async def test_no_hader() -> None:
    """Test get method."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=200,
            payload={"success": True, "Test_value": "Random string"},
        )
        client = asyncpixel.Hypixel(api_key=str(key))
        await client._get("test")
        await client.close()


@pytest.mark.asyncio
async def test_saved_rate_max() -> None:
    """Test get method."""
    key = generate_key()
    with aioresponses() as m:
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "5",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "Test_value": "Random string"},
        )
        client = asyncpixel.Hypixel(api_key=str(key))
        await client._get("test")
        m.get(
            f"https://api.hypixel.net/test?key={str(key)}",
            status=200,
            headers={
                "RateLimit-Limit": "200",
                "RateLimit-Remaining": "4",
                "RateLimit-Reset": "8",
            },
            payload={"success": True, "Test_value": "Random string"},
        )
        await client._get("test")
        assert client.total_requests == 120
        await client.close()


@pytest.mark.asyncio
async def test_get_uuid() -> None:
    """Test get uuid."""
    with aioresponses() as m:
        m.get(
            "https://api.mojang.com/users/profiles/minecraft/Technoblade",
            status=200,
            payload={"name": "Technoblade", "id": "b876ec32e396476ba1158438d83c67d4"},
        )
        client = asyncpixel.Hypixel()
        uuid = await client.uuid_from_name("Technoblade")
        assert uuid == UUID("b876ec32e396476ba1158438d83c67d4")
        await client.close()


@pytest.mark.asyncio
async def test_get_uuid_fail() -> None:
    """Test get uuid."""
    with aioresponses() as m:
        m.get(
            "https://api.mojang.com/users/profiles/minecraft/Technoblade",
            status=404,
        )
        client = asyncpixel.Hypixel()
        uuid = await client.uuid_from_name("Technoblade")
        assert uuid is None


@pytest.mark.asyncio
async def test_context_manager() -> None:
    """Test context manager."""
    with aioresponses() as m:
        m.get(
            "https://api.mojang.com/users/profiles/minecraft/Technoblade",
            status=200,
            payload={"name": "Technoblade", "id": "b876ec32e396476ba1158438d83c67d4"},
        )
        async with asyncpixel.Hypixel() as client:
            uuid = await client.uuid_from_name("Technoblade")
            assert uuid == UUID("b876ec32e396476ba1158438d83c67d4")
