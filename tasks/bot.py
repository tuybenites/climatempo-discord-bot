from discord.ext import commands
import decouple

bot = commands.Bot("!")

TOKEN = decouple.config("SECRET_TOKEN")
bot.run(TOKEN)
