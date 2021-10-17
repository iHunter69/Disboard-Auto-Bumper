import discord, os, time
from discord.ext import commands

bot = commands.Bot(command_prefix = ".", self_bot=True)

@bot.event
async def on_ready():
    print("Auto Bump bot started!!")
    while True:
        channel = bot.get_channel(872526509431226450)
        await channel.send("!d bump")
        print("bumped")
        time.sleep(7500)

bot.run("TOKEN", bot = False)
