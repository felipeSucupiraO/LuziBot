from asyncio.windows_events import NULL
import discord
from discord.ext import commands
import random


bot = commands.Bot(command_prefix = "luzi ")


@bot.event
async def on_ready():
    print ("Bot is online")
    print ("Logged in as " + bot.user.name)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Latência: " + (str(round(bot.latency * 1000))) + "ms")

@bot.command()
async def oi(ctx):
    await ctx.send("Prazer, Luzineria, agora cala a boca e enche a porra do meu tanque caralho")

@bot.command()
async def helpie(ctx):
    with open ("files\helpMessage.txt", "r") as f:
        helpMessage = f.read()
    await ctx.send(helpMessage)

@bot.command()
async def ripgeraldo(ctx):
    with open ("files\geraldoMessage.txt", "r") as f:
        geraldoMessage = f.read()
    await ctx.send(geraldoMessage)

@bot.command()
async def diga (ctx, *, message):
    await ctx.send(message)


@bot.command(aliases = ["8ball"])
async def bola8 (ctx, *, question):
    responses = [
        "Com certeza!", 
        "Já foi decidido que sim.",
        "Sem dúvidas!",
        "Sim, definitivamente.", 
        "Você pode contar com isso.", 
        "Pelo que eu vejo, sim.", 
        "Ao que tudo indica, sim.", 
        "Parece que sim.", 
        "Sim", 
        "Os sinais dizem que sim.", 
        "Está muito vago para dizer. Tente novamente.", 
        "Pergunte novamente mais tarde.", 
        "É melhor não te dizer agora.", 
        "Não consigo prever agora.", 
        "Se concentre e pergunte novamente.", 
        "Não conte com isso.", 
        "Minha resposta é não.", 
        "Minhas fontes dizem que não.", 
        "Parece que não.", 
        "Aparentemente não."]
    await ctx.send (random.choice(responses))

bot.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.dYiDqb6Nnl1TK03OpnJ5LfBId8U')