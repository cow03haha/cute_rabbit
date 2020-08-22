import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata
import asyncio
import json
import datetime
import pytz

class Admin(Cog_Extension):
    '''管理指令'''
    #member加入
    @commands.Cog.listener()
    async def on_member_join(self, member):
        global newer
        newer = member
        if member.guild.id == int(bcdata['rabbit_guild']['guild_id']):
            #print(f'{member} 加入了牛牛神殿')
            #channel = member.guild.get_channel(int(bcdata['welcome_channel']))
            role = member.guild.get_role(int(bcdata['rabbit_guild']['guest_role']))
            today = datetime.datetime.now().strftime('%Y-%m-%d')
            await member.add_roles(role)

            embed=discord.Embed(title=" ", description=f'歡迎來到{member.guild}~\n\
                                                        記得先看完 <#743353331363217418>\n\
                                                        之後再按照 <#746312391955841074> 的指示來驗證並正式加入本群\n', color=0xf5ed00)
            embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
            embed.set_footer(text=today)
            await member.send(embed=embed)
        
    #member退出
    '''
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        #print(f'{member} 離開了牛牛神殿')
        channel = self.bot.get_channel(int(bcdata['leave_channel']))
        await channel.send(f'{member} 離開了牛牛神殿')'''

    #驗證系統 
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content == '同意' and msg.author != self.bot.user and msg.channel.id == int(bcdata['rabbit_guild']['auth_channel']):
            await msg.delete()
            guest = msg.guild.get_role(int(bcdata["rabbit_guild"]['guest_role']))
            await msg.author.remove_roles(guest)

            tw = pytz.timezone('Asia/Taipei')
            embed=discord.Embed(title=" ", description=f'恭喜你正式加入本群:)\n\
                                                        記得去 <#743854911078531219> 領取身分組\n\
                                                        (這是自動息請勿回覆,如有問題請直接私訊管理員)', color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
            embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
            await msg.author.send(embed=embed)

        elif msg.content != '同意' and msg.author != self.bot.user and msg.channel.id == int(bcdata["rabbit_guild"]["auth_channel"]):
            await msg.delete()
            await msg.channel.send(f'{msg.author.mention} 驗證失敗，請再看仔細一點 ༼ ◕д ◕ ༽', delete_after=10)
        #歡迎訊息
        if msg.channel.id == int(bcdata['rabbit_guild']['welcome_channel']) and msg.author.id == 276060004262477825:
            tw = pytz.timezone('Asia/Taipei')
            embed=discord.Embed(title=" ", description=f'☆歡迎 {newer.mention} 來到Rabbit♡Fairy ☆\n\n\
                                                        新仁先去 <#743353331363217418> 了解我們的規定\n\
                                                        再來通過 <#746312391955841074> 即可成為我們的一員\n\
                                                        這邊 <#743768856853479525> 可以選擇你常玩的遊戲\n\
                                                        以及你自己喜歡的顏色(ฅ´ω`ฅ) \n\n\
                                                        ☆♡☆♡☆♡☆♡☆♡☆♡☆♡', color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
            embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
            await msg.channel.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count:int):
        '''清理當前頻道的訊息。用法：/clear 數量'''
        await ctx.message.delete()
        await ctx.channel.purge(limit=count, bulk=True)
        await ctx.send(f'清理{count}條訊息成功', delete_after=3)
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clearafter(self, ctx, year: int,month: int,day: int, hour: int,minute: int):
        '''清理當前頻道特定時間後的訊息。用法：/clear 年 月 日 小時 分鐘
        ex. /clearafter 2020 8 11 14 30'''
        await ctx.message.delete()
        if hour < 8:
            day = day-1
            hour = 24+hour-8
        else:
            hour = hour-8
        time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        await ctx.channel.purge(after=time, bulk=True)
        if hour+8 > 24:
            day = day+1
            hour = hour+8-24
        else:
            hour = hour+8
        time = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute)
        await ctx.send(f'清理{time}之後的訊息成功', delete_after=3)
    
    #recation role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        #reaction role example
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '🖥':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(614812329258778635)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功')
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        #reaction role example
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '🖥':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(614812329258778635)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        
def setup(bot):
    bot.add_cog(Admin(bot))