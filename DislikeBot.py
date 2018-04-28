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
import psutil
import random
import pip
import json
import io

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

class Information:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True)
    async def channels(self, ctx, serverid:int = None):

        if serverid is None:
            server = ctx.guild
        else:
            server = discord.utils.get(self.bot.guilds, id=serverid)
            if server is None:
                return await ctx.send('Server not found!')

        e = discord.Embed()
        e.color = await ctx.get_dominant_color()

        voice = ''
        text = ''
        categories = ''

        for channel in server.voice_channels:
            voice += f'\U0001f508 {channel}\n'
        for channel in server.categories:
            categories += f'\U0001f4da {channel}\n'
        for channel in server.text_channels:
            text += f'\U0001f4dd {channel}\n'
        
        if len(server.text_channels) > 0:
            e.add_field(name='Text Channels', value=f'```{text}```')
        if len(server.categories) > 0:
            e.add_field(name='Categories', value=f'```{categories}```')
        if len(server.voice_channels) > 0:
            e.add_field(name='Voice Channels', value=f'```{voice}```')

        try:
            await ctx.send(embed=e)
        except discord.HTTPException:
            em_list = await embedtobox.etb(e)
            for page in em_list:
                await ctx.send(page)


    
    
        













token = os.environ.get('DISCORD_TOKEN')
bot.run(token)
