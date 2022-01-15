import asyncio
import discord
from discord.ext import commands
import random
from pathlib import Path

root_path = Path(__file__).resolve().parent

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
    helpmessage = open(root_path / "files" / "helpMessage.txt", "r", encoding = "utf-8")
    await ctx.send(helpmessage.read())
    helpmessage.close()

@bot.command()
async def ripgeraldo(ctx):
    geraldomessage = open(root_path / "files" / "geraldoMessage.txt", "r", encoding = "utf-8")
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
    if (question != None):
        await ctx.send ("Tu perguntou: \"" + question + "\"\n" + "Deixa eu pensar...")  
        await ctx.trigger_typing()
        await asyncio.sleep(5)
        await ctx.send (random.choice(responses))
    else:
        await ctx.send ("Faça o favor de colocar a pergunta pra eu responder gênio")

@bot.command()
async def voto(ctx, *, situation):
    
    await ctx.send(situation + "\nO conselho tem 3 minutos para decidir.")
    firstMessage = ctx.channel.last_message
    await firstMessage.add_reaction("<:pyes:700337751597383691>")
    await firstMessage.add_reaction("<:pno:700337705510502512>")
    await asyncio.sleep(180)

    yesCount = 0
    noCount = 0
    for i in firstMessage.reactions:
        if (i.emoji.name == "pyes"):
            yesCount = i.count
        elif (i.emoji.name == "pno"):
            noCount = i.count
    if (yesCount > noCount):
        await ctx.send ("\"" + situation + "\"\nO conselho decidiu que sim.")
    elif (noCount > yesCount):
        await ctx.send ("\"" + situation + "\"\nO conselho decidiu que não.")
    else:
        await ctx.send ("\"" + situation + "\"\nO conselho não consegui tomar uma decisão.")

@bot.command()
async def teste (ctx):
    await ctx.send ("teste1")
    await ctx.send ("teste2")

#@bot.command()
#async def apagar(ctx, amount = 0):
#    canDelete = None
#    for permission in ctx.author.permissions_in(ctx):
#        if (permission.manage_messages == True):
#            canDelete = True
#
#    if (canDelete == True):
#        if (amount > 10):
#            amount = 10
#        await ctx.channel.purge(limit = (amount + 1))
#    else:
#        await ctx.send("Você não pode apagar mensagens seu plebeu")
#
#@bot.command(aliases = ["kick"])
#async def expulsar(ctx, member:discord.Member, *, reason = None):
#    for i in ctx.author.roles:
#        if ((i.id == 449251888592977932) or (i.id == 744997848155816086) or (i.id == 840028423681343488)):
#            éOMarvado = True
#        else:
#            éOMarvado = False
#This for will see if the author has any of the roles needed to normally ban people, than giving him access to this command if this is the case
#
#    if (éOMarvado == True):
#        if (reason == None):
#            await member.kick()
#        else:
#            await member.kick(reason = reason)
#    else:
#        await ctx.send ("Tu não é o MARVADO, tu não pode expulsar ninguém.")
#
#@bot.command(aliases = ["ban"])
#async def banir(ctx, member:discord.Member, *, reason = None):
#    for i in ctx.author.roles:
#        if ((i.id == 449251888592977932) or (i.id == 744997848155816086) or (i.id == 840028423681343488)):
#            éOMarvado = True
#        else:
#            éOMarvado = False
#This for will see if the author has any of the roles needed to normally ban people, than giving him access to this command if this is the case
#
#    if (éOMarvado == True):
#        if (reason == None):
#            await member.ban()
#        else:
#            await member.ban(reason = reason)
#    else:
#        await ctx.send ("Tu não é o MARVADO, tu não pode expulsar ninguém.")

#Iniciação do bot

bot.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.dYiDqb6Nnl1TK03OpnJ5LfBId8U')
