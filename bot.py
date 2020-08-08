import os
import random
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

#ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
@bot.command()
async def ping(ctx):
    await ctx.send(f'延遲：{round(bot.latency*1000)} 毫秒(ms)')

#發送本地圖片(如果想發送網路圖片，直接send網址就好)
@bot.command()
async def about(ctx):
    #發送檔案的處理方式
    pic = discord.File(bcdata['info_pic'])
    await ctx.send(file = pic)

#發送隨機圖片(使用random.choice)
@bot.command()
async def meme(ctx):
    random_pic = random.choice(bcdata['meme_pics'])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

bot.run(bcdata['token'])