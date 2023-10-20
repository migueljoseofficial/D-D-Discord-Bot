import settings
import discord
from discord.ext import commands
import random


logger = settings.logging.getLogger("bot")

def run():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event #this command will react oa certain event
    async def on_ready(): 
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
    

    
    @bot.command() #user command
    async def ping(ctx):
        await ctx.send("pong")
    
    ##the following commands are the basic dice for d&d
    @bot.command()
    async def d(ctx, dice_type: int):
        if dice_type in [4, 6, 8, 10, 12, 20]:
            roll = random.randint(1, dice_type)
            await ctx.send(f"You have rolled {roll}!")
        else:
            await ctx.send("Invalid dice type!")


    # @bot.command()
    # async def d6(ctx):
    #     await ctx.send(random.randint(1, 6))

    # @bot.command()
    # async def d8(ctx):
    #     await ctx.send(random.randint(1, 8))

    # @bot.command()
    # async def d10(ctx):
    #     await ctx.send(random.randint(1, 10))
    
    # @bot.command()
    # async def d12(ctx):
    #     await ctx.send(random.randint(1, 12))
    
    # @bot.command()
    # async def d20(ctx):
    #     await ctx.send(random.randint(1, 20))





    


    bot.run(settings.DISCORD_API_SECRET, root_logger=True)


if __name__ == '__main__':
    run()

