import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata

class Main(Cog_Extension):
    #ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'延遲：{round(self.bot.latency*1000)} 毫秒(ms)')
    
    #鸚鵡
    @commands.command()
    async def say(self, ctx, message):
        await ctx.send(message)
    
    #發送本地圖片(如果想發送網路圖片，直接send網址就好)
    @commands.command()
    async def about(self, ctx):
        pic = discord.File(bcdata['info_pic'])#發送檔案的處理方式
        await ctx.send(file = pic)#用file來定要發送檔案

def setup(bot):
    bot.add_cog(Main(bot))