import os
from discord.ext import commands

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = "Mathmat#9030"  # Change to your discord id!!!

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

@bot.command()
async def name(ctx):
    await ctx.send(ctx.author)



token = "ODkyODIzNDQ0Njg3ODQ3NDU0.YVSgoQ.hKJObQZt3VvUOkNT9y9nluCwIGs"
bot.run(token)  # Starts the bot