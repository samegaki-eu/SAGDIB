"""Main bot file"""

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

sagdib = commands.Bot(intents=intents,
                      command_prefix=commands.when_mentioned_or("🔱"),
                      case_insensitive=True)
sagdib.remove_command("help")
