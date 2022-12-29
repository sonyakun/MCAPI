import aiohttp
import base64
import asyncio
import json
        
async def get_status(ip="mc.hypixel.net", stat=0, stat1=0, section=False):
    async with aiohttp.ClientSession() as session:
        offical_api = f'https://api.mcstatus.io/v2/status/java/{ip}'
        async with session.get(offical_api) as resp:
            offical_api = await resp.json()
        if section == True:
            return offical_api[stat][stat1]
        else:
            return offical_api[stat]