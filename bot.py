import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print("bot online!")

bot.run('NjIwMTc2NTg1Mzk1NDA0ODMw.XXS-dA.izPJlDfgtII2bj3YUJKVCyhTPro')