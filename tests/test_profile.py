"""Test profile."""
import datetime
import uuid

import pytest
from aioresponses import aioresponses
from asyncpixel import Hypixel


@pytest.mark.asyncio
async def test_profiles(hypixel_client: Hypixel, key: uuid.UUID) -> None:
    """Test to check the profiles method returns correct data."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/skyblock/profiles?"
            f"key={str(key)}&uuid=405dcf08-b80f-4e23-b97d-943ad93d14fd",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={
                "success": True,
                "profiles": [
                    {
                        "profile_id": "405dcf08b80f4e23b97d943ad93d14fd",
                        "members": {
                            "405dcf08b80f4e23b97d943ad93d14fd": {
                                "last_save": 1599217969829,
                                "inv_armor": {
                                    "type": 0,
                                    "data": "H4sIAAAAAAAAAONiYOBkYMzkYmBg"
                                    + "YGEAAQCp5xppEQAAAA\u003d\u003d",
                                },
                                "first_join": 1589445775678,
                                "first_join_hub": 277843,
                                "stats": {
                                    "pet_milestone_ores_mined": 287.0,
                                    "highest_critical_damage": 38.25,
                                    "kills": 10.0,
                                    "kills_zombie": 5.0,
                                    "deaths": 2.0,
                                    "deaths_spider": 2.0,
                                    "kills_spider": 1.0,
                                    "kills_lapis_zombie": 1.0,
                                    "kills_skeleton": 3.0,
                                },
                                "objectives": {
                                    "collect_log": {
                                        "status": "COMPLETE",
                                        "progress": 1,
                                        "completed_at": 1589445782389,
                                    },
                                    "talk_to_guide": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1589445913700,
                                    },
                                    "public_island": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1589445919300,
                                    },
                                    "craft_workbench": {
                                        "status": "COMPLETE",
                                        "progress": 1,
                                        "completed_at": 1589445794301,
                                    },
                                    "craft_wood_pickaxe": {
                                        "status": "COMPLETE",
                                        "progress": 1,
                                        "completed_at": 1589445832062,
                                    },
                                    "explore_hub": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "explore_village": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_librarian": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_farmer": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_blacksmith": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_lumberjack": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_event_master": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_auction_master": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_banker": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_fairy": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_fisherman_1": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_carpenter": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "paint_canvas": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_pet_collector": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_pet_sitter": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_lazy_miner": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597640063785,
                                    },
                                    "increase_mining_skill_5": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995720523,
                                    },
                                    "talk_to_telekinesis_applier": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597640046434,
                                    },
                                    "find_pickaxe": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995287967,
                                    },
                                    "collect_ingots": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995295716,
                                        "IRON_INGOT": True,
                                        "GOLD_INGOT": True,
                                    },
                                    "warp_deep_caverns": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995761226,
                                    },
                                    "talk_to_lapis_miner": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                    "talk_to_lift_operator": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995840345,
                                    },
                                    "reach_lapis_quarry": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995897703,
                                    },
                                    "collect_lapis": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995906026,
                                        "INK_SACK:4": True,
                                    },
                                    "reach_pigmens_den": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995971118,
                                    },
                                    "collect_redstone": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597995978379,
                                        "REDSTONE": True,
                                    },
                                    "reach_slimehill": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597996062927,
                                    },
                                    "collect_emerald": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597996062927,
                                        "EMERALD": True,
                                    },
                                    "reach_diamond_reserve": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597996109717,
                                    },
                                    "collect_diamond": {
                                        "status": "COMPLETE",
                                        "progress": 0,
                                        "completed_at": 1597996167813,
                                        "DIAMOND": True,
                                    },
                                    "reach_obsidian_sanctuary": {
                                        "status": "ACTIVE",
                                        "progress": 0,
                                        "completed_at": 0,
                                    },
                                },
                                "tutorial": [
                                    "first_join",
                                    "zone_village",
                                    "tutorial_npc_crafter",
                                    "zone_auction_house",
                                    "tutorial_npc_psychic",
                                    "tutorial_npc_instructor",
                                    "tutorial_npc_bugs",
                                    "tutorial_npc_trader",
                                    "tutorial_trade",
                                    "tutorial_npc_explorer",
                                    "zone_bazaar_alley",
                                    "tutorial_npc_quester",
                                    "zone_mine",
                                    "shop_mine_merchant",
                                    "zone_gold_mine",
                                    "shop_iron_forger",
                                    "togglemusic",
                                    "zone_deep_caverns",
                                    "zone_deep_caverns_room_1",
                                    "zone_deep_caverns_room_2",
                                    "zone_deep_caverns_room_3",
                                    "zone_deep_caverns_room_4",
                                    "zone_deep_caverns_room_5",
                                    "shop_adventurer",
                                    "shop_farm_merchant",
                                ],
                                "quests": {
                                    "collect_log": {
                                        "status": "COMPLETE",
                                        "activated_at": 1589445775138,
                                        "activated_at_sb": 29170074,
                                        "completed_at": 1589445832062,
                                        "completed_at_sb": 29170130,
                                    },
                                    "explore_hub": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "explore_village": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_librarian": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_farmer": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_blacksmith": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_lumberjack": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_auction_master": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_banker": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_carpenter": {
                                        "status": "ACTIVE",
                                        "activated_at": 1589445919298,
                                        "activated_at_sb": 29170217,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_lazy_miner": {
                                        "status": "COMPLETE",
                                        "activated_at": 1597640024437,
                                        "activated_at_sb": 37364322,
                                        "completed_at": 1597995295716,
                                        "completed_at_sb": 37719593,
                                    },
                                    "increase_mining_skill_5": {
                                        "status": "ACTIVE",
                                        "activated_at": 1597640024437,
                                        "activated_at_sb": 37364322,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                    "talk_to_lapis_miner": {
                                        "status": "ACTIVE",
                                        "activated_at": 1597995761222,
                                        "activated_at_sb": 37720060,
                                        "completed_at": 0,
                                        "completed_at_sb": 0,
                                    },
                                },
                                "coin_purse": 1100.25,
                                "last_death": 37364569,
                                "crafted_generators": [
                                    "IRON_1",
                                    "COAL_1",
                                    "COBBLESTONE_1",
                                    "COBBLESTONE_2",
                                ],
                                "visited_zones": [
                                    "dynamic_portal_island",
                                    "village",
                                    "auction_house",
                                    "bazaar_alley",
                                    "mine",
                                    "gold_mine",
                                    "deep_caverns",
                                    "deep_caverns_room_1",
                                    "deep_caverns_room_2",
                                    "deep_caverns_room_3",
                                    "deep_caverns_room_4",
                                    "deep_caverns_room_5",
                                ],
                                "fairy_souls_collected": 1,
                                "fairy_souls": 1,
                                "death_count": 2,
                                "slayer_bosses": {
                                    "zombie": {"claimed_levels": {}},
                                    "spider": {"claimed_levels": {}},
                                    "wolf": {"claimed_levels": {}},
                                },
                                "pets": [],
                                "dungeons": {
                                    "dungeon_types": {"catacombs": {}},
                                    "player_classes": {
                                        "healer": {},
                                        "mage": {},
                                        "berserk": {},
                                        "archer": {},
                                        "tank": {},
                                    },
                                    "dungeon_journal": {},
                                },
                            },
                            "4282b7f0b36f479d976af4924eec6e11": {
                                "coop_invitation": {
                                    "timestamp": 1578734194541,
                                    "invited_by": "b876ec32e396476ba1158438d83c67d4",
                                    "confirmed": False,
                                }
                            },
                        },
                        "cute_name": "Strawberry",
                    }
                ],
            },
        )
        data = await hypixel_client.profiles("405dcf08-b80f-4e23-b97d-943ad93d14fd")
        assert data["405dcf08b80f4e23b97d943ad93d14fd"].cute_name == "Strawberry"
        assert data["405dcf08b80f4e23b97d943ad93d14fd"].profile_id == uuid.UUID(
            "405dcf08b80f4e23b97d943ad93d14fd"
        )
        assert len(data["405dcf08b80f4e23b97d943ad93d14fd"].members) == 1
        assert (
            "405dcf08b80f4e23b97d943ad93d14fd"
            in data["405dcf08b80f4e23b97d943ad93d14fd"].members
        )
        member = data["405dcf08b80f4e23b97d943ad93d14fd"].members[
            "405dcf08b80f4e23b97d943ad93d14fd"
        ]

        assert member.last_save == datetime.datetime.fromtimestamp(
            1599217969.829, tz=datetime.timezone.utc
        )
        assert member.inv_armor.type == 0
        assert (
            member.inv_armor.data
            == "H4sIAAAAAAAAAONiYOBkYMzkYmBgYGEAAQCp5xppEQAAAA\u003d\u003d"
        )
        assert member.first_join == datetime.datetime.fromtimestamp(
            1589445775.678, tz=datetime.timezone.utc
        )
        assert member.first_join_hub == 277843
        assert member.stats == {
            "pet_milestone_ores_mined": 287.0,
            "highest_critical_damage": 38.25,
            "kills": 10.0,
            "kills_zombie": 5.0,
            "deaths": 2.0,
            "deaths_spider": 2.0,
            "kills_spider": 1.0,
            "kills_lapis_zombie": 1.0,
            "kills_skeleton": 3.0,
        }
        assert member.tutorial == [
            "first_join",
            "zone_village",
            "tutorial_npc_crafter",
            "zone_auction_house",
            "tutorial_npc_psychic",
            "tutorial_npc_instructor",
            "tutorial_npc_bugs",
            "tutorial_npc_trader",
            "tutorial_trade",
            "tutorial_npc_explorer",
            "zone_bazaar_alley",
            "tutorial_npc_quester",
            "zone_mine",
            "shop_mine_merchant",
            "zone_gold_mine",
            "shop_iron_forger",
            "togglemusic",
            "zone_deep_caverns",
            "zone_deep_caverns_room_1",
            "zone_deep_caverns_room_2",
            "zone_deep_caverns_room_3",
            "zone_deep_caverns_room_4",
            "zone_deep_caverns_room_5",
            "shop_adventurer",
            "shop_farm_merchant",
        ]
        assert member.coin_purse == 1100.25
        assert member.last_death == 37364569
        assert member.crafted_generators == [
            "IRON_1",
            "COAL_1",
            "COBBLESTONE_1",
            "COBBLESTONE_2",
        ]
        assert member.visited_zones == [
            "dynamic_portal_island",
            "village",
            "auction_house",
            "bazaar_alley",
            "mine",
            "gold_mine",
            "deep_caverns",
            "deep_caverns_room_1",
            "deep_caverns_room_2",
            "deep_caverns_room_3",
            "deep_caverns_room_4",
            "deep_caverns_room_5",
        ]
        assert member.fairy_souls_collected == 1
        assert member.fairy_souls == 1
        assert member.death_count == 2
        assert member.pets == []


@pytest.mark.asyncio
async def test_profile(hypixel_client: Hypixel, key: uuid.UUID) -> None:
    """Test porfile."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/skyblock/profile?"
            + f"key={str(key)}&profile=405dcf08b80f4e23b97d943ad93d14fd",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={
                "success": True,
                "profile": {
                    "profile_id": "405dcf08b80f4e23b97d943ad93d14fd",
                    "members": {
                        "405dcf08b80f4e23b97d943ad93d14fd": {
                            "last_save": 1599217969829,
                            "inv_armor": {
                                "type": 0,
                                "data": "H4sIAAAAAAAAAONiYOBkYMz"
                                + "kYmBgYGEAAQCp5xppEQAAAA==",
                            },
                            "first_join": 1589445775678,
                            "first_join_hub": 277843,
                            "stats": {
                                "pet_milestone_ores_mined": 287.0,
                                "highest_critical_damage": 38.25,
                                "kills": 10.0,
                                "kills_zombie": 5.0,
                                "deaths": 2.0,
                                "deaths_spider": 2.0,
                                "kills_spider": 1.0,
                                "kills_lapis_zombie": 1.0,
                                "kills_skeleton": 3.0,
                            },
                            "objectives": {
                                "collect_log": {
                                    "status": "COMPLETE",
                                    "progress": 1,
                                    "completed_at": 1589445782389,
                                },
                                "talk_to_guide": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1589445913700,
                                },
                                "public_island": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1589445919300,
                                },
                                "craft_workbench": {
                                    "status": "COMPLETE",
                                    "progress": 1,
                                    "completed_at": 1589445794301,
                                },
                                "craft_wood_pickaxe": {
                                    "status": "COMPLETE",
                                    "progress": 1,
                                    "completed_at": 1589445832062,
                                },
                                "explore_hub": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "explore_village": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_librarian": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_farmer": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_blacksmith": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_lumberjack": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_event_master": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_auction_master": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_banker": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_fairy": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_fisherman_1": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_carpenter": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "paint_canvas": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_pet_collector": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_pet_sitter": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_lazy_miner": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597640063785,
                                },
                                "increase_mining_skill_5": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995720523,
                                },
                                "talk_to_telekinesis_applier": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597640046434,
                                },
                                "find_pickaxe": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995287967,
                                },
                                "collect_ingots": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995295716,
                                    "IRON_INGOT": True,
                                    "GOLD_INGOT": True,
                                },
                                "warp_deep_caverns": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995761226,
                                },
                                "talk_to_lapis_miner": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                                "talk_to_lift_operator": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995840345,
                                },
                                "reach_lapis_quarry": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995897703,
                                },
                                "collect_lapis": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995906026,
                                    "INK_SACK:4": True,
                                },
                                "reach_pigmens_den": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995971118,
                                },
                                "collect_redstone": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597995978379,
                                    "REDSTONE": True,
                                },
                                "reach_slimehill": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597996062927,
                                },
                                "collect_emerald": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597996062927,
                                    "EMERALD": True,
                                },
                                "reach_diamond_reserve": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597996109717,
                                },
                                "collect_diamond": {
                                    "status": "COMPLETE",
                                    "progress": 0,
                                    "completed_at": 1597996167813,
                                    "DIAMOND": True,
                                },
                                "reach_obsidian_sanctuary": {
                                    "status": "ACTIVE",
                                    "progress": 0,
                                    "completed_at": 0,
                                },
                            },
                            "tutorial": [
                                "first_join",
                                "zone_village",
                                "tutorial_npc_crafter",
                                "zone_auction_house",
                                "tutorial_npc_psychic",
                                "tutorial_npc_instructor",
                                "tutorial_npc_bugs",
                                "tutorial_npc_trader",
                                "tutorial_trade",
                                "tutorial_npc_explorer",
                                "zone_bazaar_alley",
                                "tutorial_npc_quester",
                                "zone_mine",
                                "shop_mine_merchant",
                                "zone_gold_mine",
                                "shop_iron_forger",
                                "togglemusic",
                                "zone_deep_caverns",
                                "zone_deep_caverns_room_1",
                                "zone_deep_caverns_room_2",
                                "zone_deep_caverns_room_3",
                                "zone_deep_caverns_room_4",
                                "zone_deep_caverns_room_5",
                                "shop_adventurer",
                                "shop_farm_merchant",
                            ],
                            "quests": {
                                "collect_log": {
                                    "status": "COMPLETE",
                                    "activated_at": 1589445775138,
                                    "activated_at_sb": 29170074,
                                    "completed_at": 1589445832062,
                                    "completed_at_sb": 29170130,
                                },
                                "explore_hub": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "explore_village": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_librarian": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_farmer": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_blacksmith": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_lumberjack": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_auction_master": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_banker": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_carpenter": {
                                    "status": "ACTIVE",
                                    "activated_at": 1589445919298,
                                    "activated_at_sb": 29170217,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_lazy_miner": {
                                    "status": "COMPLETE",
                                    "activated_at": 1597640024437,
                                    "activated_at_sb": 37364322,
                                    "completed_at": 1597995295716,
                                    "completed_at_sb": 37719593,
                                },
                                "increase_mining_skill_5": {
                                    "status": "ACTIVE",
                                    "activated_at": 1597640024437,
                                    "activated_at_sb": 37364322,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                                "talk_to_lapis_miner": {
                                    "status": "ACTIVE",
                                    "activated_at": 1597995761222,
                                    "activated_at_sb": 37720060,
                                    "completed_at": 0,
                                    "completed_at_sb": 0,
                                },
                            },
                            "coin_purse": 1100.25,
                            "last_death": 37364569,
                            "crafted_generators": [
                                "IRON_1",
                                "COAL_1",
                                "COBBLESTONE_1",
                                "COBBLESTONE_2",
                            ],
                            "visited_zones": [
                                "dynamic_portal_island",
                                "village",
                                "auction_house",
                                "bazaar_alley",
                                "mine",
                                "gold_mine",
                                "deep_caverns",
                                "deep_caverns_room_1",
                                "deep_caverns_room_2",
                                "deep_caverns_room_3",
                                "deep_caverns_room_4",
                                "deep_caverns_room_5",
                            ],
                            "fairy_souls_collected": 1,
                            "fairy_souls": 1,
                            "death_count": 2,
                            "slayer_bosses": {
                                "zombie": {"claimed_levels": {}},
                                "spider": {"claimed_levels": {}},
                                "wolf": {"claimed_levels": {}},
                            },
                            "pets": [],
                            "dungeons": {
                                "dungeon_types": {"catacombs": {}},
                                "player_classes": {
                                    "healer": {},
                                    "mage": {},
                                    "berserk": {},
                                    "archer": {},
                                    "tank": {},
                                },
                                "dungeon_journal": {},
                            },
                        },
                    },
                },
            },
        )
        data = await hypixel_client.profile("405dcf08b80f4e23b97d943ad93d14fd")

        assert data is not None
        assert data.profile_id == uuid.UUID("405dcf08b80f4e23b97d943ad93d14fd")
        assert len(data.members) == 1
        assert "405dcf08b80f4e23b97d943ad93d14fd" in data.members
        member = data.members["405dcf08b80f4e23b97d943ad93d14fd"]

        assert member.last_save == datetime.datetime.fromtimestamp(
            1599217969.829, tz=datetime.timezone.utc
        )
        assert member.inv_armor.type == 0
        assert (
            member.inv_armor.data
            == "H4sIAAAAAAAAAONiYOBkYMzkYmBgYGEAAQCp5xppEQAAAA\u003d\u003d"
        )
        assert member.first_join == datetime.datetime.fromtimestamp(
            1589445775.678, tz=datetime.timezone.utc
        )
        assert member.first_join_hub == 277843
        assert member.stats == {
            "pet_milestone_ores_mined": 287.0,
            "highest_critical_damage": 38.25,
            "kills": 10.0,
            "kills_zombie": 5.0,
            "deaths": 2.0,
            "deaths_spider": 2.0,
            "kills_spider": 1.0,
            "kills_lapis_zombie": 1.0,
            "kills_skeleton": 3.0,
        }
        assert member.tutorial == [
            "first_join",
            "zone_village",
            "tutorial_npc_crafter",
            "zone_auction_house",
            "tutorial_npc_psychic",
            "tutorial_npc_instructor",
            "tutorial_npc_bugs",
            "tutorial_npc_trader",
            "tutorial_trade",
            "tutorial_npc_explorer",
            "zone_bazaar_alley",
            "tutorial_npc_quester",
            "zone_mine",
            "shop_mine_merchant",
            "zone_gold_mine",
            "shop_iron_forger",
            "togglemusic",
            "zone_deep_caverns",
            "zone_deep_caverns_room_1",
            "zone_deep_caverns_room_2",
            "zone_deep_caverns_room_3",
            "zone_deep_caverns_room_4",
            "zone_deep_caverns_room_5",
            "shop_adventurer",
            "shop_farm_merchant",
        ]
        assert member.coin_purse == 1100.25
        assert member.last_death == 37364569
        assert member.crafted_generators == [
            "IRON_1",
            "COAL_1",
            "COBBLESTONE_1",
            "COBBLESTONE_2",
        ]
        assert member.visited_zones == [
            "dynamic_portal_island",
            "village",
            "auction_house",
            "bazaar_alley",
            "mine",
            "gold_mine",
            "deep_caverns",
            "deep_caverns_room_1",
            "deep_caverns_room_2",
            "deep_caverns_room_3",
            "deep_caverns_room_4",
            "deep_caverns_room_5",
        ]
        assert member.fairy_souls_collected == 1
        assert member.fairy_souls == 1
        assert member.death_count == 2
        assert member.pets == []


