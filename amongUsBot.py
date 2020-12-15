import os
import random
import math
import discord
from dotenv import load_dotenv
from discord.ext import commands

# set token and guild values from .env file (needs to be in same directory as this script)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# configure some discord.py stuff
intents = discord.Intents.default()
intents.members = True 
bot = commands.Bot(command_prefix = '!', intents = intents)

game_titles = ['Cyan Game','Red Game','Green Game','Purple Game','Yellow Game']

@bot.command(name = 'makegames')
async def create_games_command(ctx):
    # get members in General voice channel and shuffle
    voice_channel  = discord.utils.get(ctx.guild.voice_channels, name = 'General')
    members = voice_channel.members        
    random.shuffle(members)
    
    # make teams
    team_one = []
    team_two = []
    for i in range(0, (len(members) - 1), 2):
        team_one.append(members[i])
        team_two.append(members[i + 1])

    random.shuffle(game_titles)
    await create_game(ctx.guild, game_titles[0], team_one, ctx.channel, voice_channel.category)
    await create_game(ctx.guild, game_titles[1], team_two, ctx.channel, voice_channel.category)  
                

async def create_game(guild, game_title, team_list, text_channel, vc_category):
    await text_channel.send('**' + game_title + '**:')
    await guild.create_voice_channel(game_title, category = vc_category, overwrites = None)
    for member in team_list:    
        await text_channel.send(member.display_name)

            
bot.run(TOKEN)