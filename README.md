# MineAPI
MineAPI is Minecraft Servers API Wrapper.  


# reference
## The Hive API
```python
from bedrock.hive import main
import asyncio

print(asyncio.run(main.status_get(player="sonya4327", game="sky", get="kills")))
# API Reference is https://api.playhive.com/api/documentation.
```
## MCSTATUS API
### Bedrock
```python
from bedrock.MCStatus import main
import asyncio

print(asyncio.run(main.get_status(ip="pe.mineplex.com", stat="port")))
# API Reference is https://mcstatus.io/docs.
```
### Java
```python
from java.MCStatus import main
import asyncio

print(asyncio.run(main.get_status(ip="mc.hypixel.net", stat="port")))
# API Reference is https://mcstatus.io/docs.
```