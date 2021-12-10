import discord
from discord.ext import commands


bot = commands.Bot(command_prefix = "luzi ")


@bot.event
async def on_ready():
    print ("Bot is online")
    print ("Logged in as " + bot.user.name)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def oi(ctx):
    await ctx.send("Prazer, Luzineria, agora cala a boca e enche a porra do meu tanque caralho")

with open ("files\helpMessage.txt", "r") as f:
    helpMessage = f.read()
@bot.command()
async def helpie(ctx):
    await ctx.send(helpMessage)

with open ("files\geraldoMessage.txt", "r") as f:
    geraldoMessage = f.read()
@bot.command()
async def ripgeraldo(ctx):
    await ctx.send(geraldoMessage)


bot.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.dYiDqb6Nnl1TK03OpnJ5LfBId8U')