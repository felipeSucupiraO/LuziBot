import asyncio
import discord
from discord.ext import commands
import random
from pathlib import Path

root_path = Path(__file__).resolve().parent

client = commands.Bot(command_prefix = "luzi ")


#Events

@client.event
async def on_ready():
    print ("Bot is online")
    print ("Logged in as {}".format(client.user.name))

@client.event
async def on_error():
    client.send("Deu ruim")


#Commands

@client.command()
async def ping(ctx):
    await ctx.send("Pong! Latência: {} ms".format(str(round(client.latency * 1000))))

@client.command()
async def oi(ctx):
    await ctx.send("Olá, prazer, Luzineria, agora cala a boca e trás a porra da gasolina caralho")

@client.command()
async def helpie(ctx, category = None):
    if(category == "config"):
        configHelpMessage = open(root_path / "files" / "configHelpMessage.txt", "r", encoding = "utf-8")
        await ctx.send(configHelpMessage.read())
        configHelpMessage.close()
    elif (category == None):
        helpmessage = open(root_path / "files" / "helpMessage.txt", "r", encoding = "utf-8")
        await ctx.send(helpmessage.read())
        helpmessage.close()

@client.command()
async def ripgeraldo(ctx):
    geraldomessage = open(root_path / "files" / "geraldoMessage.txt", "r", encoding = "utf-8")
    await ctx.send(geraldomessage.read())
    geraldomessage.close()

@client.command()
async def diga(ctx, *, message = None):
    if (message == None):
        await ctx.send("O que tu quer que eu fale porra?")
        return
    
    await ctx.send(message)

@client.command(aliases = ["8ball"])
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
        return
    
    await ctx.send ("Tu perguntou: \"{}\" \n" + "Deixa eu pensar...".format(question))  
    await ctx.trigger_typing()
    await asyncio.sleep(5)
    await ctx.send (random.choice(responses))

@client.command()
async def voto(ctx, *, situation = None):
    
    if (situation == None):
        await ctx.send("Qual é a questão pra votar po?")
        return
    
    await ctx.send(situation + "\nO conselho tem {} minuto(s) para decidir.".format(votoTime))
    firstMessage = ctx.channel.last_message
    await firstMessage.add_reaction("<:pyes:700337751597383691>")
    await firstMessage.add_reaction("<:pno:700337705510502512>")
    await asyncio.sleep(votoTime * 60)
    yesCount = 0
    noCount = 0
    for i in firstMessage.reactions:
        if (i.emoji.name == "pyes"):
            yesCount = i.count
        elif (i.emoji.name == "pno"):
            noCount = i.count
    if (yesCount > noCount):
        await ctx.send ("\"{}\" \nO conselho decidiu que sim.".format(situation))
    elif (noCount > yesCount):
        await ctx.send ("\"{}\" \nO conselho decidiu que não.".format(situation))
    else:
        await ctx.send ("\"{}\" \nO conselho ficou dividido e não conseguiu tomar uma desição.".format(situation))

@client.command()
async def teste (ctx):
    ctx.send ("teste1")

@client.command()
async def apagar(ctx, amount = 0):
    author = ctx.author

    if (author.permissions_in(ctx.channel).manage_messages == True):
        if (amount > 10):
            amount = 10
        await ctx.channel.purge(limit = (amount + 1))
    else:
        await ctx.send("Você não pode apagar mensagens seu plebeu")

#Setting um global variables for the config command
votoTime = 3

@client.command()
async def config (ctx, parameter = None, value = 0):
    if (parameter == None):
        await ctx.send ("Qual configuração você quer alterar?")
        return

    if (parameter == "tempovoto"):
        global votoTime
        votoTime = value
        await ctx.send("O tempo de voto agora passou a ser de {} minuto(s).".format(str(votoTime)))

@client.command(aliases = ["kick"])
async def expulsar(ctx, member:discord.Member = None, *, reason = None):
    if (True == True):
        await ctx.send("Comando desativado")
        return

    if (member == None):
        await ctx.send("Você tem que dizer quem será o infeliz que será banido.")
        return

    for i in ctx.author.roles:
        if ((i.id == 449251888592977932) or (i.id == 744997848155816086) or (i.id == 840028423681343488)):
            éOMarvado = True
        else:
            éOMarvado = False
#This for will see if the author has any of the roles needed to normally ban people, than giving him access to this command if this is the case

    if (éOMarvado == True):
        if (reason == None):
            await member.kick()
        else:
            await member.kick(reason = reason)
    else:
        await ctx.send ("Tu não é o MARVADO, tu não pode expulsar ninguém.")

@client.command(aliases = ["ban"])
async def banir(ctx, member:discord.Member = None, *, reason = None):
    if (True == True):
        await ctx.send("Comando desativado")
        return

    if (member == None):
        await ctx.send("Você tem que dizer quem será o infeliz que será banido.")
        return

    for i in ctx.author.roles:
        if ((i.id == 449251888592977932) or (i.id == 744997848155816086) or (i.id == 840028423681343488)):
            éOMarvado = True
        else:
            éOMarvado = False
#This for will see if the author has any of the roles needed to normally ban people, than giving him access to this command if this is the case

    if (éOMarvado == True):
        if (reason == None):
            await member.ban()
        else:
            await member.ban(reason = reason)
    else:
        await ctx.send ("Tu não é o MARVADO, tu não pode expulsar ninguém.")

#Iniciação do client

client.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.dYiDqb6Nnl1TK03OpnJ5LfBId8U')
