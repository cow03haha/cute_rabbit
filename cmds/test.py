import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner

class Test(Cog_Extension):
    '''test only'''

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if type(error) in [discord.ext.commands.errors.CheckFailure, discord.ext.commands.errors.MissingPermissions]:
            await ctx.send("你的權限不足以使用此指令")
        else:
            await ctx.send(f'不明錯誤，如持續出現請聯絡 <@315414910689476609> 並提供以下資訊\n```{error}\n{type(error)}```')
    
    @commands.command()
    @commands.check(check_owner)
    async def test(self, ctx):
        '''for test'''
        await ctx.send("OOF")

def setup(bot):
    bot.add_cog(Test(bot))