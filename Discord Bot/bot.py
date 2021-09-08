import discord
from discord.ext import commands

#Client variable that makes use of Discord commands module
client = commands.Bot(command_prefix = '!')

TOKEN = 'INSERT TOKEN HERE'

cogs = ['cogs.events', 'cogs.Utils']

for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f'Could not load cog {cog}: {str(e)}')



@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("The Ryerson Engineering Game"))
    print("Bot is ready!")

@client.command()
async def loadcog(ctx, cogname = None):
    if cogname is None:
        return
    try:
        client.load_extension(cogname)
    except Exception as e:
        print(f'Could not load cog {cogname}: {str(e)}')
    else:
        print("Loaded cog successfully")

@client.command()
async def unloadcog(ctx, cogname = None):
    if cogname is None:
        return
    try:
        client.unload_extension(cogname)
    except Exception as e:
        print(f'Could not unload cog {cogname}: {str(e)}')
    else:
        print("Unloaded cog successfully")

@client.command()
async def ping(ctx):
    await ctx.send(':ping_pong: Pong!')

@client.command()
async def multi(ctx, role: discord.Role, user: discord.User):
    await ctx.send(user.id)
    await ctx.send(role.id)

@client.command()
async def say(ctx, *, message = None):
    if message == None:
        await ctx.send("Please enter a valid message")
        return
    await ctx.send(f'{ctx.author.name} said {message}')

@client.command()
async def kick(ctx, member: discord.Member = None, *, reason = None):
    if member is None:
        await ctx.send('Please enter a valid user name.')
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked from the server')
    
@client.command()
async def ban(ctx, member: discord.Member = None, *, reason = None):
    if member is None:
        await ctx.send('Please enter a valid user name.')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned from the server')

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.Guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.Guild.unban(user)
            await ctx.send(f'{user.mention} has been unbanned from the server')
            return


client.run(TOKEN)




