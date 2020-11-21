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
        voice_channel = ctx.author.voice.channel

        if voice_channel != None:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio(executable="C:\\Python\\Python37\\Scripts\\ffmpeg.exe", source="audio/fbi open up.webm"))
            # Sleep while audio is playing.
            while vc.is_playing():
                await asyncio.sleep(0.1)
            await vc.disconnect()
        else:
            await ctx.send(str(ctx.author.name) + "is not in a channel.")

        # Delete command after the audio is done playing.
        #await ctx.message.delete()

def setup(bot):
    bot.add_cog(Test(bot))