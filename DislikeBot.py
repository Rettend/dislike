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

bot = commands.Bot(command_prefix='d-', description=None)
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
    if message.content.startswith('d-list'):
        em = discord.Embed(title="COMMANDS:", description=":closed_book: d-say (something)\n"
                           ":white_small_square: Repeat what you said\n"
                           "\n"
                           ":closed_book: d-joined (user)\n"
                           ":white_small_square: Show when joined the user in UTC\n"
                           "\n"
                           ":closed_book: d-game (game)\n"
                           ":white_small_square: r: Set a game for the Bot\n"
                           "\n"
                           ":closed_book: d-list\n"
                           ":white_small_square: Show this message", colour=0x992d22)
        em.set_thumbnail(url="https://cdn.discordapp.com/emojis/440044660036206593.png?v=1")
        em.set_footer(text="The Official Bot of Like Server, inviting and using the Bot in other servers breaks the Term of Use.", icon_url="https://cdn.discordapp.com/emojis/440044660036206593.png?v=1")
        await bot.send_message(message.channel, embed=em)
        
@bot.command()
async def game(play):
    await bot.change_presence(game=discord.Game(name=play))
    em = discord.Embed(title="Game-Status", description=f"Game-status changed to __{play}__!", colour=0x992d22)
    await bot.say(embed=em)

@bot.command()
async def joined(member):
    member = discord.Member = None
    if member is None:
        member = message.author
    await bot.say(f'**{member} joined at {member.joined_at}**')



token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
