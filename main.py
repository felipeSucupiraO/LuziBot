import discord


client = discord.Client()


@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("luzi oi"):
        await message.channel.send("Olá")

    if message.content.startswith("luzi ping"):
        await message.channel.send("Pong!")

    if message.content.startswith("luzi help"):
        await message.channel.send(commandsList)

commandsList = "Lista de comandos (prefixo \"luzi\") \n \n- \"help\": Luzi apresenta a lista de todos os comandos \n- \"oi\": Luzi se apresenta \n- \"ping\": Luzi devolve"


client.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.NSEiWxLYNcs2xASZsIwHSVlOgiQ')

#Find a way for the commandsList variable to be equal to the txt