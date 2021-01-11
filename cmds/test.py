import discord
from discord.ext import commands
from cores.classes import Cog_Extension
from bot import check_owner
import json
import asyncio
import os
import random


class Test(Cog_Extension):
    '''test only'''

    @commands.command()
    @commands.check(check_owner)
    async def rand_sqad(self, ctx, count: int, *, users):
        '''for test'''
        users = users.split()
        team = ""

        for i in range(int(len(users)/count)):
            team += "第" + str(i+1) + "小隊:"

            for _ in range(count):
                rand = random.choice(users)
                team += "   " + rand
                users.remove(rand)

            team += "\n\n"

        if users:
            team += "剩餘玩家:"
            for i in users:
                team += "   " + i
        await ctx.send(team)


def setup(bot):
    bot.add_cog(Test(bot))
