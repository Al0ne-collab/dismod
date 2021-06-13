import os
import requests
import sys
import discord
import time
import threading
import cv2
from discord import *
from PIL import GifImagePlugin, Image, ImageSequence
from imgpy import Img

client = discord.Client()

@client.event
async def on_ready():
    print("Connected as", client.user)
    print("Select one:\n\033[4;49;96m1\033[0m. New version\n\033[4;49;96m2\033[0m. Old version")
    print()
    while True:
        select = input()
        if "1" in select:
            with open("save.txt", "w") as test:
                test.write("1")
            break
        if "2" in select:
            with open("save.txt", "w") as test:
                test.write("2")
            break
        else:
            print("Sorry select just one option!")
            time.sleep(1)
            os.system("clear")
    os.system("clear")
    print("\033[2;49;31m Nitro-free emoji has been \033[0;91mactivated\033[0m\033[2;49;31m. \nPlease type emoji. for example: :emoji_123:")
    with open("update.txt", "r") as test:
        print()
        print(test.read())
@client.event
async def on_message(message):
    with open("save.txt", "r") as test:
        ok = test.read()
    tata, frames, l, info = [], [], 0, {}
    for t in client.emojis:
        tata.append(t)
    ## for new version
    if ok == "1":
        async for hack in message.channel.history(limit=1):
            for t in tata:
                if hack.content == ":" + str(t.name) + ":":
                    await message.delete()
                    req = requests.get(t.url).content
                    if not t.animated:
                        with open("image.png", "wb") as test:
                            test.write(req)
                        image = cv2.imread("image.png", cv2.IMREAD_UNCHANGED)
                        image = cv2.resize(image, (48, 48))
                        cv2.imwrite("image.png", image, [cv2.IMWRITE_PNG_COMPRESSION, 9])
                        await message.channel.send(file=File("image.png"))
                    else:
                        with open("animate.gif", "wb") as test:
                            test.write(req)
                        im = Image.open("animate.gif")
                        frames = ImageSequence.Iterator(im)
                        def thumbn(frames):
                            for frame in frames:
                                thumb = frame.copy()
                                thumb.thumbnail((48, 48), Image.ANTIALIAS)
                                yield thumb
                        frames = thumbn(frames)
                        om = next(frames)
                        print(im.info)
                        om.info = im.info
                        print(om.info)
                        om.save("animate.gif", save_all=True, append_images=list(frames), loop=0)
                        await message.channel.send(file=File("animate.gif"))
    if ok == "2":
        async for mas in message.channel.history(limit=1):
            for t in tata:
                if mas.content == ":" + str(t.name) + ":":
                    await message.delete()
                    await message.channel.send(t.url)
client.run(sys.argv[1], bot=False)
