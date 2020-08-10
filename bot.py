import discord
from discord.ext import commands
import json
import os

#導入json庫
with open('settings.json', 'r', encoding='utf8') as bcfile:
    bcdata = json.load(bcfile)

#代表bot本身
bot = commands.Bot(command_prefix='.')

#導入梗圖(list)
dn = os.path.dirname(__file__)
dn = os.path.join(dn, 'meme')
imgs = os.listdir(dn)
imgs = [os.path.join(dn, path) for path in imgs]

#bot上線
@bot.event
async def on_ready():
    print("bot online!")

#檢查所有者
def check_owner(ctx):
    return ctx.message.author.id == 315414910689476609

@commands.check(check_owner)
@bot.command()
async def load(ctx, extension):
    '''載入特定模組'''
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} 模組載入完成')

@commands.check(check_owner)
@bot.command()
async def unload(ctx, extension):
    '''卸載特定模組'''
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} 模組卸載完成')

@commands.check(check_owner)
@bot.command()
async def reload(ctx, extension):
    '''重新載入特定模組'''
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'{extension} 模組重新載入完成')

@commands.check(check_owner)
@bot.command()
async def poweroff(ctx):
    '''關閉bot'''
    await ctx.send('bot關閉中...')
    exit()

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(bcdata['token'])