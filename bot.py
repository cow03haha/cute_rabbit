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

@bot.event
async def on_member_join(self, member):
    #print(f'{member} 加入了牛牛神殿')
    channel = bot.get_channel(int(bcdata['join_channel']))
    await channel.send(f'{member} 加入了牛牛神殿')

@bot.event
async def on_member_remove(self, member):
    #print(f'{member} 離開了牛牛神殿')
    channel = bot.get_channel(int(bcdata['leave_channel']))
    await channel.send(f'{member} 離開了牛牛神殿')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

if __name__ == "__main__":
    bot.run(bcdata['token'])