import discord, os
from discord.ext import commands
from keepalive import keep_alive

token = os.getenv("token")
prefix = os.getenv("prefix")

bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    print(f'Running as {bot.user.name}#{bot.user.discriminator}')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

bot.run(token)
