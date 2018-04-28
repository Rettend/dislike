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
import logging

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

log = logging.getLogger('LOG')
class Moderation:

    def __init__(self, bot):
        self.bot = bot

    @bot.command(aliases=['Reactions'])
    async def reactions(self, ctx, search: int = None):
        if search:
            async for message in ctx.message.channel.history(limit=search):
                await message.clear_reactions()
            await edit(ctx, content=f"\N{HEAVY CHECK MARK} Cleaned the last {search} Messages", ttl=5)
        else:
            await edit(ctx, content="\N{HEAVY EXCLAMATION MARK SYMBOL} Don't forget to give the amount you wanna delte", ttl=5)
                
def setup(bot):
    bot.add_cog(Moderation(bot))





token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
