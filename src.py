import os
import discord
from discord import channel
from discord.ext import commands, tasks
from discord.message import MessageReference
from webserver import keep_alive
import asyncio
import dns
import time
import _thread
import datetime
import requests
from math import floor
from discord.colour import Colour
import random
b = commands.Bot(command_prefix='.')
reminder=[]
from pymongo import MongoClient
c = discord.Client()
a=[]
rem=[]


async def ch() :
  await b.wait_until_ready()
  statuses= ["Absorbed Aman's AI GF", "Looking after IIITS UWU", "Hosted by Viper"]
  while not b.is_closed() :
    status = random.choice(statuses)
    if(status=="Hosted by Viper") :
        await b.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(2)
    else :
      await b.change_presence(activity=discord.Game(name=status))
      await asyncio.sleep(60)

b.loop.create_task(ch())

# @b.event
# async def on_message_delete(message):
#   msg ='**' + str(message.author) + '**' + ' just deleted a message in '+ '**'+str(message.channel)+ ' : ' + str(message.content) + '**'
#   channel = b.get_channel(872934491985969223)
#   if not message.author.bot:
#     await channel.send(msg)
#   await b.process_commands(message)

@b.event
async def on_message(message) :
  def rmbc(stg):
    stg = stg.replace('[', '')
    stg = stg.replace(']', '')    
    return stg
  if message.content.startswith('$dict'):
    try :
      b.embeds = []
      msg= message.content
      mesg = msg[6:]
      url = 'https://api.urbandictionary.com/v0/define'
      prms = {"term" : mesg};
      res = requests.get(url, params = prms);
      defs = res.json()
      for i in range (len(defs['list'])):
        embed=discord.Embed(title=f"Meaning of {mesg}", color=discord.Color.dark_grey())
        embed.add_field(name="Definition", value=f"```{rmbc(defs['list'][i]['definition'])}```", inline=False)
        embed.add_field(name="Example", value=f"```{rmbc(defs['list'][i]['example'])}```", inline=False)
        embed.add_field(name="Link", value=rmbc(defs['list'][i]['permalink']), inline=False)
        b.embeds.append(embed);
      buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] 
      current = 0
      msg = await message.reply(embed=b.embeds[current])
    
      for button in buttons:
        await msg.add_reaction(button)
        
      while True:
        try:
            reaction, user = await b.wait_for("reaction_add", check=lambda reaction, user: user == message.author and reaction.emoji in buttons, timeout=None)

        except asyncio.TimeoutError:
            return print("test")

        else:
            previous_page = current        
            if reaction.emoji == u"\u23EA":
                current = 0
                
            elif reaction.emoji == u"\u2B05":
                if current > 0:
                    current -= 1
                    
            elif reaction.emoji == u"\u27A1":
                if current < len(b.embeds)-1:
                    current += 1

            elif reaction.emoji == u"\u23E9":
                current = len(b.embeds)-1

            for button in buttons:
                await msg.remove_reaction(button, message.author)

            if current != previous_page:
                await msg.edit(embed=b.embeds[current])
    except :
      await message.reply('No such word exists....Get Some Help!')
  if message.content.startswith('.tt') :
    await message.reply(file=discord.File('timetablenew.png'))
  if message.content.startswith('.al') :
    await message.reply(file=discord.File('almanac.png'))
  if message.content.startswith('.ex') :
    await message.reply(file=discord.File('exam.png'))
  if message.content.startswith('.scq') :
    await message.reply('**Scheduled Quiz Dates in November**\n```OOP  - 10\nCA   - 11\nM3   - 13\nADSA - 15\nDBMS - 16```')
  if message.content.startswith('.yayy') :
    await message.delete()
  if message.content.startswith('.heyy') :
    await message.delete()
  if message.content.startswith('.porz') :
    await message.delete()
  if ( message.content=='<@!872480069430431794>') :
    embed=discord.Embed(title=f"Help Menu For {message.author}", color=discord.Color.dark_grey())
    embed.add_field(name="View Help Menu", value='```Mention The Bot```',inline =False)
    embed.add_field(name='Basic Commands',value='```.al  --> View Almanac\n\n.tt  --> View TimeTable\n\n.ex  --> View End-Sem-Exam Schedule\n\n.scq --> View Dates of Scheduled Quiz```',inline=False)
    embed.add_field(name="View Meaning of a Word", value='```$dict word```',inline = False)
    await message.reply(embed=embed)
  await b.process_commands(message)
  
