import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata, check_owner
import datetime
import time
import pytz

class Main(Cog_Extension):
    '''基本指令'''
    #ping指令(discord給的單位為秒，直接乘於1000得到毫秒(ms)，在用round取整數)
    @commands.command()
    async def ping(self, ctx):
        '''測試延遲。'''
        t = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.trigger_typing()

        bot = round((t2 - t) * 1000)
        ws = int(self.bot.latency * 1000)
        await ctx.send(f'延遲：{bot} 毫秒(ms)\nWebsocket：{ws} 毫秒(ms)')
    
    #鸚鵡
    @commands.command()
    async def say(self, ctx, *, msg):
        '''你說我回。用法：/say 要說的話'''
        await ctx.send(msg)
    
    @commands.command(aliases=['about'])
    async def info(self, ctx):
        '''bot資訊。'''
        tw = pytz.timezone('Asia/Taipei')
        embed=discord.Embed(title="about", description="Rabbit♡Fairy專用bot", color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
        embed.set_author(name="cow03", icon_url="https://i.imgur.com/QinbCaq.png")
        embed.set_thumbnail(url="https://i.imgur.com/za5ATTg.png")
        embed.add_field(name="作者", value="<@315414910689476609>", inline=True)
        embed.add_field(name="support server", value="[link](https://discord.gg/DRqZk6Y)", inline=True)
        await ctx.send(embed=embed)
    
    @commands.command()
    async def sayd(self, ctx, *, msg):
        '''你說我回(你傳的訊息會刪除)。用法：/sayd 要說的話'''
        await ctx.message.delete()
        await ctx.send(msg)
    
    @commands.check(check_owner)
    @commands.command()
    
    async def says(self, ctx, channel: int, *, msg):
        '''在特定頻道傳訊息。用法：/says 頻道id 要說的話'''
        channel = self.bot.get_channel(channel)
        await channel.send(msg)

    @commands.command(aliases=['date'])
    async def time(self, ctx, tz):
        '''顯示現在的時間。用法：/time 時區，詳細時區列表請參考/help time
        日本 = jp
        台灣 = tw
        美國(中部) = us_mid
        美國(西岸) = us_west
        美國(東岸) = us_east
        英國 = uk
        土耳其 = tk'''
        if tz == 'tw':
            time = datetime.datetime.now().strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的台灣時間是 {time}')
        elif tz == 'jp':
            tz = pytz.timezone('Asia/Tokyo')
            time = datetime.datetime.now(tz=tz).strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的日本時間是 {time}')
        elif tz == 'us_east':
            tz = pytz.timezone('US/Eastern')
            time = datetime.datetime.now(tz=tz).strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的美國東岸時間是 {time}')
        elif tz == 'us_mid':
            tz = pytz.timezone('US/Central')
            time = datetime.datetime.now(tz=tz).strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的美國中部時間是 {time}')
        elif tz == 'us_west':
            tz = pytz.timezone('US/Pacific')
            time = datetime.datetime.now(tz=tz).strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的美國西岸時間是 {time}')
        elif tz == 'uk':
            tz = pytz.timezone('Etc/GMT+1')
            time = datetime.datetime.now(tz=tz).strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的英國時間是 {time}')
        elif tz == 'tk':
            tz = pytz.timezone('Turkey')
            time = datetime.datetime.now(tz=tz).strftime("%m-%d %H:%M:%S")
            await ctx.send(f'現在的土耳其時間是 {time}')
        else:
            await ctx.send('請輸入正確的時區!')

    @commands.command()
    async def srvinfo(self, ctx):
        '''顯示伺服器資訊。'''
        guild = self.bot.get_guild(ctx.guild.id)
        owner = guild.owner
        await ctx.send(f'此伺服器擁有者是 {owner}')

def setup(bot):
    bot.add_cog(Main(bot))