import discord

""""
client = discord.Client()

@client.event
async def on_ready():
    print('Raurbaurlaurlaur is charged and online ╰(*°▽°*)╯')

client.run('OTI2NjQxNDkxMTk0MDQwNDIw.Yc-oIw.7fgqsB6vccqTdhFt0De13wAAYro')
"""

# custom bot without decorators
class MyClient(discord.client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # reference to parent class

    async def on_ready(self):
        print('Raurbaurlaurlaur is charged and online ╰(*°▽°*)╯')


intents = discord.Intents.default()

client = MyClient()

client.run('OTI2NjQxNDkxMTk0MDQwNDIw.Yc-oIw.7fgqsB6vccqTdhFt0De13wAAYro')
