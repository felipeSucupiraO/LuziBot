import discord
from discord.ext import commands
import random


bot = commands.Bot(command_prefix = "luzi ")


@bot.event
async def on_ready():
    print ("Bot is online")
    print ("Logged in as " + bot.user.name)

#Comandos

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Latência: " + (str(round(bot.latency * 1000))) + "ms")

@bot.command()
async def oi(ctx):
    await ctx.send("Olá, prazer, Luzineria, agora cala a boca e trás a porra da gasolina caralho")

@bot.command()
async def helpie(ctx):
    helpmessage = open("files\helpMessage.txt", "r", encoding = "utf-8")
    await ctx.send(helpmessage.read())
    helpmessage.close()

@bot.command()
async def ripgeraldo(ctx):
    geraldomessage = open("files\geraldoMessage.txt", "r", encoding = "utf-8")
    await ctx.send(geraldomessage.read())
    geraldomessage.close()

@bot.command()
async def diga(ctx, *, message = None):
    if (message == None):
        await ctx.send("O que tu quer que eu fale porra?")
    else:
        await ctx.send(message)

@bot.command(aliases = ["8ball"])
async def bola8(ctx, *, question = None):
    responses = [
        "Com certeza!", 
        "Decididamente que sim.",
        "Sem dúvidas!",
        "Sim, definitivamente.", 
        "Você pode contar que sim.", 
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
    if (question == None):
        await ctx.send ("Faça o favor de colocar a pergunta pra eu responder gênio")
    else:
        await ctx.send ("Tu perguntou: \"" + question + "\"\n" + random.choice(responses))

@bot.command()
async def apagar(ctx, amount = 1):
    await ctx.channel.purge(limit = (amount + 1))

@bot.command(aliases = ["kick"])
async def expulsar(ctx, member:discord.Member, *, reason = None):
    if (reason == None):
        await member.kick()
    else:
        await member.kick(reason = reason)

@bot.command(aliases = ["ban"])
async def banir(ctx, member:discord.Member, *, reason = None):
    if (reason == None):
        await member.kick()
    else:
        await member.kick(reason = reason)

#Iniciação do bot

bot.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.dYiDqb6Nnl1TK03OpnJ5LfBId8U')