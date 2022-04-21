from discord.ext import commands

class Messages(commands.Cog):
    """ Commands to do the weather configs """

    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Messages(bot))
