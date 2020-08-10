import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata

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
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count:int):
        '''清理當前頻道的訊息'''
        await ctx.channel.purge(limit=count+1)
        await ctx.send(f'清理{count}條訊息成功', delete_after=3)
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == 742363869015703593:
            if str(payload.emoji) == '<:blobpopcorn:713660254440783932>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(742364064369475644)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功')

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == 742363869015703593:
            if str(payload.emoji) == '<:blobpopcorn:713660254440783932>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(742364064369475644)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')

def setup(bot):
    bot.add_cog(Admin(bot))