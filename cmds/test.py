import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner
import asyncio

class Test(Cog_Extension):
    '''test only'''
    
    @commands.command()
    @commands.check(check_owner)
    async def test(self, ctx):
        '''for test'''
        # Gets voice channel of message author
        voice_channel = ctx.author.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="C:<path_to_file>"))
            # Sleep while audio is playing.
            while vc.is_playing():
                sleep(.1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")
        # Delete command after the audio is done playing.
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Test(bot))