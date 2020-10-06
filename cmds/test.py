import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner

class Test(Cog_Extension):
    '''test only'''
    
    @commands.command()
    @commands.check(check_owner)
    async def test(self, ctx, user: discord.User="me"):
        '''for test'''
        if user == "me":
            await ctx.send(ctx.message.author.avatar_url)
        else:
            await ctx.send(user.avatar_url)

def setup(bot):
    bot.add_cog(Test(bot))