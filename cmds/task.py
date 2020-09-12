import discord
from discord.ext import commands
from cores.classes import Cog_Extension
import asyncio
import json
import datetime

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        '''
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(741685158335479950)
            while not self.bot.is_closed():
                await self.channel.send('loop test')
                await asyncio.sleep(5)
            
        self.bg_task = self.bot.loop.create_task(interval())
        '''
        
        #self.counter = 0
        
        async def daily_check():
            await self.bot.wait_until_ready()

            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%H%M%S')

                if now_time == '000000':
                    with open('members.json', 'r', encoding='utf8') as bcfile:
                        bcdata = json.load(bcfile)

                    for i in bcdata["member_id"]:
                        if bcdata[f'{i}']["today"] != 1:
                            bcdata[f'{i}']["total"] = 0
                            bcdata[f'{i}']["today"] = 0
                            with open('members.json', 'w', encoding='utf8') as bcfile:
                                json.dump(bcdata, bcfile, indent=4)
                        else:
                            bcdata[f'{i}']["today"] = 0
                            with open('members.json', 'w', encoding='utf8') as bcfile:
                                json.dump(bcdata, bcfile, indent=4)
                        
                        if bcdata[f'{i}']["total"] < 3 and bcdata[f'{i}']["custom_role"] != False:
                            guild = self.bot.get_guild(743292989790748812)
                            member = guild.get_member(i)
                            role = guild.get_role(bcdata[f'{i}']["custom_role"])
                            await member.remove_roles(role)
                        elif bcdata[f'{i}']["total"] >= 3 and bcdata[f'{i}']["custom_role"] != False:
                            guild = self.bot.get_guild(743292989790748812)
                            member = guild.get_member(i)
                            role = guild.get_role(bcdata[f'{i}']["custom_role"])
                            await member.add_roles(role)


                    channel = self.bot.get_channel(743768856853479525)
                    await channel.send("每日結算成功")
                        
                    await asyncio.sleep(1)
                    self.bg_task = self.bot.loop.create_task(daily_check())
                else:
                    await asyncio.sleep(1)
                    pass

        self.bg_task = self.bot.loop.create_task(daily_check())
        

        '''
        async def fight_task():
            await self.bot.wait_until_ready()

            with open('settings.json', 'r', encoding='utf8') as bcfile:
                bcdata =json.load(bcfile)
            self.guild = self.bot.get_guild(int(bcdata['fight_guild']))
            self.channel = self.guild.get_channel(int(bcdata['fight_channel']))
            self.role = self.guild.get_role(743668426383294495)
            
            while not self.bot.is_closed():
                now_time = datetime.datetime.now().strftime('%m%d%H%M')
                
                with open('settings.json', 'r', encoding='utf8') as bcfile:
                    bcdata = json.load(bcfile)
                
                if now_time == bcdata['end_time'] and bcdata['fight_counter'] == '0':
                    now_time = datetime.datetime.now().strftime('%m-%d %H:%M')
                    await self.channel.send(f'內戰已於{now_time}截止報名')

                    with open('settings.json', 'r', encoding='utf8') as bcfile:
                        bcdata =json.load(bcfile)
                    bcdata['fight_counter'] = '1'
                    bcdata['fight_process'] = '0'
                    bcdata['end_time'] = '0'
                    with open('settings.json', 'w', encoding='utf8') as bcfile:
                        json.dump(bcdata, bcfile, indent=4)

                    await self.channel.send('開始隨機分組...')

                    with open('settings.json', 'r', encoding='utf8') as bcfile:
                        bcdata =json.load(bcfile)
                    users = self.role.members
                    bcdata['fight_users'] = str(users.id)
                    with open('settings.json', 'w', encoding='utf8') as bcfile:
                        json.dump(bcdata, bcfile, indent=4)

                    await asyncio.sleep(1)
                else:
                    await asyncio.sleep(1)
                    pass

            self.bg_task = self.bot.loop.create_task(fight_task())
        '''

    '''
    @commands.command()
    async def set_channel(self, ctx, ch: int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f'{self.channel.mention} 的排程設定成功')
    
    @commands.command()
    async def set_time(self,ctx ,time):
        self.counter = 0
 
        with open('settings.json', 'r', encoding='utf8') as bcfile:
            bcdata =json.load(bcfile)

        bcdata['task_time'] = time

        with open('settings.json', 'w', encoding='utf8') as bcfile:
            json.dump(bcdata, bcfile, indent=4)
    '''

def setup(bot):
    bot.add_cog(Task(bot))