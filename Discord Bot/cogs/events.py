import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cool(self, ctx):
        await ctx.send(':sunglasses:')
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("Cog ready!")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.client.get_channel('796877555181420614').send(member + "has joined the server")
    
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.client.get_channel('796877555181420614').send(member + "has left the server")

def setup(client):
    client.add_cog(Events(client))