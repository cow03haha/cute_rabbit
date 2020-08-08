import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata
import json
import random

class Fun(Cog_Extension):
    #發送本地圖片(如果想發送網路圖片，直接send網址就好)
    @commands.command()
    async def about(self, ctx):
        pic = discord.File(bcdata['info_pic'])#發送檔案的處理方式
        await ctx.send(file = pic)#用file來定要發送檔案

    #發送隨機圖片(使用random.choice)
    @commands.command()
    async def meme(self, ctx):
        random_pic = random.choice(bcdata['meme_pics'])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

def setup(bot):
    bot.add_cog(Fun(bot))