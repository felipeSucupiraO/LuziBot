import asyncio
import discord
from discord.ext import commands
import random
from pathlib import Path

root_path = Path(__file__).resolve().parent

intents = discord.Intents.all()
client = commands.Bot(command_prefix = "luzi ", help_command = None, intents = intents)


#Setting some global variables for the config command
serverList = [None]
voteTimeList = [None]
mainChannelList = [None]
initialRoleList = [None]
# These variables work to make each server have it's own configurations in the array by making the index of the configuration the same as the index of the respective server on the "serversList" array.


#Events
@client.event
async def on_ready():
    print ("Bot is online")
    print ("Logged in as {}".format(client.user.name))

    i = 1
    for server in client.guilds:
        #This variable is used to make the if statement run just in the first for loop, to then run only the else statement.
        if (i == 1):
            serverList[0] = server
            voteTimeList[0] = 3
            mainChannelList[0] = None
            initialRoleList[0] = None
        else:
            serverList.append(server)
            voteTimeList.append(3)
            mainChannelList.append(None)
            initialRoleList.append(None)
        i = i + 1
        #These statements organize an array containing all the servers the bot is currently. Also, it creates arrays for information in which the lenght is the amount of servers, therefore, one variable for each server.

@client.event
async def on_member_join(member):
    mainChannel = member.guild.get_channel(mainChannelList[serverList.index(member.guild)])
    initialRole = member.guild.get_role(initialRoleList[serverList.index(member.guild)])

    mainChannel.send ("Welcome to the server, {}!".format(member.name))

    member.add_roles(initialRole)


@client.event
async def on_member_remove(member):
    mainChannel = member.guild.get_channel(mainChannelList[serverList.index(member.guild)])
    
    mainChannel.send("Goodbye, {}!".format(member.name))


#Commands
@client.command()
async def ping(ctx):
    await ctx.send("Pong! Latency: {}ms".format(str(round(client.latency * 1000))))


@client.command()
async def hello(ctx):
    await ctx.send("Hello, my name is Luzi! It is a pleasure to meet you!")


@client.command()
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
async def say(ctx, *, message = None):
    if (message == None):
        await ctx.send("Tell me what you want me to say.")
        return
    
    await ctx.send(message)


@client.command(aliases = ["8ball"])
#Here, the name of the function isn't the actual command because apparently you can't start with a number
async def ball(ctx, *, question = None):
    responses = [ 
        "For sure!", 
        "Decidedly yes.",
        "Undoubtedly!",
        "Yes, definitely.", 
        "You can count on a yes.", 
        "From my perspective, yes.", 
        "Seemingly, yes.", 
        "It seems so.", 
        "Yes", 
        "The sinals says yes.", 
        "It is too vague to tell. Try again.", 
        "Ask again later.", 
        "It's better not to tell you now.", 
        "I can't tell now.", 
        "Concentrate and ask again.", 
        "Don't count on this.", 
        "My awnser is no.", 
        "My sources says no.", 
        "It don't seems so.", 
        "Aparently, no."]

    if (question == None):
        await ctx.send ("Put your question after the command")
        return
    
    await ctx.send ("Your question: \"{}\" \n" + "Let me think...".format(question))  
    await ctx.trigger_typing()
    await asyncio.sleep(5)
    await ctx.send (random.choice(responses))


@client.command()
async def vote(ctx, *, situation = None):
    voteTime = int(voteTimeList[serverList.index(ctx.guild)])
    
    if (situation == None):
        await ctx.send("What do you want to vote for?")
        return
    
    await ctx.send(situation + "\nYou have {} minute(s) to decide.".format(voteTime))
    firstMessage = ctx.channel.last_message
    await firstMessage.add_reaction("<:thumbsup:>")
    await firstMessage.add_reaction("<:thumbsdown:>")
    await asyncio.sleep(voteTime * 60)

    yesCount = 0
    noCount = 0
    for i in firstMessage.reactions:
        if (i.emoji.name == "thumbsup"):
            yesCount = i.count
        elif (i.emoji.name == "thumbsdown"):
            noCount = i.count
    if (yesCount > noCount):
        await ctx.send ("\"{}\" \nThe result of the vote was \"yes\".".format(situation))
    elif (noCount > yesCount):
        await ctx.send ("\"{}\" \nThe result of the vote was \"no\".".format(situation))
    else:
        await ctx.send ("\"{}\" \nThe voting ended up tied.".format(situation))


@client.command()
async def delete(ctx, amount = 0):
    author = ctx.author

    if (author.permissions_in(ctx.channel).manage_messages == True):
        if (amount > 10):
            amount = 10
        await ctx.channel.purge(limit = (amount + 1))
    else:
        await ctx.send("You don't have permission to delete messages.")


#The kick and ban commands are not currently active because the role permission needed to use them is not working, therefore, anyone can use them.
@client.command()
async def kick(ctx, member:discord.Member = None, *, reason = None):
    if (True == True):
        await ctx.send("Deactivated command")
        return
    #This statement deactivates the command

    if (member == None):
        await ctx.send("Who will be kicked?")
        return

    for i in ctx.author.roles:
        if ((i.id == 449251888592977932) or (i.id == 744997848155816086) or (i.id == 840028423681343488)):
            canKick = True
        else:
            canKick = False
    #This for statement will check if the author has any of the roles needed to kick people and, if so, give access to the command.

    if (canKick == True):
        if (reason == None):
            await member.kick()
        else:
            await member.kick(reason = reason)
    else:
        await ctx.send ("You cannot kick people.")
@client.command()
async def ban(ctx, member:discord.Member = None, *, reason = None):
    if (True == True):
        await ctx.send("Deactivated command")
        return
    #This statement deactivates the command

    if (member == None):
        await ctx.send("Who will be banned?")
        return

    for i in ctx.author.roles:
        if ((i.id == 449251888592977932) or (i.id == 744997848155816086) or (i.id == 840028423681343488)):
            canBan = True
        else:
            canBan = False
    #This for statement will check if the author has any of the roles needed to ban people and, if so, give access to the command.

    if (canBan == True):
        if (reason == None):
            await member.ban()
        else:
            await member.ban(reason = reason)
    else:
        await ctx.send ("You cannot ban people.")


#The config command is not properly working
@client.command()
async def config (ctx, parameter = None, value = None):
    if (parameter == None):
        await ctx.send ("Which configuration do you wish to change?")
        return

    if (parameter == "votetime"):
        global voteTimeList
        timeValue = int(value)
        voteTimeList[serverList.index(ctx.guild)] = timeValue
        #The line above changes the configuration in the global array. It gets the index of the server in the servers array and then use it to change the respective configuration array. That is the same aproach used in the other config commands.
        await ctx.send("The voting time is now {} minute(s).".format(value))

    if (parameter == "mainchannel"):
        global mainChannelList
        channelValue = value.replace ("<", "")
        channelValue = channelValue.replace (">", "")
        channelValue = int(channelValue.replace ("#", ""))
        mainChannelList[serverList.index(ctx.guild)] = channelValue
        await ctx.send("The main channel is now {}".format(value))

    if(parameter == "initialrole"):
        global initialRoleList
        roleValue = value.replace ("<", "")
        roleValue = roleValue.replace (">", "")
        roleValue = roleValue.replace ("@", "")
        roleValue = int(roleValue.replace ("&", ""))
        initialRoleList[serverList.index(ctx.guild)] = roleValue
        await ctx.send("The initial role is now {}".format(value))


#Client's inicialization
token = open(root_path / "files" / "token.txt", "r", encoding = "uft-8")
client.run(token)
token.close
