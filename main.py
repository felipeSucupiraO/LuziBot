import asyncio
import discord
from discord.ext import commands
import random
from pathlib import Path

root_path = Path(__file__).resolve().parent

client = commands.Bot(command_prefix = "luzi ", help_command = None)

#Setting um global variables for the config command
serverList = [None]
votoTimeList = [None]
mainChannelList = [None]
initialRoleList = [None]

#Events

@client.event
async def on_ready():
    print ("Bot is online")
    print ("Logged in as {}".format(client.user.name))

    i = 1
    for server in client.guilds:
        #This variable is used to make the if statement run just in the first for loop
        if (i == 1):
            serverList[0] = server
            votoTimeList[0] = 3
            mainChannelList[0] = None
            initialRoleList[0] = None
        else:
            serverList.append(server)
            votoTimeList.append(3)
            mainChannelList.append(None)
            initialRoleList.append(None)
        # These statements organize an array containing all the servers the bot is currently in and create arrays for information of the same lenght of the servers
        i = i + 1

@client.event
async def on_member_join(member):
    mainChannel = member.guild.get_channel(mainChannelList[serverList.index(member.guild)])
    initialRole = member.guild.get_role(initialRoleList[serverList.index(member.guild)])

    mainChannel.send ("{} agora faz parte do clube da luta. Já sabe a primeira regra né?".format(member.name))

    member.add_roles(initialRole)

@client.event
async def on_member_remove(member):
    mainChannel = member.guild.get_channel(mainChannelList[serverList.index(member.guild)])
    
    mainChannel.send("Adeus {}, obrigado por não apagar o geraldo.".format(member.name))


#Commands

@client.command()
async def ping(ctx):
    await ctx.send("Pong! Latência: {} ms".format(str(round(client.latency * 1000))))

@client.command()
async def oi(ctx):
    await ctx.send("Olá, prazer, Luzineria, agora cala a boca e trás a porra da gasolina caralho")

@client.command(aliases = ["ajuda"])
async def help(ctx, category = None):
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
    votoTime = int(votoTimeList[serverList.index(ctx.guild)])
    
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
    mainChannel = ctx.guild.get_channel(mainChannelList[serverList.index(ctx.guild)])
    await mainChannel.send("teste")

@client.command()
async def apagar(ctx, amount = 0):
    author = ctx.author

    if (author.permissions_in(ctx.channel).manage_messages == True):
        if (amount > 10):
            amount = 10
        await ctx.channel.purge(limit = (amount + 1))
    else:
        await ctx.send("Você não pode apagar mensagens seu plebeu")

@client.command()
async def vera(ctx):
    for role in ctx.author.roles:
        if (role.id == "449251888592977932" or role.id == "744997848155816086"):
            break
        else:
            await ctx.send ("Você não é digno.")
            return

    server = ctx.guild
    await server.create_text_channel("vera")
    for channel in server.channels:
        if (channel.name == "vera"):
            channelVera = channel
    
    counter = 1
    while (counter <= 10):
        await channelVera.send("<:smallvera:742756448085475449>")
        message = channelVera.last_message
        await message.add_reaction("<:smallvera:742756448085475449>")
        await message.add_reaction("<:microvera:742841219574661133>")
        await message.add_reaction("<:nanovera:742840914015420597>")
        await message.add_reaction("<:quantumvera:756146161840029846>")
        counter = counter + 1

@client.command()
async def config (ctx, parameter = None, value = None):
    if (parameter == None):
        await ctx.send ("Qual configuração você quer alterar?")
        return

    if (parameter == "tempovoto"):
        global votoTimeList
        finalValue = int(value)
        votoTimeList[serverList.index(ctx.guild)] = finalValue
        await ctx.send("O tempo de voto agora passou a ser de {} minuto(s).".format(value))

    if (parameter == "canalprincipal"):
        global mainChannelList
        finalValue = value.replace ("<", "")
        finalValue = finalValue.replace (">", "")
        finalValue = int(finalValue.replace ("#", ""))
        mainChannelList[serverList.index(ctx.guild)] = finalValue
        await ctx.send("Agora o meu canal principal é {}".format(value))

    if(parameter == "cargoinicial"):
        global initialRoleList
        finalValue = value.replace ("<", "")
        finalValue = finalValue.replace (">", "")
        finalValue = finalValue.replace ("@", "")
        finalValue = int(finalValue.replace ("&", ""))
        initialRoleList[serverList.index(ctx.guild)] = finalValue
        await ctx.send("Agora o cargo para novos membros do server é {}".format(value))

    # The statements are made in a way that each server has it's own configurations in the array, in a way that the index of the configuration is the same of the index of the respective guild on the "serversList" array 

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
