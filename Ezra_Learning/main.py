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

@client.tree.command(name="embed", description="Embed demo!", guild=GUILD_ID)
async def embed(interaction:discord.Interaction):
    embed = discord.Embed(title="I am a title", url="https://github.com/arionlauriano/Hollow-Universe/blob/DiscordBot-Learning/Ezra_Learning/main.py", description="I am the description", color=discord.Color.purple())
    embed.add_field(name="Field 1 Title", value="This is a field!", inline=False)
    embed.add_field(name="Field 2 Title", value="This is a field!", inline=True)
    embed.add_field(name="Field 3 Title", value="This is a field!")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1409660471216177272/1524498522236522596/Untitled_Artwork.png?ex=6a51f1a3&is=6a50a023&hm=64556bfb4f1ae9af4de45e3cb6342630933a730fe7f96c58e2baf5c6af0e5d6a&=&format=webp&quality=lossless&width=1265&height=1265")
    embed.set_footer(text="This is the footer!")
    embed.set_author(name=interaction.user.name, icon_url=interaction.user.avatar)
    await interaction.response.send_message(embed=embed)

class View(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.red, emoji="🔥")
    async def clickme(self, button, interaction):
        await button.response.send_message("You've ckicked the button!")

    @discord.ui.button(label="Button 2", style=discord.ButtonStyle.blurple, emoji="🥎")
    async def button2(self, button, interaction):
        await button.response.send_message("This is the second button!")

    @discord.ui.button(label="Button 3", style=discord.ButtonStyle.green, emoji="⚾")
    async def threebutton(self, button, interaction):
        await button.response.send_message("This is the third button!")

@client.tree.command(name="button", description="Displaying a button", guild=GUILD_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())

# Busca o token do bot em confidentials.py
Token = confidentials.BotToken
client.run(Token)
