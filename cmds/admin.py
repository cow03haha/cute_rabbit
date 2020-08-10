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

    @commands.command()
    async def clear(self, ctx, count:int):
        '''清理當前頻道的訊息'''
        if bcdata['admin_roles'] in ctx.author.roles:
            await ctx.channel.purge(limit=count+1)
            await ctx.send(f'清理{count}條訊息成功')
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send('只有管理員能用這個指令')

def setup(bot):
    bot.add_cog(Admin(bot))