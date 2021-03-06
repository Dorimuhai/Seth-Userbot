# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import ALIVE_NAME, CMD_HELP, StartTime, DEVS
from userbot.events import register

absen = [
    "**Eh ada seth**",
    "**Hadir ganteng** ð¥µ",
    "**Hadir bro** ð",
    "**Hadir kak** ð",
    "**Hadir bang seth** ð",
    "**Hadir kak maap telat** ð¥º",
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def _(seth):
    await seth.reply(random.choice(absen))


@register(outgoing=True, pattern="^.sping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**ð ADA BABIð **")
    await pong.edit("**ðð ADA BABI ðð**")
    await pong.edit("**ððð ADA BABI ððð**")
    await pong.edit("**ðððð LU BABI ðððð**")
    await pong.edit("**ððððð OINKK ððððð**")
    await pong.edit("**ðððððð OINKK ðððððð**")
    await pong.edit("**ððððððð OINKK ððððððð**")
    await pong.edit("`.................ð`")
    await pong.edit("`................ð.`")
    await pong.edit("`...............ð..`")
    await pong.edit("`..............ð...`")
    await pong.edit("`.............ð....`")
    await pong.edit("`............ð.....`")
    await pong.edit("`...........ð......`")
    await pong.edit("`..........ð.......`")
    await pong.edit("`.........ð........`")
    await pong.edit("`........ð.........`")
    await pong.edit("`.......ð..........`")
    await pong.edit("`......ð...........`")
    await pong.edit("`.....ð............`")
    await pong.edit("`....ð.............`")
    await pong.edit("`...ð..............`")
    await pong.edit("`..ð...............`")
    await pong.edit("`.ð................`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**{ALIVE_NAME}**        \n"
        f"**â¾Kecepatan : ** %sms  \n"
        f"**â¾Branch : ** Seth-Userbot \n" % (duration)
    )


@register(outgoing=True, pattern="^.lping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**`{ALIVE_NAME}`**\n"
        f"â§ **-ê±ÉªÉ¢É´á´Ê- :** "
        f"`%sms` \n"
        f"â§ **-á´á´á´Éªá´á´- :** "
        f"`{uptime}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat...__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat.__")
    await pong.edit("__Sedang Memuat..__")
    await pong.edit("__Sedang Memuat...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**â¡ï¸sá´á´Ê-á´sá´ÊÊá´á´â¡ï¸**\n"
        f"â¾ __Signal__    __:__ "
        f"`%sms` \n"
        f"â¾ __Uptime__ __:__ "
        f"`{uptime}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.sinyal$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Mengecek Sinyal...**")
    await pong.edit("**0% ââââââââââ**")
    await pong.edit("**20% ââââââââââ**")
    await pong.edit("**40% ââââââââââ**")
    await pong.edit("**60% ââââââââââ**")
    await pong.edit("**80% ââââââââââ**")
    await pong.edit("**100% ââââââââââ**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**â¡ï¸sá´á´Ê-á´sá´ÊÊá´á´â¡ï¸**\n"
        f"** â¹  SÉªÉ¢É´á´Ê   :** "
        f"`%sms` \n"
        f"** â¹  Uá´á´Éªá´á´  :** "
        f"`{uptime}` \n"
        f"** â¹  Oá´¡É´á´Ê   :** `{ALIVE_NAME}` \n" % (duration)
    )


@register(outgoing=True, pattern="^.ping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**ð£**")
    await pong.edit("**ð£ð£**")
    await pong.edit("**ð£ð£ð£**")
    await pong.edit("**ââ¿- PONG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**DUARâ¨!!ð**\n"
        f"â¥ **á´ÉªÉ´É¢:** "
        f"`%sms` \n"
        f"â¥ **á´á´á´Éªá´á´:** "
        f"`{uptime}` \n"
        f"**â³ á´Ê É´á´á´á´:** `{ALIVE_NAME}`" % (duration)
    )


@register(outgoing=True, pattern="^.kecepatan$")
async def speedtst(spd):
    """For .speed command, use SpeedTest to check server speeds."""
    await spd.edit("**Sedang Menjalankan Tes Kecepatan Jaringan,Mohon Tunggu...**")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit(
        "**Kecepatan Jaringan:\n**"
        " âââââââââââââââââ \n"
        f"â§ **Dimulai Pada :**  \n"
        f"`{result['timestamp']}` \n"
        "â§ **Download:** "
        f"`{speed_convert(result['download'])}` \n"
        "â§ **Upload:** "
        f"`{speed_convert(result['upload'])}` \n"
        "â§ **Signal:** "
        f"`{result['ping']}` \n"
        "â§ **ISP:** "
        f"`{result['client']['isp']}` \n"
        "â§ **BOT:** â¡seth-userbotâ¡"
    )


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2 ** 10
    zero = 0
    units = {0: "", 1: "Kb/s", 2: "Mb/s", 3: "Gb/s", 4: "Tb/s"}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^.pong$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    start = datetime.now()
    await pong.edit("`Pong...........ð¤`")
    await pong.edit("`Pong..........ð¤.`")
    await pong.edit("`Pong.........ð¤..`")
    await pong.edit("`Pong........ð¤...`")
    await pong.edit("`Pong.......ð¤....`")
    await pong.edit("`Pong......ð¤.....`")
    await pong.edit("`Pong.....ð¤......`")
    await pong.edit("`Pong....ð¤.......`")
    await pong.edit("`Pong...ð¤........`")
    await pong.edit("`Pong..ð¤.........`")
    await pong.edit("`Pong.ð¤..........`")
    await pong.edit("`Pongð¤...........`")
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**â¡Oá´¡É´á´Ê : {ALIVE_NAME}**\nð `%sms`" % (duration))


@register(outgoing=True, pattern="^.pink$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8â===D")
    await pong.edit("8=â==D")
    await pong.edit("8==â=D")
    await pong.edit("8===âD")
    await pong.edit("8==â=D")
    await pong.edit("8=â==D")
    await pong.edit("8â===D")
    await pong.edit("8=â==D")
    await pong.edit("8==â=D")
    await pong.edit("8===âD")
    await pong.edit("8==â=D")
    await pong.edit("8=â==D")
    await pong.edit("8â===D")
    await pong.edit("8=â==D")
    await pong.edit("8==â=D")
    await pong.edit("8===âD")
    await pong.edit("8===âDð¦")
    await pong.edit("8====Dð¦ð¦")
    await pong.edit("**CROOTTTT PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**DUARRR!! **\n**NMAXXX** : %sms\n**Bot Uptime** : {uptime}ð" % (duration)
    )


@register(outgoing=True, pattern=r"^\.fping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    datetime.now()
    await pong.edit(".                       /Â¯ )")
    await pong.edit(".                       /Â¯ )\n                      /Â¯  /")
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /"
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸"
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸\n          /'/   /    /       /Â¨Â¯\\ "
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')"
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /"
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /\n          \\                _.â¢Â´"
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /\n          \\                _.â¢Â´\n            \\              ("
    )
    await pong.edit(
        ".                       /Â¯ )\n                      /Â¯  /\n                    /    /\n              /Â´Â¯/'   '/Â´Â¯Â¯`â¢Â¸\n          /'/   /    /       /Â¨Â¯\\ \n        ('(   (   (   (  Â¯~/'  ')\n         \\                        /\n          \\                _.â¢Â´\n            \\              (\n              \\  "
    )


CMD_HELP.update(
    {
        "ping": "ð¾ð¤ð¢ð¢ðð£ð: `.ping` | `.lping` | `.xping` | `.sinyal` | `.sping` | `.pink` | `.fping`\
         \nâ³ : Untuk Menunjukkan Ping Bot Anda.\
         \n\nð¾ð¤ð¢ð¢ðð£ð: `.kecepatan`\
         \nâ³ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\nð¾ð¤ð¢ð¢ðð£ð: `.pong`\
         \nâ³ : Sama Seperti Perintah Ping."
    }
)
