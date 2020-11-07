import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner
import random
import os
import datetime
import pytz
import json

class Fun(Cog_Extension):
    '''娛樂指令'''
    #發送本地圖片(如果想發送網路圖片，直接send網址就好)
    #發送隨機圖片(使用random.choice)
    @commands.command()
    async def meme(self, ctx):
        '''隨機梗圖。'''
        #導入梗圖路徑(list)
        dn = os.path.dirname('..')
        dn = os.path.join(dn, 'meme')
        imgs = os.listdir(dn)
        imgs = [os.path.join(dn, path) for path in imgs]

        random_pic = random.choice(imgs)
        pic = discord.File(random_pic)#發送檔案的處理方式
        await ctx.send(file = pic)#用file來定要發送檔案
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.author.bot:
            return

        if msg.content == f'<@!{self.bot.user.id}>':
            with open('settings.json', 'r', encoding='utf8') as bcfile:
                bcdata =json.load(bcfile)
                
            await msg.channel.send(random.choice(bcdata['cow_msg']))
        
        if msg.content in ["oof", "OOF"]:
            await msg.channel.send(msg.content)
        
        if "egg" in msg.content:
            await msg.add_reaction("🥚")

        if "A" in msg.content:
            await msg.add_reaction("🇦")
    
    @commands.command(aliases=['抽'])
    async def 抽籤(self, ctx):
        '''試手氣。'''
        fortune = ['大吉', '吉', '小吉', '小凶', '凶', '大凶']
        pro = [2, 6, 4, 3, 2, 1]
        reply = ''.join(random.choices(fortune, weights=pro))
        await ctx.send(f'你抽到了 "{reply}"')
    
    @commands.command(aliases=['選擇'])
    async def choice(self, ctx, *, msg):
        '''選擇障礙專用。用法：/選擇 選項1 選項2 選項3...'''
        choice = random.choice(msg.split())
        await ctx.send(f'我選擇... {choice}!')

    @commands.command(aliases=['list'])
    @commands.check(check_owner)
    async def reminder(self, ctx, target, method, *args):
        '''個人備忘錄。用法：/list 對象 動作 (事項/時間)
        可選的動作有：add(增加代辦事項)、remove(移除代辦事項)、check(檢查代辦事項)
        範例：/list check(檢查有哪些代辦事項)
            /list add 吃早餐  約會(增加代辦事項吃早餐)跟約會'''
        with open('members.json', 'r', encoding='utf8') as bcfile:
            bcdata = json.load(bcfile)
        if target in ["matter", "事項"]:
            if method == "check":
                if bcdata[f'{ctx.author.id}']["remind_list"]:
                    cow = self.bot.get_user(315414910689476609)
                    tw = pytz.timezone('Asia/Taipei')
                    k = 0
                    embed = discord.Embed(title="代辦事項", color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
                    embed.set_author(name=cow.name, icon_url=str(cow.avatar_url))
                    embed.set_thumbnail(url=str(self.bot.user.avatar_url))

                    for i in bcdata[f'{ctx.author.id}']["remind_list"]:
                        k += 1
                        embed.add_field(name=f'事項{k}', value=i, inline=True)

                    await ctx.author.send(embed=embed)
                else:
                    await ctx.author.send("沒有代辦事項")
            elif method == "add":
                if args:
                    for i in args:
                        if i in bcdata[f'{ctx.author.id}']["remind_list"]:
                            await ctx.author.send(f'事項 `{i}` 已經存在了')
                            return

                        bcdata[f'{ctx.author.id}']["remind_list"].append(i)

                    with open('members.json', 'w', encoding='utf8') as bcfile:
                        json.dump(bcdata, bcfile, indent=4)

                    item = " ".join(args)
                    await ctx.author.send(f'新增 `{item}` 事項成功')
                else:
                    await ctx.author.send("你沒有指定要增加的代辦事項")
            elif method == "remove":
                for i in args:
                    if i not in bcdata[f'{ctx.author.id}']["remind_list"]:
                        await ctx.author.send(f'你的事項中沒有 `{i}` 這個事項')
                        return
                        
                    bcdata[f'{ctx.author.id}']["remind_list"].remove(i)


                with open('members.json', 'w', encoding='utf8') as bcfile:
                    json.dump(bcdata, bcfile, indent=4)

                item = " ".join(args)
                await ctx.author.send(f'移除事項 `{item}` 成功')
            else:
                await ctx.author.send("錯誤的動作選項")
        elif target in ["time", "時間"]:
            if method == "check":
                if bcdata[f'{ctx.author.id}']["remind_time"]:
                    cow = self.bot.get_user(315414910689476609)
                    tw = pytz.timezone('Asia/Taipei')
                    k = 0
                    embed = discord.Embed(title="提醒時間", color=0xf5ed00, timestamp=datetime.datetime.now(tz=tw))
                    embed.set_author(name=cow.name, icon_url=str(cow.avatar_url))
                    embed.set_thumbnail(url=str(self.bot.user.avatar_url))

                    for i in bcdata[f'{ctx.author.id}']["remind_time"]:
                        k += 1
                        embed.add_field(name=f'時間{k}', value=i, inline=True)

                    await ctx.author.send(embed=embed)
                else:
                    await ctx.author.send("沒有設定提醒時間")
            elif method == "add":
                if args:
                    for i in args:
                        if i in bcdata[f'{ctx.author.id}']["remind_time"]:
                            await ctx.author.send(f'提醒時間 `{i}` 已經存在了')
                            return

                        if len(i) > 6:
                            await ctx.author.send("錯誤的時間格式")
                            return

                        bcdata[f'{ctx.author.id}']["remind_time"].append(i)
                        bcdata["remind_time"].append(i)

                    with open('members.json', 'w', encoding='utf8') as bcfile:
                        json.dump(bcdata, bcfile, indent=4)

                    item = " ".join(args)
                    await ctx.author.send(f'新增提醒時間 `{item}` 成功')
                else:
                    await ctx.author.send("你沒有指定要增加的提醒時間")
            elif method == "remove":
                for i in args:
                    if i not in bcdata[f'{ctx.author.id}']["remind_time"]:
                        await ctx.author.send(f'你的提醒時間中沒有 `{i}` 這個時間')
                        return
                        
                    bcdata[f'{ctx.author.id}']["remind_time"].remove(i)
                    bcdata["remind_time"].remove(i)


                with open('members.json', 'w', encoding='utf8') as bcfile:
                    json.dump(bcdata, bcfile, indent=4)

                item = " ".join(args)
                await ctx.author.send(f'移除提醒時間 `{item}` 成功')
            else:
                await ctx.author.send("錯誤的動作選項")
        else:
            await ctx.author.send("錯誤的對象")
            
    @commands.command()
    @commands.check(check_owner)
    async def 內戰(self, ctx, str_time, end_time, *, description):
        '''傳說區內戰用。用法詳情請使用/help 內戰
        用法：/內戰 開始時間 報名截止時間 備註
        ex. /內戰 08301800 08301730 無
        表示內戰將於8月30號18點開始，於8月30號17點30分截止報名'''
        if len(str_time) != 8 or len(end_time) != 8:
            await ctx.send('請輸入正確的時間格式')
            return

        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        if bcdata['fight_process'] == '1':
            await ctx.send('一次只能舉辦一個內戰')
            return

        bcdata['fight_counter'] = '0'
        with open('settings.json', 'w', encoding='utf8') as bcfile:
            json.dump(bcdata, bcfile, indent=4)
        
        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        bcdata['fight_process'] = '1'
        with open('settings.json', 'w', encoding='utf8') as bcfile:
            json.dump(bcdata, bcfile, indent=4)

        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        bcdata['str_time'] = str_time
        with open('settings.json', 'w', encoding='utf8') as bcfile:
            json.dump(bcdata, bcfile, indent=4)
        
        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        bcdata['end_time'] = end_time
        with open('settings.json', 'w', encoding='utf8') as bcfile:
            json.dump(bcdata, bcfile, indent=4)

        tw = pytz.timezone('Asia/Taipei')
        embed=discord.Embed(title="內戰調查", description="在這則訊息增加任意表情符號來報名參加", colour=ctx.author.colour, timestamp=datetime.datetime.now(tz=tw))
        embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
        
        m = str_time[:2]
        d = str_time[2:4]
        H = str_time[4:6]
        M = str_time[6:]
        embed.add_field(name="內戰開始時間:", value=f'{m}-{d} {H}:{M}', inline=True)
        
        m = end_time[:2]
        d = end_time[2:4]
        H = end_time[4:6]
        M = end_time[6:]
        embed.add_field(name="報名截止時間:", value=f'{m}-{d} {H}:{M}', inline=True)
        
        embed.add_field(name="備註:", value=description, inline=False)
        global fight
        fight = await ctx.send(embed=embed)
        await fight.add_reaction('✅')
    
    @commands.command()
    @commands.check(check_owner)
    async def 取消內戰(self, ctx):
        '''取消內戰(限管理員使用)'''
        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        if bcdata['fight_process'] == "0":
            await ctx.send('沒有正在舉辦中的內戰')
            return

        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)
        bcdata['fight_process'] = '0'
        bcdata['str_time'] = '0'
        bcdata['end_time'] = '0'
        with open('settings.json', 'w', encoding='utf8') as bcfile:
            json.dump(bcdata, bcfile, indent=4)
        
        await fight.delete()
        await ctx.send('內戰取消成功')
    '''
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == fight.id:
            if payload.user_id != self.bot.user.id:
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(743668426383294495)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send('報名內戰成功')
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == fight.id:
            if payload.user_id != self.bot.user.id:
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(743668426383294495)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send('退出內戰成功')
    '''

    @commands.check(check_owner)
    @commands.command(aliases=["vcconnect", "vcjoin"])
    async def voiceconnect(self, ctx, target: discord.VoiceChannel):
        '''連接到特定頻道'''
        
        global vClient
        vClient = await target.connect(reconnect=True)
    
    @commands.check(check_owner)
    @commands.command(aliases=["vcdisconnect", "vcleave"])
    async def voicedisconnect(self, ctx):
        '''從特定頻道斷線'''

        await vClient.disconnect()
        
def setup(bot):
    bot.add_cog(Fun(bot))