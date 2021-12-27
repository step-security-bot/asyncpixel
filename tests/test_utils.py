"""Test utilss."""
import pytest
from asyncpixel.models.utils import safe_divide
from asyncpixel.models.utils import to_camel
from asyncpixel.utils import get_rank


@pytest.mark.asyncio
async def test_get_rank() -> None:
    """Test get rank."""
    assert (
        get_rank(
            prefix_raw="§a§l[§bVIP§a§l]",
        )
        == "VIP"
    )
    assert get_rank(rank="OWNER") == "OWNER"
    assert get_rank(monthly_package_rank="MVP++") == "MVP++"
    assert get_rank(new_package_rank="MVP++") == "MVP++"
    assert get_rank(package_rank="MVP++") == "MVP++"


@pytest.mark.asyncio
async def test_safe_divide() -> None:
    """Test safe divide."""
    assert safe_divide(dividend=1, divisor=1) == 1
    assert safe_divide(dividend=1, divisor=0) == float("inf")


@pytest.mark.asyncio
async def test_to_camel() -> None:
    """Test to camel."""
    assert to_camel("test_string") == "testString"
    assert to_camel("test_string_2") == "testString2"
