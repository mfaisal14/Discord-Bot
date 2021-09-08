import discord
from discord.ext import commands

class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def schedule(self, ctx, user: discord.User = None):
        if user is None:
            await ctx.send('Please porvide a proper user!')
            return

        embed = discord.Embed(title = 'RyeEng Schedule', description = f'here is some info on {user.name}\'s Schedule for W2021\n\n', 
        colour = discord.Colour.green())
        
        embed.add_field(name = '__Monday__', value = '**Course: **' + 'COE 528\n' + '**Class Type: **' + 'Lab\n'+ '**Class Time: **' 
        + '12:00PM - 2:00PM\n' + '**Professor\'s Name: **' + 'Staff\n' + '\n\n' +'**Course: **' + 'COE 528\n' + '**Class Type: **' + 
        'Lecture\n'+   '**Class Time: **' + '2:00PM - 3:00PM\n' + '**Professor\'s Name: **' + 'Olivia Das\n\n', inline = False)
        
        embed.add_field(name = '__Tuesday__', value = '**Course: **' + 'COE 428\n' + '**Class Type: **' + 'Lab\n'+ '**Class Time: **' 
        + '8:00AM - 10:00AM\n' + '**Professor\'s Name: **' + 'Staff\n' + '\n\n' +'**Course: **' + 'COE 428\n' + '**Class Type: **' + 
        'Lecture\n'+   '**Class Time: **' + '12:00PM - 2:00PM\n' + '**Professor\'s Name: **' + 'Reza Sedaghat\n\n', inline = False)
        
        embed.add_field(name = '__Wednesday__', value = '**Course: **' + 'COE 428\n' + '**Class Type: **' + 'Lecture\n'+ '**Class Time: **' 
        + '2:00PM - 4:00PM\n' + '**Professor\'s Name: **' + 'Reza Sedaghat\n\n', inline= False)
        
        embed.add_field(name = '__Friday__', value = '**Course: **' + 'ECN 801\n' + '**Class Type: **' + 'Lecture\n'+ '**Class Time: **' 
        + '9:10AM - 10:30AM\n' + '**Professor\'s Name: **' + 'Mikhail Gurvitz', inline = False)
        
        

        await ctx.send(embed = embed)
    
    @commands.command()
    async def exams(self,ctx):
        embed = discord.Embed(title = "Midterm Exam Schedule", description = "W2021 Midterm Exam Schedule", colour = discord.Colour.red())
        embed.add_field(name = "__Tuesday March 2 2021__", value = "**COE528: 12:00PM - 4:00PM**",inline=False)
        embed.add_field(name = "__Friday March 5 2021__", value = "**ECN801: 6:00PM - 8:30PM**", inline = False)
        embed.add_field(name = "__Wednesday March 10 2021__", value = "**COE428: 8:00AM - 12:00PM**", inline = False)

        await ctx.send(embed = embed)


def setup(client):
    client.add_cog(Utils(client))