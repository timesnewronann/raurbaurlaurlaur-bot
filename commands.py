import discord
from discord.ext import commands



roboLolo = commands.Bot(command_prefix='!')


@roboLolo.command(pass_context = True)
async def bonk(ctx):
    """

    !bonk

    """
    await ctx.send('Bonk! Go to horny jail', file = discord.File('bonk.jpg'))

@roboLolo.command()
async def hi(ctx):
    """
    ctx - context (information about how the command was executed)

    !hi

    """

    await ctx.send('Hiiiiii!', file = discord.File('roboLolo.jpg'))

@roboLolo.command()
async def sus(ctx):
    """
    !sus

    """

    await ctx.send('Fake laurlaur detected')

@roboLolo.command()
async def recharge(ctx):
    """

    !recharge

    """

    await ctx.send("I'm sleepy need to recharge.", file = discord.File('sleepyLolo.jpg'))


@roboLolo.command()
async def bark(ctx):

    await ctx.send('BARK BARK BARK WOOF WOOF!!')

@roboLolo.command()
async def abg(ctx):
    await ctx.send('Where is the bay area man', file = discord.File('abgLolo.jpg'))


@roboLolo.command()
async def olaf(ctx):
    await ctx.send(file = discord.File('olafLolo.jpg'))


@roboLolo.command()
async def nap(ctx):
    await ctx.send(file = discord.File('nappyLolo.jpg'))

@roboLolo.command()
async def minion(ctx):
    await ctx.send(file = discord.File('minionLolo.jpg'))




roboLolo.run('OTI2NjQxNDkxMTk0MDQwNDIw.Yc-oIw.7fgqsB6vccqTdhFt0De13wAAYro')


