import asyncio
from websockets import serve
import json
import os
import threading
import pyautogui
from io import BytesIO

async def echo(websocket):
    async for message in websocket:
        f=open("games.json","r")
        for appName in f.readlines():
            if json.loads(appName)["name"]==message:
                os.system("start "+json.loads(appName)["path"])
        x = threading.Thread(target=getScreen,args=(websocket,))
        x.start()
 
def getScreen(websocket):
    while True:
        myScreenshot = pyautogui.screenshot()
        resizedscreen=myScreenshot.resize((256,144))
        im_file = BytesIO()
        resizedscreen.save(im_file, format="JPEG")
        im_bytes = im_file.getvalue()
        asyncio.run(asyncio.sleep(0.5))
        asyncio.run(websocket.send(im_bytes))
    
async def main():
    async with serve(echo, "0.0.0.0", 3000):
        await asyncio.Future()  # run forever

asyncio.run(main())
