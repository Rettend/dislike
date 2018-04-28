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
bot.process_commands(message)



@bot.command()
async def react(search: int = None):
    if search:
        async for message in bot.channel.history(limit=search):
            await bot.clear_reactions()
        await bot.send_message(message.channel, f":heavy_check_mark: **Cleaned the last {search} Messages**")






token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
