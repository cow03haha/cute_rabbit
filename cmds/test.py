import json
import random

from discord.ext import commands

from bot import check_owner
from cores.classes import Cog_Extension


class Test(Cog_Extension):
    """test only"""

    @commands.command()
    @commands.check(check_owner)
    async def rand_sqad(self, ctx, count: int, *, users):
        """隨機組隊"""
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

    @commands.command()
    @commands.check(check_owner)
    async def checkout(self, ctx):
        guild = self.bot.get_guild(743292989790748812)

        channel = self.bot.get_channel(743768856853479525)
        notice = await channel.send("結算中...")

        channel = self.bot.get_channel(753543338006806528)
        role = guild.get_role(743292989790748812)
        msg = await channel.send("結算中...")
        await channel.set_permissions(role, send_messages=False)

        with open('members.json', 'r', encoding='utf8') as bcfile:
            bcdata = json.load(bcfile)

        for i in bcdata["member_id"]:
            if not bcdata[f'{i}']["today"]:
                bcdata[f'{i}']["total"] = 0
                with open('members.json', 'w', encoding='utf8') as bcfile:
                    json.dump(bcdata, bcfile, indent=4)
            else:
                bcdata[f'{i}']["today"] = False
                with open('members.json', 'w', encoding='utf8') as bcfile:
                    json.dump(bcdata, bcfile, indent=4)

            if bcdata[f'{i}']["total"] < 3 and bcdata[f'{i}']["custom_role"] and not bcdata[f'{i}']["remain"]:
                member = guild.get_member(i)
                role = guild.get_role(bcdata[f'{i}']["custom_role"])
                await member.remove_roles(role)
            elif bcdata[f'{i}']["total"] >= 3 and bcdata[f'{i}']["custom_role"]:
                member = guild.get_member(i)
                role = guild.get_role(bcdata[f'{i}']["custom_role"])
                await member.add_roles(role)

            if bcdata[f'{i}']["total"] >= 14:
                bcdata[f'{i}']["remain"] = True
                with open('members.json', 'w', encoding='utf8') as bcfile:
                    json.dump(bcdata, bcfile, indent=4)

        await msg.delete()
        role = guild.get_role(743292989790748812)
        await channel.set_permissions(role, send_messages=None)

        await notice.edit(content="結算成功!", delete_after=60)


def setup(bot):
    bot.add_cog(Test(bot))
