import os
import random
from urllib import response
import discord
from discord.ext import commands
from dotenv import load_dotenv

# 1


load_dotenv()
# imports os, discord and .env
secret = os.getenv('auth')
TOKEN = secret

# fetches the token from the .env

# 2
bot = commands.Bot(command_prefix='-')
# bot prefix
@bot.event
async def on_ready():
    # this is executed when the bot is ready to run
    print(f'{bot.user.name} has connected to Discord!')



@bot.command(name='ping') #ping pong
async def pong(ctx):
    response = "Pong"
    await ctx.send(response)

bot.run(TOKEN)
# runs the bot with the token