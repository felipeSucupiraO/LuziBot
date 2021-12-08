import discord


bot = discord.Client()


@bot.event
async def on_ready():
    print("Bot Ready. \nLogged in as " + bot.user.name)

@bot.event
async def on_message (message):
    if message.author == bot.user:
        return

    if message.content.startswith("luzi oi"):
        await message.channel.send("Olá")

    if message.content.startswith("luzi ping"):
        await message.channel.send("Pong!")

    with open ("files\helpMessage.txt", "r") as f:
        helpMessage = f.read()
    if message.content.startswith("luzi help"):
        await message.channel.send(helpMessage)


bot.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.dYiDqb6Nnl1TK03OpnJ5LfBId8U')