import discord
from discord.ext import commands
from cores.classes import Cog_Extension

class Main(Cog_Extension):
    #ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'延遲：{round(self.bot.latency*1000)} 毫秒(ms)')

def setup(bot):
    bot.add_cog(Main(bot))