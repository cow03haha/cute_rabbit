import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata, check_owner
import datetime
import pytz

class Main(Cog_Extension):
    '''基本指令'''
    #ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
    @commands.command()
    async def ping(self, ctx):
        '''測試延遲。'''
        await ctx.send(f'延遲：{round(self.bot.latency*1000)} 毫秒(ms)')
    
    #鸚鵡
    @commands.command()
    async def say(self, ctx, *, msg):
        '''你說我回。用法：/say 要說的話'''
        await ctx.send(msg)
    
    @commands.command()
    async def info(self, ctx):
        '''bot資訊。'''
        tw = pytz.timezone('Asia/Taipei')
        embed=discord.Embed(title="about", description="開心莊園專用bot", color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
        embed.set_author(name="cow03", icon_url="https://i.imgur.com/QinbCaq.png")
        embed.set_thumbnail(url="https://i.imgur.com/za5ATTg.png")
        embed.add_field(name="作者", value="cow03#7829", inline=True)
        embed.add_field(name="support server", value="[link](https://discord.gg/DRqZk6Y)", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self, ctx, *, msg):
        '''你說我回(你傳的訊息會刪除)。用法：/sayd 要說的話'''
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.check(check_owner)
    @commands.command()
    
    async def says(self, ctx, channel, *, msg):
        '''在特定頻道傳訊息。用法：/says 頻道id 要說的話'''
        channel = self.bot.get_channel(int(channel))
        await channel.send(msg)

    @commands.command()
    async def time(self, ctx):
        '''顯示現在的時間。'''
        tw = pytz.timezone('Asia/Taipei')
        time = datetime.datetime.now(tz=tw).strftime("%H:%M:%S")
        await ctx.send(f'現在的時間是 {time}')

    @commands.command()
    async def srvinfo(self, ctx):
        '''顯示伺服器資訊。'''
        guild = self.bot.get_guild(ctx.guild.id)
        owner = guild.owner
        await ctx.send(f'此伺服器擁有者是 {owner}')

def setup(bot):
    bot.add_cog(Main(bot))