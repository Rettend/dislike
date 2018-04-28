import discord
from discord.ext import commands
import asyncio
import time
import random
import aiohttp
import re
import datetime
import traceback
import os
import sys

description = "The Offical bot of Like-Server!"
bot = commands.Bot(command_prefix='d-', description=description)
message = discord.Message

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name='-Alpha version-'))

@bot.event
async def on_message(message):
    if message.content.startswith('d-say'):
        args = message.content.split(' ')
        await bot.send_message(message.channel, '**%s**' % (' '.join(args[1:])))
    await bot.process_commands(message)

@bot.command()
async def game(play):
    list = []
    list.append(play)
    await bot.change_presence(game=discord.Game(name=play))
    await bot.say(f"**Game-status changed to {play}!**")

@bot.command(pass_context=True)
async def joined_at(member: discord.Member = None):
    if member is None:
        member = message.author
    await bot.say('{0} joined at {0.joined_at}'.format(member))



token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
