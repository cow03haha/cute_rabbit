import discord
from discord.ext import commands
from cores.classes import Cog_Extension
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
        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata = json.load(bcfile)
        
        if member.guild.id == int(bcdata['rabbit_guild']['guild_id']):
            #print(f'{member} 加入了牛牛神殿')
            #channel = member.guild.get_channel(int(bcdata['welcome_channel']))
            role = member.guild.get_role(int(bcdata['rabbit_guild']['guest_role']))
            tw = pytz.timezone('Asia/Taipei')
            await member.add_roles(role)

            embed=discord.Embed(title=" ", description=f'歡迎來到{member.guild}~\n記得先看完 <#743353331363217418>\n之後再按照 <#746312391955841074> 的指示來驗證並正式加入本群\n', color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
            embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
            await member.send(embed=embed)
        
    #member退出
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        
        with open('members.json', 'r', encoding='utf8') as bcfile:
                bcdata =json.load(bcfile)
        
        if member.id in bcdata["member_id"]:
            if bcdata[f'{member.id}']["custom_role"] != False:
                role = member.guild.get_role(bcdata[f'{member.id}']["custom_role"])
                await role.delete(reason="成員退出")
            bcdata["member_id"].remove(member.id)
            del bcdata[f'{member.id}']
            
            with open('members.json', 'w', encoding='utf8') as bcfile:
                json.dump(bcdata, bcfile, indent=4)
        
    @commands.Cog.listener()
    async def on_message(self, msg):
        
        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata = json.load(bcfile)

        #驗證系統 
        if msg.content == '同意' and msg.author != self.bot.user and msg.channel.id == int(bcdata['rabbit_guild']['auth_channel']):
            await msg.delete()
            guest = msg.guild.get_role(int(bcdata["rabbit_guild"]['guest_role']))
            await msg.author.remove_roles(guest)

            tw = pytz.timezone('Asia/Taipei')
            embed=discord.Embed(title=" ", description=f'恭喜你正式加入本群:)\n記得去 <#743854911078531219> 領取身分組\n(這是自動息請勿回覆,如有問題請直接私訊管理員)', color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
            embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
            await msg.author.send(embed=embed)

        elif msg.content != '同意' and msg.author != self.bot.user and msg.channel.id == int(bcdata["rabbit_guild"]["auth_channel"]):
            await msg.delete()
            await msg.channel.send(f'{msg.author.mention} 驗證失敗，請再看仔細一點 ༼ ◕д ◕ ༽', delete_after=10)

        #歡迎訊息
        if msg.channel.id == int(bcdata['rabbit_guild']['welcome_channel']) and msg.author.id == 276060004262477825:
            tw = pytz.timezone('Asia/Taipei')
            embed=discord.Embed(title=" ", description=f'☆歡迎 {newer.mention} 來到Rabbit♡Fairy ☆\n\n新仁先去 <#743353331363217418> 了解我們的規定\n再來通過 <#746312391955841074> 即可成為我們的一員\n這邊 <#743854911078531219> 可以選擇你常玩的遊戲\n以及你自己喜歡的顏色(ฅ´ω`ฅ)\n\n☆♡☆♡☆♡☆♡☆♡☆♡☆♡', color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
            embed.set_author(name="牛牛の僕", icon_url="https://imgur.com/za5ATTg.jpg")
            await msg.channel.send(embed=embed)
        
        #簽到系統
        if msg.channel.id == 753543338006806528 and msg.content == "簽" and msg.author.bot == False:
            with open("members.json", "r", encoding="utf8") as bcfile:
                bcdata =json.load(bcfile)
            
            if msg.author.id in bcdata["member_id"]:
                if bcdata[f'{msg.author.id}']["today"]:
                    await msg.channel.send(f'{msg.author.mention} 你今天已經簽到了!')
                    return
                if msg.author.name != bcdata[f'{msg.author.id}']["name"]:
                    bcdata[f'{msg.author.id}']["name"] = msg.author.name
                if msg.author.display_name != bcdata[f'{msg.author.id}']["nickname"]:
                    bcdata[f'{msg.author.id}']["nickname"] = msg.author.display_name
                 
                bcdata[f'{msg.author.id}']["today"] = True
                bcdata[f'{msg.author.id}']["total"] += 1
            else:
                bcdata[f'{msg.author.id}'] = { "name": msg.author.name, "nickname": msg.author.display_name, "total": 1, "today": True, "custom_role": False, "remain": False}
                bcdata["member_id"].append(msg.author.id)

            with open("members.json", "w", encoding="utf8") as bcfile:
                json.dump(bcdata, bcfile, indent=4)
            
            await msg.channel.send(f'{msg.author.mention} 簽到成功!，這是你連續簽到的第 **{bcdata[str(msg.author.id)]["total"]}** 天')
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def status(self, ctx, member: discord.User):
        '''檢查成員簽到狀態。用法/status @成員'''
        with open('members.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        
        if member.id in bcdata["member_id"]:
            user = bcdata[f'{member.id}']
            today = user["today"]
            name = user["name"]
            nickname = user["nickname"] 
            if today:
                today = "是"
            else:
                today = "否"
            if user["custom_role"]:
                custom_role = ctx.guild.get_role(user["custom_role"])
                role_str =f'擁有自訂身分組：是\n自訂身分組名稱：{custom_role.mention}'
            else:
                role_str="擁有自訂身分組：否"

            await ctx.send(f'名稱：{name}\n暱稱：{nickname}\nid：{member.id}\n已連續簽到：{user["total"]}天\n今天簽到狀態：{today}\n{role_str}')
        else:
            await ctx.send("沒有資料!")
    
    @commands.command(aliases=['申請'])
    async def apply(self, ctx, name, color: discord.Colour):
        if ctx.channel.id != 753542568939356220:
            await ctx.send("你不能在這個頻道使用此指令!")
            return
            
        with open('members.json', 'r', encoding='utf8') as bcfile:
            bcdata = json.load(bcfile)
        
        if ctx.author.id in bcdata["member_id"]:
            if bcdata[f'{ctx.author.id}']["total"] >= 3:
                if bcdata[f'{ctx.author.id}']["custom_role"] == False:
                    line = ctx.guild.get_role(753989478464487505)

                    role = await ctx.guild.create_role(reason="連續簽到3天獎勵", name=name, colour=color)
                    positions = {role: line.position-1}
                    await ctx.guild.edit_role_positions(reason="連續簽到3天獎勵", positions=positions)
                    bcdata[f'{ctx.author.id}']["custom_role"] = role.id
                    with open('members.json', 'w', encoding='utf8') as bcfile:
                        json.dump(bcdata, bcfile, indent=4)

                    await ctx.author.add_roles(role, reason="連續簽到3天獎勵")
                    await ctx.send(f'{ctx.author.mention} 申請自訂身分組成功')
                elif bcdata[f'{ctx.author.id}']["custom_role"]:
                    role = ctx.guild.get_role(bcdata[f'{ctx.author.id}']["custom_role"])

                    await role.edit(reson="連續簽到3天獎勵", name=name, colour=color)
                    await ctx.author.add_roles(role, reason="連續簽到3天獎勵")
                    await ctx.send(f'{ctx.author.mention} 更新自訂身分組成功')
            else:
                await ctx.send(f'{ctx.author.mention} 你沒有達到申請資格!')
        else:
            await ctx.send(f'{ctx.author.mention} 你沒有達到申請資格!')

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
    
    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def voicemoveall(self, ctx, origin: discord.VoiceChannel, target: discord.VoiceChannel, reason="N/A"):
        """將全部人從一個頻道移到另外一個頻道。用法：/voicemoveall 原本頻道id 目標頻道id"""
        if ctx.author.guild_permissions.move_members == True:
            if origin in ctx.guild.voice_channels and target in ctx.guild.voice_channels:
                for members in origin.members:
                    await members.edit(voice_channel=target)
        res = f"把所有成員從 {origin.mention} 移動到 {target.mention} 成功"
        await ctx.send(res)

    #recation role
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        
        #reaction role 傳說
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:AOVicon:747125830186041345>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745851285621702687)#取得role資料
                channel = guild.get_channel(743316291296690216)#取得channel資料
                await payload.member.add_roles(role)#給予role
                await channel.send(f'【你踩到兔几的陷阱，掉進了新的區域】\n歡迎【{payload.member.mention}】來到了 {channel.mention} \n送上胡蘿蔔，以示友好☆')

        #reaction role minecraft
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:minecraft_grass:747125831297663057>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745851154700959906)#取得role資料
                channel = guild.get_channel(744791458216935495)#取得channel資料
                await payload.member.add_roles(role)#給予role
                await channel.send(f'【你踩到兔几的陷阱，掉進了新的區域】\n歡迎【{payload.member.mention}】來到了 {channel.mention} \n送上胡蘿蔔，以示友好☆')

        #reaction role pubg lite
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:pubgliteicon:747125830269927495>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745850928653008938)#取得role資料
                channel = guild.get_channel(744792180425621545)#取得channel資料
                await payload.member.add_roles(role)#給予role
                await channel.send(f'【你踩到兔几的陷阱，掉進了新的區域】\n歡迎【{payload.member.mention}】來到了 {channel.mention} \n送上胡蘿蔔，以示友好☆')

        #reaction role osu
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:OsuLogo:747128004974477382>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745859173048385561)#取得role資料
                channel = guild.get_channel(745858655005442118)#取得channel資料
                await payload.member.add_roles(role)#給予role
                await channel.send(f'【你踩到兔几的陷阱，掉進了新的區域】\n歡迎【{payload.member.mention}】來到了 {channel.mention} \n送上胡蘿蔔，以示友好☆')
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        
        #移除reaction role 傳說
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:AOVicon:747125830186041345>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745851285621702687)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role

        #移除reaction role minecraft
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:minecraft_grass:747125831297663057>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745851154700959906)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role

        #移除reaction role pubg lite
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:pubgliteicon:747125830269927495>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745850928653008938)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role

        #移除reaction role osu
        if payload.message_id == 746320857516998816:
            if str(payload.emoji) == '<:OsuLogo:747128004974477382>':
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(745859173048385561)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
        
def setup(bot):
    bot.add_cog(Admin(bot))