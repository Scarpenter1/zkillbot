import discord
from discord.ext import commands
from .config import TOKEN, TARGET_DISCORD_CHANNEL_ID
from .websocket_handler import subscribe_to_websocket

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    bot.loop.create_task(subscribe_to_websocket(bot))  # Pass bot to the websocket handler
    print(f'Logged in as {bot.user}')
    channel = bot.get_channel(TARGET_DISCORD_CHANNEL_ID)
    if channel:
        await channel.send("Connected Successfully")
    else:
        print(f"Channel with ID {TARGET_DISCORD_CHANNEL_ID} not found")

def run_bot():
    bot.run(TOKEN)
