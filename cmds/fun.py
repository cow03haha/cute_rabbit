import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata, imgs
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
        random_pic = random.choice(imgs)
        pic = discord.File(random_pic)#發送檔案的處理方式
        await ctx.send(file = pic)#用file來定要發送檔案
    
    @commands.Cog.listener()
    async def on_message(self, msg):
        if msg.content.endswith('牛牛') and msg.author != self.bot.user:
            await msg.channel.send(random.choice(bcdata['cow_msg']))
    
    @commands.command()
    async def 抽籤(self, ctx):
        '''試手氣。'''
        fortune = ['大吉', '吉', '小吉', '小凶', '凶', '大凶']
        pro = [2, 6, 4, 3, 2, 1]
        reply = ''.join(random.choices(fortune, weights=pro))
        await ctx.send(f'你抽到了 "{reply}"')
    
    @commands.command()
    async def 選擇(self, ctx, *, msg):
        '''選擇障礙專用。用法：/選擇 選項1 選項2 選項3...'''
        choice = random.choice(msg.split())
        await ctx.send(f'我選擇... {choice}!')

    @commands.has_role(612613325766787072)
    @commands.command()
    async def 內戰(self, ctx, str_time, end_time, *, description):
        '''傳說區內戰用。用法詳情請使用/hlep 內戰
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
    
    @commands.has_role(612613325766787072)
    @commands.command()
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
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.message_id == fight.id:
            if payload.user_id != self.bot.user.id:
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(742364064369475644)#取得role資料
                await payload.member.add_roles(role)#給予role
                await payload.member.send('報名內戰成功')
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        if payload.message_id == fight.id:
            if payload.user_id != self.bot.user.id:
                guild = self.bot.get_guild(payload.guild_id)#取得server id
                role = guild.get_role(742364064369475644)#取得role資料
                user = guild.get_member(payload.user_id)
                await user.remove_roles(role)#移除role
                await user.send('退出內戰成功')

def setup(bot):
    bot.add_cog(Fun(bot))