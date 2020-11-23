import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner
import asyncio
import os

class Test(Cog_Extension):
    '''test only'''
    
    @commands.command()
    @commands.check(check_owner)
    async def test(self, ctx, *, name):
        '''for test'''
        # Gets voice channel of message author
        songs = []
        for filename in os.listdir('./audio'):
            if filename.endswith('.webm'):
                songs.append(filename[:-5])
        
        vc = ctx.author.voice

        if vc != None:
            if name == "list":
                await ctx.send("\n".join(songs))
                return
            if name not in songs:
                await ctx.send("歌曲庫裡沒有這首歌")
                return
            
            vc_channel = await vc.channel.connect()
            vc_channel.play(discord.FFmpegPCMAudio(executable="C:\\Python\\Python37\\Scripts\\ffmpeg.exe", source=f'audio/{name}.webm'))
            # Sleep while audio is playing.
            while vc_channel.is_playing():
                await asyncio.sleep(0.1)
            await vc_channel.disconnect()
        else:
            await ctx.send(ctx.author.name + " is not in a channel.")

        # Delete command after the audio is done playing.
        #await ctx.message.delete()

def setup(bot):
    bot.add_cog(Test(bot))