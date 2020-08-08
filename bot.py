import os
import discord
from discord.ext import commands
import json

with open('settings.json', 'r', encoding='utf8') as bcfile:
    bcdata = json.load(bcfile)

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print("bot online!")

@bot.event
async def on_member_join(member):
#    print(f'{member} 加入了牛牛神殿')
    channel = bot.get_channel(int(bcdata['join_channel']))
    await channel.send(f'{member} 加入了牛牛神殿')

@bot.event
async def on_member_remove(member):
#    print(f'{member} 離開了牛牛神殿')
    channel = bot.get_channel(int(bcdata['leave_channel']))
    await channel.send(f'{member} 離開了牛牛神殿')

@bot.command()
async def ping(ctx):
    await ctx.send(f'延遲：{round(bot.latency*1000)} 毫秒(ms)')


bot.run(bcdata['token'])