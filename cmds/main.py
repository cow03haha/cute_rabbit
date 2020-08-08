import discord
from discord.ext import commands

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'延遲：{round(self.bot.latency*1000)} 毫秒(ms)')

def setup(bot):
    bot.add_cog(Main(bot))