import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print("bot online!")

@bot.event
async def on_member_join(member):
#    print(f'{member} 加入了牛牛神殿')
    channel = bot.get_channel(620192290547433492)
    await channel.send(f'{member} 加入了牛牛神殿')
@bot.event
async def on_member_remove(member):
#    print(f'{member} 離開了牛牛神殿')
    channel = bot.get_channel(620192290547433492)
    await channel.send(f'{member} 離開了牛牛神殿')

bot.run('NjIwMTc2NTg1Mzk1NDA0ODMw.XXS-dA.dnIgi6ZeO7zwWo5Dcc6c4CBDU6s')