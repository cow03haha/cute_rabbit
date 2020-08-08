import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata
import datetime
import pytz

class Main(Cog_Extension):
    #ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'延遲：{round(self.bot.latency*1000)} 毫秒(ms)')
    
    #鸚鵡
    @commands.command()
    async def say(self, ctx, message):
        await ctx.send(message)
    
    @commands.command()
    async def about(self, ctx):
        tw = pytz.timezone('Asia/Taipei')
        embed=discord.Embed(title="about", description="開心莊園專用bot", color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
        embed.set_author(name="cow03", icon_url="https://i.imgur.com/QinbCaq.png")
        embed.set_thumbnail(url="https://i.imgur.com/za5ATTg.png")
        embed.add_field(name="作者", value="cow03#7829", inline=True)
        embed.add_field(name="support server", value="[link](https://discord.gg/DRqZk6Y)", inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Main(bot))