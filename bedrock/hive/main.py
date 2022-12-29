import aiohttp
import asyncio
import json

async def status_get(game, player, get="played"):
    async with aiohttp.ClientSession() as session:
        hive_api = f'https://api.playhive.com/v0/game/all/{game}/{player}'
        async with session.get(hive_api) as resp:
            hive_api = await resp.json()
            return hive_api[get]
