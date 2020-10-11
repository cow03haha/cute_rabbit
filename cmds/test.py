import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner

class Test(Cog_Extension):
    '''test only'''
    
    @commands.command()
    @commands.check(check_owner)
    async def test(self, ctx):
        '''for test'''
        if 0:
            await ctx.send("1")
def setup(bot):
    bot.add_cog(Test(bot))