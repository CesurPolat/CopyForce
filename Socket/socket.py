import asyncio
from flask import jsonify
from websockets import serve
import json
import os

async def echo(websocket):
    #await websocket.send("Welcome Message")
    async for message in websocket:
        await websocket.send(message)
        f=open("games.json","r")
        for appName in f.readlines():
            if json.loads(appName)["name"]==message:
                os.system("start "+json.loads(appName)["path"])
            

async def main():
    async with serve(echo, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())