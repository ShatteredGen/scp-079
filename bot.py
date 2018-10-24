import discord
from discord.ext import commands

TOKEN = 'NTA0Njc0MDg4MjA0MTA3Nzc2.DrIeJg.wprKwWYBroD1c5FX4641biLVVsc'

client = commands.Bot (command_prefix = '')

@client.event
async def on_ready() :
    print('SCP - 079 has awoken')



@client.command()
async def ping():
    await client.say('Pong')
    await client.process_commands(message)


@client.command()
async def echo(*args) :
    output = ''
    for word in args:
        output += word
        output += ' '

    await client.say(output)


client.run(TOKEN)
