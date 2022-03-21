import discord
from discord.ext import commands
import random
from datetime import datetime
import pytz

class fun(commands.Cog):
  def __init__(self, client):
    self.client = client

  #Heads or tails game
  @commands.command()
  async def headsortails(self, ctx):
    rand = random.randint(0, 1)
    if rand == 0:
      await ctx.send("Heads")
    else:
      await ctx.send("Tails")
  
  @commands.command()
  async def rolldice(self, ctx):
    rand = random.randint(1, 6)
    await ctx.send("You rolled a " + str(rand))

  
  @commands.command()
  async def milkme(self, ctx):
    await ctx.send("yes daddy")
  
  

  @commands.command()
  async def ligma(self, ctx):
    await ctx.send("ligma balls")
  
  @commands.command()
  async def jensen(self, ctx):
    await ctx.send("sugs nuts")

  
  #Return time in New Zealand
  @commands.command()
  async def time(self, ctx):
    now = datetime.now(pytz.timezone('Pacific/Auckland'))
    current_time = now.strftime("%H:%M:%S")
    await ctx.send("The time in New Zealand is " + current_time)
  
  @commands.command()
  async def pokie(self, ctx):
    emojis = ["💎", "🍒", "🍌", "🍇", "💩"]
    num1 = random.randint(0, 4)
    num2 = random.randint(0, 4)
    num3 = random.randint(0, 4)
    await ctx.send(emojis[num1]+emojis[num2]+emojis[num3])
    if (num1+num2+num3==0):
      await ctx.send("Holy shit u got 3 diamonds!")
    elif (num1==1 and num2==1 and num3==1):
      await ctx.send("3 cherries nice balls.")
    elif (num1==2 and num2==2 and num3==2):
      await ctx.send("pass me the banan.")
    elif (num1==3 and num2==3 and num3==3):
      await ctx.send("3 Diamonds would have been better.")
    elif (num1==4 and num2==4 and num3==4):
      await ctx.send("LMAO megashit moment xd")
    else:
      await ctx.send("You suck try again.")
  

    


def setup(client):
  client.add_cog(fun(client))