import discord
import asyncio
import os
import glob
import random
from discord.ext import commands
#from dotenv import load_dotenv

# from discord_slash import SlashCommand

client = commands.Bot(command_prefix=';;')


@client.event
async def on_ready():
    print('Bot is ready')


@client.command()
async def ping(ctx):
    await ctx.send(f' Pong!{round(client.latency * 1000)}ms')


@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    responses = ['It is certain', 'its is deciely so', 'without a doubt',
                 'yes',
                 'you may rely on it',
                 'as i see it, yes',
                 'most likely',
                 'outlook good',
                 'yes',
                 'signs point to yes',
                 'repl hazy try again',
                 'ask again later',
                 'better not tell you now',
                 'cannot predict now',
                 'concerntrate and ask again',
                 'dont cout oon it',
                 'my reply is no',
                 'my soucrs say no',
                 'outlook not so good',
                 'very doubtful']
    await ctx.send(f'Question:{question}\nAnswer:{random.choice(responses)}')


@client.command()
async def Pet(ctx, *, question):
    responses = [' Why yes she is his pet. He is a cutie and he can do anything he wants to to her. <3']
    await ctx.send(f'Answer:{random.choice(responses)}')


@client.command()
async def love(ctx):
    percentage = (random.randint(0, 100))
    await ctx.send(f'Uwu I love my master {percentage} %  of the time <3!')


@client.command(aliases=['cowgirl', 'cow', 'kinky'])
async def _cowgif(ctx):
    await ctx.send("")


async def background_loop():
    await client.wait_until_ready()
    while not client.is_closed():
        channel = await client.get_channel(713867808907198494)
        messages = ["Hello!", "How are you doing?", "Howdy!"]
        await channel.send(random.choice(messages))
        print("ran")
        await asyncio.sleep(5)


# @client.event
# async def on_message(message):
#  lst = ['mad','angry','sad','salty','lolhemad']
#  channe_id = client.get_channel(713867808907198494)
# if message.content.startswith('!') :
#   await channe_id.send(random.choice(lst))"""

client.run('')










