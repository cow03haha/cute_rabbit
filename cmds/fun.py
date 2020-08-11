import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata, imgs
import random
import os
import datetime
import pytz 

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
    async def 內戰(self, ctx, str_time, end_time):
        '''傳說區內戰用'''
        #<@&670280115556712458>
        tw = pytz.timezone('Asia/Taipei')
        embed=discord.Embed(title="內戰調查", description="增加任意表情來報名參加", colour=ctx.author.colour, timestamp=datetime.datetime.now(tz=tw))
        embed.set_author(name=ctx.author, icon_url=str(ctx.author.avatar_url))
        embed.add_field(name="內戰開始時間:", value=str_time, inline=True)
        embed.add_field(name="報名截止時間:", value=end_time, inline=True)
        global fight
        fight = await ctx.send(embed=embed)
        await fight.add_reaction('✅')
    
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