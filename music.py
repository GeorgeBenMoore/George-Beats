import discord
from discord.ext import commands
import youtube_dl
import random
import os
from youtubesearchpython import VideosSearch
import youtubesearchpython

queue = []




class music(commands.Cog):
  def __init__(self, client):
    self.client = client

  
  #search youtube for a song URL based off word
  @commands.command()
  async def search(self, ctx, *content):
    word = " ".join(content)
    word = word.replace("'", "")
    videosSearch = VideosSearch(word, limit = 1)
    result = videosSearch.result()
    url = result["result"][0]["link"]
    await ctx.send(url)


    
  #join bot to voice channel (if user is in a channel)
  @commands.command()
  async def join(self,ctx):
    if ctx.author.voice is None:
      await ctx.send("Pls join a voice channel, sugma")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

  #disconnect bot from voice channel
  @commands.command()
  async def disconnect(self,ctx):
    await ctx.voice_client.disconnect()
    await ctx.send("Fuck you")


  @commands.command()
  async def play(self, ctx, *content):
    #Bot Join Voice Channel
    if ctx.author.voice is None:
      await ctx.send("Pls join a voice channel, sugma")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

    #reformat input word
    word = " ".join(content)
    word = word.replace("'", "")

    #search youtube for top result
    videosSearch = VideosSearch(word, limit = 1)
    result = videosSearch.result()

    #Extract song title and URL
    await ctx.send("Now Playing: " + result["result"][0]["title"])
    url = result["result"][0]["link"]

    #Stop Current Song
    if ctx.voice_client != None:
      ctx.voice_client.stop()
    
    #Play searched song
    FFMPEG_OPTIONS = {'before_options': "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
    YDL_OPTIONS = {"format":"bestaudio"}
    vc = ctx.voice_client
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info["formats"][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)
  
  #Pause Current Song
  @commands.command()
  async def pause(self,ctx):
    await ctx.send("Song paused")
    ctx.voice_client.pause()
    
  #Resume Current Song
  @commands.command()
  async def resume(self,ctx):
    await ctx.send("Song resumed")
    ctx.voice_client.resume()
  
   


def setup(client):
  client.add_cog(music(client))



