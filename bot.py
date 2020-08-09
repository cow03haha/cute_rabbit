import discord
from discord.ext import commands
import json
import os

#導入json庫
with open('settings.json', 'r', encoding='utf8') as bcfile:
    bcdata = json.load(bcfile)

#代表bot本身
bot = commands.Bot(command_prefix='/')

#bot上線
@bot.event
async def on_ready():
    print("bot online!")

@bot.command()
async def load(ctx, extension):
    '''載入特定模組'''
    if ctx.author.id == 315414910689476609:
        bot.load_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} 模組載入完成')
    else:
        await ctx.send('只有牛牛能用這個指令')
@bot.command()
async def unload(ctx, extension):
    '''卸載特定抹組'''
    if ctx.author.id == 315414910689476609:
        bot.unload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} 模組卸載完成')
    else:
        await ctx.send('只有牛牛能用這個指令')
@bot.command()
async def reload(ctx, extension):
    '''重新載入特定模組'''
    if ctx.author.id == 315414910689476609:
        bot.reload_extension(f'cmds.{extension}')
        await ctx.send(f'{extension} 模組重新載入完成')
    else:
        await ctx.send('只有牛牛能用這個指令')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(bcdata['token'])