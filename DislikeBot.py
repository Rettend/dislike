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
    if message.content.startswith('d-disable'):
        role = await bot.utils.get(server.roles, id=439868272347709440)
        await bot.add_roles(message.author, role)
        await bot.send_message(message.channel, "**NSFW is disabled for you! ;)**")
    elif message.content.startswith('d-enable'):
        await bot.remove_roles(message.author, role)
        await bot.send_message(message.channel, "**NSFW is enabled for you! ;)**")

@bot.command()
async def game(play):
    await bot.change_presence(game=discord.Game(name=play))
    em = discord.Embed(title="Game-Status", description=f"Game-status changed to __{play}__!", colour=0x992d22)
    await bot.say(embed=em)

@bot.command()
async def joined_at(member):
    member = discord.Member = None
    if member is None:
        member = message.author
    await bot.say(f'{member} joined at {member.joined_at}')



token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
