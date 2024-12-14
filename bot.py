# Necassary libraries
import os
import random
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from datetime import datetime, timedelta, timezone

# Fetching the values from the .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Activate necessary intents
intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
intents.guilds = True

# Using '!' as a command prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Confirmation and guild details in the terminal
@bot.event
async def on_ready():
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(
        f'{bot.user.name} er koblet til følgende Discord-server:\n'
        f'{guild.name}(id: {guild.id})'
    )

# Load welcome message from a file
def load_welcome_message():
    try:
        with open('welcome_message.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return 'Welcome message could not load. File "welcome_message.txt" does not exist.'

WELCOME_MESSAGE = load_welcome_message()

# Sends a welcome message to the user with exception
@bot.event
async def on_member_join(member):
    try:
        await member.create_dm()
        await member.send(f'{WELCOME_MESSAGE}')
    except discord.Forbidden:
        print(f"Could not send DM to {member.name}#{member.discriminator}. User may have blocked DM's.")

# Load the help message from a file
def load_help_message():
    try:
        with open('help_message.txt', 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return 'Help message could not load. File "help_message.txt" does not exist.'

help_message = load_help_message()

# The command 'hjelp' displays a list of commands and it's uses
@bot.command(name='hjelp')
async def custom_help(ctx):
    await ctx.send(help_message)

# Load the encouraging message from a file
def load_encourage_message():
    try:
        with open('encourage_message.txt', 'r', encoding='utf=8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ['Encourage message could not load. File "encourage_message.txt" does not exist.']

encourage_message = load_encourage_message()

# Sends an ecnouraging message in random    
@bot.command(name='oppmuntring')
async def send_encourage(ctx):
    # Velg et tilfeldig sitat og send det
    response = random.choice(encourage_message)
    await ctx.send(response)

# Load the hug message from a file
def load_hug_message():
    try:
        with open('hug_message.txt', 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ['Klem-meldingene kunne ikke lastes. Filen "hug_message.txt" eksisterer ikke.']

# Load the hug gif links from a file
def load_hug_gifs():
    try:
        with open('hug_gifs.txt', 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []

hug_message = load_hug_message()
hug_gifs = load_hug_gifs()

# Sends a hug message and a hug gif to a mentioned user
@bot.command(name='klem')
async def send_hug(ctx, member: discord.Member = None):

# If no member is mentioned, use Dagny as the sender.
    if not member:
        member = ctx.author

    # Choose a random hug-message
    hug_text = random.choice(hug_message)

# Checks if a user is mentioned or not
    if member == ctx.author:
        await ctx.send(f"{bot.user.mention} gir en stor klem til {member.mention}! {hug_text}")
    else:
        await ctx.send(f"{ctx.author.mention} gir en stor virtuell klem til {member.mention}! {hug_text}")

    # Send a hug gif if gifs exists in the list
    if hug_gifs:
        hug_gif = random.choice(hug_gifs)
        await ctx.send(hug_gif)
    else:
        await ctx.send("Beklager, jeg fant ingen gifs å sende.")

# Function to load support phrases from a file
def load_support_phrases():
    try:
        with open('support_phrases.txt', 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ['støtter faktisk']  # Fallback if file is not found

# Function to load support emojis from a file
def load_support_emojis():
    try:
        with open('support_emojis.txt', 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return ['🤝']  # Fallback if file is not found
    
# Load support phrases
support_phrases = load_support_phrases()

# Load support emojis
support_emojis = load_support_emojis()

# The command !støtte will choose a person to support
@bot.command(name='støtte', help='Gives support to a specific member or a random person')
async def støtte(ctx, member: discord.Member = None):
    # If a member is mentioned, we support that person directly
    if member:
        # Choose a random support phrase and emoji
        support_phrase = random.choice(support_phrases)
        support_emoji = random.choice(support_emojis)

        # Send a message saying that you support the mentioned person
        await ctx.send(f"{ctx.author.mention} {support_phrase} {member.mention}! {support_emoji}")
    else:
        # If no one is mentioned, choose a random active participant in the discussion
        time_window = 5  # in minutes
        recent_members = []

        # Get the current time and calculate the cutoff time for the discussion period
        now = datetime.now(timezone.utc)
        cutoff_time = now - timedelta(minutes=time_window)

        # Loop through the messages in the channel to find members who have been active recently
        async for message in ctx.channel.history(after=cutoff_time):
            if message.author != bot.user:  # Ignore bot's own messages
                recent_members.append(message.author)

        # Remove duplicates by converting the list to a set, and then back to a list
        recent_members = list(set(recent_members))

        # If no one has been active recently, send a message
        if not recent_members:
            await ctx.send("No one has been active in the discussion for a while. Please be more active!")
            return

        # Randomly select a person from the list of active members
        supported_member = random.choice(recent_members)

        # Choose a random support phrase and emoji
        support_phrase = random.choice(support_phrases)
        support_emoji = random.choice(support_emojis)

        # Send a message saying the bot supports the randomly selected person
        await ctx.send(f"{bot.user.mention} {support_phrase} {supported_member.mention}! {support_emoji}")

# Writes errors to the err.log fil
@bot.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        now = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        try:
            if event == 'on_message':
                message = args[0] if len(args) > 0 else "No message details available"
                f.write(f'[{now}] Unhandled message: {str(message)[:500]}\n') # Truncate to 500 chars
            else:
                f.write(f'[{now}] Unknown error in event {event} with args: {args}, kwargs: {kwargs}\n')
        except Exception as log_error:
            f.write(f'[{now}] Failed to log error: {log_error}\n')

# Print message if the bot was stopped by keyboard, instead of a log of events
if __name__ == "__main__":
    try:
        asyncio.run(bot.start(TOKEN))
    except KeyboardInterrupt:
        print(f'Bot has been manually stopped.')