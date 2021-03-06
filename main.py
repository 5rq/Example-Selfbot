import discord, json
from discord.ext import commands

with open('config.json') as c:
    config = json.load(c)

token = config.get('token')
prefix = config.get('prefix')

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print(f'Running as {bot.user.name}#{bot.user.discriminator}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

bot.run(token)
