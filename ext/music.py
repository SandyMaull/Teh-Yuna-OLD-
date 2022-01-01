import discord
import youtube_dl
import requests
import json
import os
from discord.ext import commands

class music(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You're not in a voice channel!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
        YDL_OPTIONS = {'format':'bestaudio'}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            #   exec_path = os.path.isfile('./Include/ffmpeg.exe')
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS, executable='./Include/ffmpeg.exe')
            # source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            #   vc.play(discord.FFmpegPCMAudio(executable=exec_path, source=source))
            vc.play(source)
        # except:
        #     await ctx.send("An error occurred, please check the backend services!")


    @commands.command()
    async def pause(self, ctx):
        await ctx.send("paused")
        await ctx.voice_client.pause()

    @commands.command()
    async def resume(self, ctx):
        await ctx.send("resume")
        await ctx.voice_client.resume()



def setup(client):
    client.add_cog(music(client))