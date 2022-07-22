import asyncio
from websockets import serve
import json
import os
import pyautogui
from io import BytesIO
from pynput.keyboard import KeyCode,Controller

keyboard = Controller()

async def getScreen(websocket):
    try:
        while True:
            myScreenshot = pyautogui.screenshot()
            resizedscreen=myScreenshot.resize((1920,1080))
            im_file = BytesIO()
            resizedscreen.save(im_file, format="JPEG")
            im_bytes = im_file.getvalue()
            await websocket.send(im_bytes)
            await asyncio.sleep(.1)
    except:
        print("Err")

async def messageSys(websocket):
    async for message in websocket:
        if "key" in json.loads(message):
            keyboard.press(KeyCode(int(json.loads(message)["key"])))
            keyboard.release(KeyCode(int(json.loads(message)["key"])))
        if "open" in json.loads(message):
            f=open("games.json","r")
            for appName in f.readlines():
                if json.loads(appName)["name"]==json.loads(message)["open"]:
                    os.system("start "+json.loads(appName)["path"])
                    break

async def echo(websocket):
    await asyncio.gather(
        getScreen(websocket),
        messageSys(websocket),
    )

async def main():
    async with serve(echo, "0.0.0.0", 3000):
        await asyncio.Future()  # run forever

asyncio.run(main())
