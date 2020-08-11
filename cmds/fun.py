import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import bcdata, imgs
import random
import os

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

def setup(bot):
    bot.add_cog(Fun(bot))