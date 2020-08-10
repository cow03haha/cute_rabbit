import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata
import json

class Admin(Cog_Extension):
    @commands.Cog.listener()
    async def on_member_join(self, member):
        #print(f'{member} 加入了牛牛神殿')
        channel = self.bot.get_channel(int(bcdata['join_channel']))
        await channel.send(f'{member} 加入了牛牛神殿')

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #print(f'{member} 離開了牛牛神殿')
        channel = self.bot.get_channel(int(bcdata['leave_channel']))
        await channel.send(f'{member} 離開了牛牛神殿')

    @commands.has_any_role(bcdata["管理員", "傳說區管理員", "亂鬥區管理員", "第五區管理員", "麥塊區管理員", "跑跑區管理員"])
    async def clear(self, ctx, count:int):
        await ctx.channel.purge(limit=count+1)
        await ctx.send(f'清理{count}條訊息成功')
        await ctx.channel.purge(limit=1)

def setup(bot):
    bot.add_cog(Admin(bot))