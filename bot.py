from discord.ext import commands
import decouple

bot = commands.Bot("!")


bot.load_extension("manager")
bot.load_extension("commands.messages")


TOKEN = decouple.config("SECRET_TOKEN")

bot.run(TOKEN)
