import discord


class MyClient (discord.Client):
    async def on_ready(self):
        print("Bot Ready. \nLogged in as {0.user}".format(self.user))


    async def on_message(self, message):
        with open ("comandsList.txt", "r") as f:
            commandsList = f.read()
        if message.author == self.user:
            return

        if message.content.startswith("luzi oi"):
            await message.channel.send("Olá")

        if message.content.startswith("luzi ping"):
            await message.channel.send("Pong!")

        if message.content.startswith("luzi help"):
            await message.channel.send(commandsList)


client = MyClient()
client.run('ODk5Nzg1Nzk0MjQyMzU1MjUy.YW300g.NSEiWxLYNcs2xASZsIwHSVlOgiQ')

#Find a way for the commandsList variable to be equal to the txt