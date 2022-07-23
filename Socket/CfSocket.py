import asyncio
from websockets import serve
import json
import os
import pyautogui
from io import BytesIO
from pynput.keyboard import KeyCode,Controller
from pynput.mouse import Button
from pynput import mouse

keyboard = Controller()
mouse=mouse.Controller()

Buttons=[
    "",
    Button.left,
    Button.right,
    "",
    Button.middle,
]

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
        jsonMessage=json.loads(message)
        if "key" in jsonMessage:
            keyboard.press(KeyCode(int(jsonMessage["key"])))
            keyboard.release(KeyCode(int(jsonMessage["key"])))
        if "mouse" in jsonMessage:
            mouse.move(jsonMessage['mouse'][0],jsonMessage['mouse'][1])
        if "click" in jsonMessage:
            mouse.click(Buttons[jsonMessage['click']],1)
        if "wheel" in jsonMessage:
            mouse.scroll(0,jsonMessage["wheel"])
        if "open" in jsonMessage:
            f=open("games.json","r")
            for appName in f.readlines():
                if json.loads(appName)["name"]==jsonMessage["open"]:
                    os.system("start "+json.loads(appName)["path"])
                    mouse.position=(0,0)
                    break

async def echo(websocket):
    await asyncio.gather(
        getScreen(websocket),
        messageSys(websocket),
    )

async def main():
    async with serve(echo, "0.0.0.0", 3000):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())
    print("Websocket Running...")
