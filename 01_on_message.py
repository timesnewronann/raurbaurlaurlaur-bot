import discord

""""
client = discord.Client()

@client.event
async def on_ready():
    print('Online')

client.run('OTI2NjQxNDkxMTk0MDQwNDIw.Yc-oIw.7fgqsB6vccqTdhFt0De13wAAYro')
"""

client = discord.Client()  # connection to discord


@client.event
async def on_ready():  # triggered whenever bot is online and logged in
    print('Raurbaurlaurlaur is charged and online ╰(*°▽°*)╯')


@client.event
async def on_message(message):  # listens for any messages and sends that back

    if message.author == client.user:
        return

    if message.content == 'hi':
        await message.channel.send('*bobs head*')

    if message.content == 'robo':  # robot reaction
        await message.add_reaction('\U0001F916')



@client.event
async def on_message_edit(before, after):
    await before.channel.send(
        f'{before.author} edit a message.\n'
        f'Before: {before.content}\n'
        f'After: {after.content}'
    )


@client.event
async def on_reaction_add(reaction, user):
    await reaction.message.channel.send(f'{user} farted {reaction.emoji}')



client.run('OTI2NjQxNDkxMTk0MDQwNDIw.Yc-oIw.7fgqsB6vccqTdhFt0De13wAAYro')
