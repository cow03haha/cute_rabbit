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
        #print(f'{member} 加入了牛牛神殿')
        channel = member.guild.get_channel(int(bcdata['welcome_channel']))
        role = member.guild.get_role(int(bcdata['guest_role']))
        await member.add_roles(role)
        await member.send(f'歡迎來到{member.guild}~\n新人請一定要看 <#612592834884796436> 跟 <#623149304529289225> \n之後按照上面的指示來驗證以正式加入本群\n')

        #tw = pytz.timezone('Asia/Taipei')
        #embed=discord.Embed(title=" ", description="----歡迎新的小夥伴{mention}來到{guild}----\n\n新人請到 <#612592834884796436> 來了解本群規則\n然後再到 <#623149304529289225> 完成驗證來加入該群喔~\n驗證完後請到 <#612551316346109983> 領取自己有玩的遊戲的身分組(驗證完後才會看到\n時不時也可以到 <#613004916079853581> 獲取本群最新資訊\n\n------------------------------------------------", color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
        #embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
        #await channel.send(embed=embed)

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
        if msg.content == '同意' and msg.author != self.bot.user and msg.channel.id == int(bcdata['auth_channel']):
            await msg.delete()
            guest = msg.guild.get_role(int(bcdata['guest_role']))
            newer = msg.guild.get_role(int(bcdata['newer_role']))
            await msg.author.add_roles(newer)
            await msg.author.remove_roles(guest)
            await msg.author.send(f'恭喜你正式加入本群:)\n記得觀看 <#613004916079853581> 來獲取更多資訊\n如果你是discord新手的話也歡迎參考<#623079544227889182>\n關於bot的使用請參考<#613333035659558922>並在對應的頻道使用\n(這是自動訊息請勿回覆,如有問題請直接私訊管理員)')

        elif msg.content != '同意' and msg.author != self.bot.user and msg.channel.id == int(bcdata['auth_channel']):
            await msg.delete()
            await msg.channel.send('驗證失敗，請再看仔細一點！', delete_after=5)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, count:int):
        '''清理當前頻道的訊息。用法：/clear 數量'''
        await ctx.message.delete()
        await ctx.channel.purge(limit=count)
        await ctx.send(f'清理{count}條訊息成功', delete_after=3)
    
    #recation role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        #PC
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '🖥':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(614812329258778635)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功')
        #傳說
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:AOVicon:612550770772017169>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(610181297217863692)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#621994307431301130> 看看喔')
        #第五
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:I5icon:612550771967262720>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(610179872152616961)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#621994116292673536> 看看喔')
        #荒野
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:bsicon:612550771623591937>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(610181340897345546)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#621994581688451082> 看看喔')
        #決勝時刻m
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:codmicon:628200401220665344>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(628180918670065674)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#628181683186696192> 看看喔')
        #minecraft
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:MCicon:638362113131282463>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(638001209092997134)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#638000562041782282> 看看喔')
        #皇室
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:cricom:713945207808196660>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(713945766699335691)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#713947690831970364> 看看喔')
        #跑跑rush+
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:runicom:713945243111653387>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(713945765004705834)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#713952107258052738> 看看喔')
        #明日方舟
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:arkicon:736092448841007194>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(736091703873634434)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功')
        #活躍玩家
        if payload.message_id == 672672848514646036:
            if str(payload.emoji) == '<:minecraftheart:623144393326723072>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(670280115556712458)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n公告或是群友揪人都會@這個身分組，請特別注意')
        #聊天
        if payload.message_id == 672672848514646036:
            if str(payload.emoji) == '💬':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(672669628018982912)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功\n記得去 <#672670934234038272> 看看喔')
        #DJ
        if payload.message_id == 719415779233235045:
            if str(payload.emoji) == '🎵':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(719415296045219881)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send(f'領取 **{role}** 身分組成功')
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        #PC
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '🖥':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(614812329258778635)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #傳說
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:AOVicon:612550770772017169>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(610181297217863692)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #第五
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:I5icon:612550771967262720>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(610179872152616961)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #荒野
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:bsicon:612550771623591937>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(610181340897345546)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #決勝時刻m
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:codmicon:628200401220665344>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(628180918670065674)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #minecraft
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:MCicon:638362113131282463>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(638001209092997134)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #皇室
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:cricom:713945207808196660>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(713945766699335691)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #跑跑rush+
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:runicom:713945243111653387>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(713945765004705834)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #明日方舟
        if payload.message_id == 612553821528391702:
            if str(payload.emoji) == '<:arkicon:736092448841007194>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(736091703873634434)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #活躍玩家
        if payload.message_id == 672672848514646036:
            if str(payload.emoji) == '<:minecraftheart:623144393326723072>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(670280115556712458)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #聊天
        if payload.message_id == 672672848514646036:
            if str(payload.emoji) == '💬':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(672669628018982912)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
        #dj
        if payload.message_id == 719415779233235045:
            if str(payload.emoji) == '🎵':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(719415296045219881)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send(f'移除 **{role}** 身分組成功')
    
def setup(bot):
    bot.add_cog(Admin(bot))