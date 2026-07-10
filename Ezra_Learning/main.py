import discord
from discord.ext import commands
from discord import app_commands

import confidentials

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            ServerID = confidentials.DevelopmentServerID
            guild = discord.Object(id=ServerID)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} comands to guild {guild.id}')
        except Exception as e:
            print(f'Error syncing commands: {e}')


    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted!')



intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

ServerID = confidentials.DevelopmentServerID
GUILD_ID = discord.Object(id=ServerID)

@client.tree.command(name="helloo", description="Say Hello.", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there!")

@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

# Busca o token do bot em confidentials.py
Token = confidentials.BotToken
client.run(Token)
