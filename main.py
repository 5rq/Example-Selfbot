import discord, json
from discord.ext import commands

with open('config.json') as c:
    config = json.load(c)

token = config.get('token')
prefix = config.get('prefix')