@pytest.mark.asyncio
async def test_no_profile(hypixel_client: Hypixel, key: uuid.UUID) -> None:
    """Test no problem."""
    with aioresponses() as m:
        m.get(
            "https://api.hypixel.net/skyblock/profile?"
            f"key={str(key)}&profile=405dcf08-b80f-4e23-b97d-943ad93d14fd",
            status=200,
            headers={
                "RateLimit-Limit": "120",
                "RateLimit-Remaining": "119",
                "RateLimit-Reset": "8",
            },
            payload={
                "success": True,
                "profile": None,
            },
        )
        data = await hypixel_client.profile("405dcf08-b80f-4e23-b97d-943ad93d14fd")

        assert data is None


@pytest.mark.asyncio
async def test_fill_profile(hypixel_client: Hypixel, key: uuid.UUID) -> None:
    """Test fill profile."""
    data = hypixel_client._fill_profile(
        {
            "profile_id": "405dcf08b80f4e23b97d943ad93d14fd",
            "members": {
                "405dcf08b80f4e23b97d943ad93d14fd": {
                    "last_save": 1599217969829,
                    "inv_armor": {
                        "type": 0,
                        "data": "H4sIAAAAAAAAAONiYOBkYMzkYmB"
                        + "gYGEAAQCp5xppEQAAAA\u003d\u003d",
                    },
                    "first_join": 1589445775678,
                    "first_join_hub": 277843,
                    "stats": {
                        "pet_milestone_ores_mined": 287.0,
                        "highest_critical_damage": 38.25,
                        "kills": 10.0,
                        "kills_zombie": 5.0,
                        "deaths": 2.0,
                        "deaths_spider": 2.0,
                        "kills_spider": 1.0,
                        "kills_lapis_zombie": 1.0,
                        "kills_skeleton": 3.0,
                    },
                    "objectives": {
                        "collect_log": {
                            "status": "COMPLETE",
                            "progress": 1,
                            "completed_at": 1589445782389,
                        },
                        "talk_to_guide": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1589445913700,
                        },
                        "public_island": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1589445919300,
                        },
                        "craft_workbench": {
                            "status": "COMPLETE",
                            "progress": 1,
                            "completed_at": 1589445794301,
                        },
                        "craft_wood_pickaxe": {
                            "status": "COMPLETE",
                            "progress": 1,
                            "completed_at": 1589445832062,
                        },
                        "explore_hub": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "explore_village": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_librarian": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_farmer": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_blacksmith": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_lumberjack": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_event_master": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_auction_master": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_banker": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_fairy": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_fisherman_1": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_carpenter": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "paint_canvas": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_pet_collector": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_pet_sitter": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_lazy_miner": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597640063785,
                        },
                        "increase_mining_skill_5": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995720523,
                        },
                        "talk_to_telekinesis_applier": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597640046434,
                        },
                        "find_pickaxe": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995287967,
                        },
                        "collect_ingots": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995295716,
                            "IRON_INGOT": True,
                            "GOLD_INGOT": True,
                        },
                        "warp_deep_caverns": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995761226,
                        },
                        "talk_to_lapis_miner": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                        "talk_to_lift_operator": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995840345,
                        },
                        "reach_lapis_quarry": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995897703,
                        },
                        "collect_lapis": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995906026,
                            "INK_SACK:4": True,
                        },
                        "reach_pigmens_den": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995971118,
                        },
                        "collect_redstone": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597995978379,
                            "REDSTONE": True,
                        },
                        "reach_slimehill": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597996062927,
                        },
                        "collect_emerald": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597996062927,
                            "EMERALD": True,
                        },
                        "reach_diamond_reserve": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597996109717,
                        },
                        "collect_diamond": {
                            "status": "COMPLETE",
                            "progress": 0,
                            "completed_at": 1597996167813,
                            "DIAMOND": True,
                        },
                        "reach_obsidian_sanctuary": {
                            "status": "ACTIVE",
                            "progress": 0,
                            "completed_at": 0,
                        },
                    },
                    "tutorial": [
                        "first_join",
                        "zone_village",
                        "tutorial_npc_crafter",
                        "zone_auction_house",
                        "tutorial_npc_psychic",
                        "tutorial_npc_instructor",
                        "tutorial_npc_bugs",
                        "tutorial_npc_trader",
                        "tutorial_trade",
                        "tutorial_npc_explorer",
                        "zone_bazaar_alley",
                        "tutorial_npc_quester",
                        "zone_mine",
                        "shop_mine_merchant",
                        "zone_gold_mine",
                        "shop_iron_forger",
                        "togglemusic",
                        "zone_deep_caverns",
                        "zone_deep_caverns_room_1",
                        "zone_deep_caverns_room_2",
                        "zone_deep_caverns_room_3",
                        "zone_deep_caverns_room_4",
                        "zone_deep_caverns_room_5",
                        "shop_adventurer",
                        "shop_farm_merchant",
                    ],
                    "quests": {
                        "collect_log": {
                            "status": "COMPLETE",
                            "activated_at": 1589445775138,
                            "activated_at_sb": 29170074,
                            "completed_at": 1589445832062,
                            "completed_at_sb": 29170130,
                        },
                        "explore_hub": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "explore_village": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_librarian": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_farmer": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_blacksmith": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_lumberjack": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_auction_master": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_banker": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_carpenter": {
                            "status": "ACTIVE",
                            "activated_at": 1589445919298,
                            "activated_at_sb": 29170217,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_lazy_miner": {
                            "status": "COMPLETE",
                            "activated_at": 1597640024437,
                            "activated_at_sb": 37364322,
                            "completed_at": 1597995295716,
                            "completed_at_sb": 37719593,
                        },
                        "increase_mining_skill_5": {
                            "status": "ACTIVE",
                            "activated_at": 1597640024437,
                            "activated_at_sb": 37364322,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                        "talk_to_lapis_miner": {
                            "status": "ACTIVE",
                            "activated_at": 1597995761222,
                            "activated_at_sb": 37720060,
                            "completed_at": 0,
                            "completed_at_sb": 0,
                        },
                    },
                    "coin_purse": 1100.25,
                    "last_death": 37364569,
                    "crafted_generators": [
                        "IRON_1",
                        "COAL_1",
                        "COBBLESTONE_1",
                        "COBBLESTONE_2",
                    ],
                    "visited_zones": [
                        "dynamic_portal_island",
                        "village",
                        "auction_house",
                        "bazaar_alley",
                        "mine",
                        "gold_mine",
                        "deep_caverns",
                        "deep_caverns_room_1",
                        "deep_caverns_room_2",
                        "deep_caverns_room_3",
                        "deep_caverns_room_4",
                        "deep_caverns_room_5",
                    ],
                    "fairy_souls_collected": 1,
                    "fairy_souls": 1,
                    "death_count": 2,
                    "slayer_bosses": {
                        "zombie": {"claimed_levels": {}},
                        "spider": {"claimed_levels": {}},
                        "wolf": {"claimed_levels": {}},
                    },
                    "pets": [],
                    "dungeons": {
                        "dungeon_types": {"catacombs": {}},
                        "player_classes": {
                            "healer": {},
                            "mage": {},
                            "berserk": {},
                            "archer": {},
                            "tank": {},
                        },
                        "dungeon_journal": {},
                    },
                }
            },
            "cute_name": "Strawberry",
        }
    )

    assert data.cute_name == "Strawberry"
    assert data.profile_id == uuid.UUID("405dcf08b80f4e23b97d943ad93d14fd")
    assert len(data.members) == 1
    assert "405dcf08b80f4e23b97d943ad93d14fd" in data.members
    member = data.members["405dcf08b80f4e23b97d943ad93d14fd"]

    assert member.last_save == datetime.datetime.fromtimestamp(
        1599217969.829, tz=datetime.timezone.utc
    )
    assert member.inv_armor.type == 0
    assert (
        member.inv_armor.data
        == "H4sIAAAAAAAAAONiYOBkYMzkYmBgYGEAAQCp5xppEQAAAA\u003d\u003d"
    )
    assert member.first_join == datetime.datetime.fromtimestamp(
        1589445775.678, tz=datetime.timezone.utc
    )
    assert member.first_join_hub == 277843
    assert member.stats == {
        "pet_milestone_ores_mined": 287.0,
        "highest_critical_damage": 38.25,
        "kills": 10.0,
        "kills_zombie": 5.0,
        "deaths": 2.0,
        "deaths_spider": 2.0,
        "kills_spider": 1.0,
        "kills_lapis_zombie": 1.0,
        "kills_skeleton": 3.0,
    }
    assert member.tutorial == [
        "first_join",
        "zone_village",
        "tutorial_npc_crafter",
        "zone_auction_house",
        "tutorial_npc_psychic",
        "tutorial_npc_instructor",
        "tutorial_npc_bugs",
        "tutorial_npc_trader",
        "tutorial_trade",
        "tutorial_npc_explorer",
        "zone_bazaar_alley",
        "tutorial_npc_quester",
        "zone_mine",
        "shop_mine_merchant",
        "zone_gold_mine",
        "shop_iron_forger",
        "togglemusic",
        "zone_deep_caverns",
        "zone_deep_caverns_room_1",
        "zone_deep_caverns_room_2",
        "zone_deep_caverns_room_3",
        "zone_deep_caverns_room_4",
        "zone_deep_caverns_room_5",
        "shop_adventurer",
        "shop_farm_merchant",
    ]
    assert member.coin_purse == 1100.25
    assert member.last_death == 37364569
    assert member.crafted_generators == [
        "IRON_1",
        "COAL_1",
        "COBBLESTONE_1",
        "COBBLESTONE_2",
    ]
    assert member.visited_zones == [
        "dynamic_portal_island",
        "village",
        "auction_house",
        "bazaar_alley",
        "mine",
        "gold_mine",
        "deep_caverns",
        "deep_caverns_room_1",
        "deep_caverns_room_2",
        "deep_caverns_room_3",
        "deep_caverns_room_4",
        "deep_caverns_room_5",
    ]
    assert member.fairy_souls_collected == 1
    assert member.fairy_souls == 1
    assert member.death_count == 2
    assert member.pets == []
