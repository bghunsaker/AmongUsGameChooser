# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext import commands
import random
import math

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


intents = discord.Intents.default()
intents.members = True 
client = discord.Client(intents=intents)

game_titles = ['Cyan Game','Red Game','Green Game','Purple Game','Yellow Game']

@client.event
async def on_ready():
    # in case this bot is part of multiple guilds
    for guild in client.guilds:
        if guild.name == GUILD:
            break
                 
    #print(
    #    f'{client.user} is connected to the following guild:\n'
    #    f'{guild.name}'
    #)
   
    # get members in General voice channel
    for voice_channel in guild.voice_channels:
        if(voice_channel.name == 'General'):
            members = voice_channel.members
            break
        
    random.shuffle(members)
    team_one = []
    team_two = []
    
    # make teams
    i = 0
    while i  < (len(members) - 1):
        team_one.append(members[i])
        team_two.append(members[i + 1])
        i += 2
        
    # get text channel
    for text_channel in guild.text_channels:
        if (text_channel.name == 'general'):
            break    
    
    random.shuffle(game_titles)
    await create_game(guild, game_titles[0], team_one, text_channel, voice_channel.category)
    await create_game(guild, game_titles[1], team_two, text_channel, voice_channel.category)
          

async def create_game(guild, game_title, team_list, text_channel, category):
    #print('\n' + game_title)
    await text_channel.send('**' + game_title + '**:')
    await guild.create_voice_channel(game_title, category = category, overwrites = None)
    for member in team_list:    
        #print(member.display_name)
        await text_channel.send(member.display_name)
                 
            
client.run(TOKEN)