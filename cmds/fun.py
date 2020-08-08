import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata
import json
import random

class Fun(Cog_Extension):
    #發送本地圖片(如果想發送網路圖片，直接send網址就好)
    #發送隨機圖片(使用random.choice)
    @commands.command()
    async def meme(self, ctx):
        random_pic = random.choice(bcdata['meme_pics'])
        pic = discord.File(random_pic)#發送檔案的處理方式
        await ctx.send(file = pic)#用file來定要發送檔案
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('牛牛') and msg.author != self.bot.user:
            cow_msg = ['安安', 'hello', '叫我嗎?', 'owo']
            message = random.choice(cow_msg)
            await msg.channel.send(message)

def setup(bot):
    bot.add_cog(Fun(bot))