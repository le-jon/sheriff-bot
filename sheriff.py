# bot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_SERV')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to PoliSigh')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome {member.name} to the Political Revolution.'
    )

# CLIENT EVENT TO LIST ALL MEMBERS IN SERVER
# @client.event
# async def on_ready():
#    for guild in client.guilds:
#        if guild.name == GUILD:
#            break
#    print(
#        f'{client.user} is connected to the following server:\n'
#        f'{guild.name}(id: {guild.id})'
#    )

#    members = '\n - '.join([member.name for member in guild.members])
#    print(f'Guild Members:\n - {members}')

client.run(TOKEN)