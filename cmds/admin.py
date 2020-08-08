import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata

class Admin:
    @commands.event
    async def on_member_join(self, member):
        #print(f'{member} 加入了牛牛神殿')
        channel = commands.get_channel(int(bcdata['join_channel']))
        await channel.send(f'{member} 加入了牛牛神殿')

    @commands.event
    async def on_member_remove(self, member):
        #print(f'{member} 離開了牛牛神殿')
        channel = commands.get_channel(int(bcdata['leave_channel']))
        await channel.send(f'{member} 離開了牛牛神殿')