# @b.command()
# async def yayy(ctx) :
#   org = "CantEscapeFromMe"
#   print(org)
#   message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
#   string = f"{ctx.author}"
#   nick = string[:len(string)-5]
#   await b.get_member(872480069430431794).edit(nick=nick)
#   # await b.change_own_nick(b.nick, string[:len(string)-5])
#   #  with open('image.png', 'rb') as image:
#   #    await b.user.edit(avatar=image)
#   await message.reply(file=discord.File('yay.gif'))
#   # await b.change_own_nick(b.nick, org)

 

# @b.command()
# async def yayy(ctx,  m : discord.Member):
#   nick='CodeVentures'
#   await m.edit(nick=nick)




# @b.command()
# async def yayy(ctx,  m : discord.Member= None):
#       try :
#         message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
#         m= message.author
#         string = f"{ctx.author}"
#         nick = string[:len(string)-5]
#         await m.edit(nick=nick)
#         await message.reply(file=discord.File('yay.gif'))
#         await asyncio.sleep(60)
#         nick="CantEscapeFromNQN"
#         await m.edit(nick=nick)

#       except :
#         try :
#             message = b.get_channel(ctx.channel.id)
#             m= ctx.author
#             string = f"{ctx.author}"
#             nick = string[:len(string)-5]
#             await m.edit(nick=nick)
#             await message.send(file=discord.File('yay.gif'))
#             await asyncio.sleep(60)
#             nick="CantEscapeFromNQN"
#             await m.edit(nick=nick)
#         except :
#           await ctx.reply('idiot ....mention only bot')







# @b.command()
# async def heyy(ctx,  m : discord.Member = None):
#       try :
#         message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
#         m= message.author
#         string = f"{ctx.author}"
#         nick = string[:len(string)-5]
#         await m.edit(nick=nick)
#         await message.reply(file=discord.File('hey.gif'))
#         await asyncio.sleep(60)
#         nick="CantEscapeFromNQN"
#         await m.edit(nick=nick)

#       except :
#         try :
#             message = b.get_channel(ctx.channel.id)
#             m= ctx.author
#             string = f"{ctx.author}"
#             nick = string[:len(string)-5]
#             await m.edit(nick=nick)
#             await message.send(file=discord.File('hey.gif'))
#             await asyncio.sleep(60)
#             nick="CantEscapeFromNQN"
#             await m.edit(nick=nick)
#         except :
#           await ctx.reply('idiot ....mention only bot')






# @b.command()
# async def porz(ctx,  m : discord.Member = None):
#       try :
#         message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
#         m= message.author
#         string = f"{ctx.author}"
#         nick = string[:len(string)-5]
#         await m.edit(nick=nick)
#         await message.reply(file=discord.File('porz.gif'))
#         await asyncio.sleep(60)
#         nick="CantEscapeFromNQN"
#         await m.edit(nick=nick)

#       except :
#         try :
#             message = b.get_channel(ctx.channel.id)
#             m= ctx.author
#             string = f"{ctx.author}"
#             nick = string[:len(string)-5]
#             await m.edit(nick=nick)
#             await message.send(file=discord.File('porz.gif'))
#             await asyncio.sleep(60)
#             nick="CantEscapeFromNQN"
#             await m.edit(nick=nick)
#         except :
#           await ctx.reply('idiot ....mention only bot')



keep_alive()
b.run('ODcyNDgwMDY5NDMwNDMxNzk0.YQqeYg.BrNI68Hbpi2-PD2_07xMeX1MMBo')
