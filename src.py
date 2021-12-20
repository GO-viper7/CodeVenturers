import os
import discord
from discord import channel
from discord.ext import commands
from discord.message import MessageReference
from webserver import keep_alive
import asyncio
import dns
import time
import _thread
import datetime
from pip._vendor import requests
from math import floor
import flask
from discord.colour import Colour
import random
b = commands.Bot(command_prefix='.',intents=discord.Intents.all())
reminder=[]
from pymongo import MongoClient
c = discord.Client()
a=[]
rem=[]
import io
import pytesseract
import cv2
import numpy as np
from PIL import Image
import json

def get_string(imageLink):
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract'
    response = requests.get(imageLink)
    img = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    return text


async def ch() :
  await b.wait_until_ready()
  statuses= [ "Looking after IIITS UWU",]
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



# @b.event
# async def on_member_update(before, after) :
#   if after.status is discord.Status.idle:
#     await message.reply("```U are Idle now, u shouldn't be chatting ryt? :)```")

cluster=MongoClient()
db=cluster["test"]
coll=db["SFF"]
guild = None
async def ch() :
  await b.wait_until_ready()
  statuses= [ "Looking after IIITS UwU"]
  while not b.is_closed() :
    status = random.choice(statuses)
    if(status=="Hosted by Viper") :
        await b.change_presence(activity=discord.Game(name=status))
        await asyncio.sleep(2)
    else :
      await b.change_presence(activity=discord.Game(name=status))
      await asyncio.sleep(60)

b.loop.create_task(ch())


async def change_nickname() :
  await asyncio.sleep(5)
  amanbot =await guild.fetch_member(788616065042219031)
  while not b.is_closed() :
      names=["useless_goddess", "goddessofchaos","._.braindead._."]
      s= random.choice(names)
      print('changed')
      await amanbot.edit(nick=s)
      await asyncio.sleep(60)


# print(guild)
# amanbot = None

b.loop.create_task(change_nickname())
   


# @b.event
# async def on_message_delete(message):
#   msg ='**' + str(message.author) + '**' + ' just deleted a message in '+ '**'+str(message.channel)+ ' : ' + str(message.content) + '**'
#   channel = b.get_channel(872934491985969223)
#   if not message.author.bot:
#     await channel.send(msg)
#   await b.process_commands(message)

@b.event
async def on_ready():
  global guild
  guild = b.get_guild(783921718392520715)
  print("Bot Ready")


@b.command()
async def nickreset(ctx) :
  amanbot =await guild.fetch_member(ctx.author.id)
  await amanbot.edit(nick='')
  await ctx.send(f'NickName for {ctx.author.mention} has been reset')


@b.command()
async def nick(ctx,*,s) :
  amanbot =await guild.fetch_member(ctx.author.id)
  await amanbot.edit(nick=s)
  await ctx.send(f'NickName for {ctx.author.mention} has been changed')




@b.event
async def on_message(message) : 
  def rmbc(stg):
    stg = stg.replace('[', '')
    stg = stg.replace(']', '')    
    return stg
  if message.content.startswith('.dict'):
    try :
      b.embeds = []
      msg= message.content
      mesg = msg[6:]
      app_id = "c6cda02a"
      app_key = "2ecbb3e71e167ce2eceaaa7e20e00b4c"
      language = "en"
      word_id = mesg
      url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
      r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
      # url = 'https://dictionaryapi.com/products/json'
      # prms = {"term" : mesg};
      # res = requests.get(url, params = prms);
      
      # print("code {}\n".format(r.status_code))
      # print("text \n" + r.text)
      print("json \n" + json.dumps(r.json()))
      defs = r.json()
      for i in range (len(defs['list'])):
        embed=discord.Embed(title=f"Meaning of {mesg}", color=discord.Color.dark_grey())
        # embed.add_field(name="Definition", value=f"```{rmbc(defs['list'][i]['definitions'])}```", inline=False)
        # embed.add_field(name="Example", value=f"```{rmbc(defs['list'][i]['example'])}```", inline=False)
        # embed.add_field(name="Link", value=rmbc(defs['list'][i]['permalink']), inline=False)
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
      if(message.author.id==777840921227689984) :
        await message.reply('Sir Viper, Kindly ensure that wheather u have typed correct word or not.')
      else :
        await message.reply('No such word exists....Get Some Help ASAP!')
  if not message.author.bot :
        if discord.Status.online==message.author.status :
          results=coll.find({})
          for result in results :
              if(result["member"]==f'{message.author}') :
                coll.delete_one({"member" : f'{message.author}'})
        if discord.Status.idle==message.author.status:
              flag=0
              results=coll.find({})
              for result in results :
                if(result["member"]==f'{message.author}') :
                  flag=1
                  break
              if(flag==0 and  f'{message.author}'!='._.braindead._.#5109') :
                coll.insert_one({"member" : f'{message.author}'})
                await message.reply('Congo U have been added to SFF :), Type .show to see the list')
            
        if discord.Status.dnd==message.author.status:
              f=0
              results=coll.find({})
              for result in results :
                if(result["member"]==f'{message.author}') :
                  f=1
                  break
              if(f==0 and  f'{message.author}'!='._.braindead._.#5109') :
                coll.insert_one({"member" : f'{message.author}'})
                await message.reply('Congo U have been added to SFF :), Type .show to see the list')
              await message.reply("U are in **DND** now, u shouldn't be getting disturbed ryt? :)")

        if discord.Status.offline==message.author.status :
              fl=0
              results=coll.find({})
              for result in results :
                if(result["member"]==f'{message.author}') :
                  fl=1
                  break
              if(fl==0 and  f'{message.author}'!='._.braindead._.#5109') :
                coll.insert_one({"member" : f'{message.author}'})
                await message.reply('Congo U have been added to SFF :), Type .show to see the list')
              await message.reply("U are **Offline** now, how the hell r u texting :(")
  if message.content.startswith('.show') :
    cnt=1
    a=[]
    embed=discord.Embed(title="Status Faking Freaks",color=Colour.dark_grey())
    a.append('```')
    results=coll.find({})
    for result in results :
      if cnt<10 :
        a.append(f'{cnt}.  {result["member"][:len(result["member"])-5]}')
      else :
        a.append(f'{cnt}. {result["member"][:len(result["member"])-5]}')
      cnt+=1
    a.append('```')
    separator="\n"
    embed.description=separator.join(map(str,a))
    await message.reply(embed=embed)
    a.clear()

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
      #print("json \n" + json.dumps(res.json()))
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
      if(message.author.id==777840921227689984) :
        await message.reply('Sir Viper, Kindly ensure that wheather u have typed correct word or not.')
      else :
        await message.reply('No such word exists....Get Some Help ASAP!')
        print(message.author.id)
  if message.content.startswith('.tt') :
    await message.reply(file=discord.File('images/timetablenew.png'))
  if message.content.startswith('.al') :
    await message.reply(file=discord.File('images/almanac.png'))
  if message.content.startswith('.ex') :
    await message.reply(file=discord.File('images/exam.png'))
  if message.content.startswith('.scq') :
    await message.reply('**Scheduled Quiz Dates in November**\n```OOP  - 17\nCA   - 11\nM3   - 20\nADSA - 15\nDBMS - 16```')
  if message.content.startswith('.yayy') :
    await message.delete()
  if message.content.startswith('.heyy') :
    await message.delete()
  if message.content.startswith('.porz') :
    await message.delete()
  if ( message.content=='<@!872480069430431794>') :
    embed=discord.Embed(title=f"Help Menu For {message.author}", color=discord.Color.dark_grey())
    embed.add_field(name="View Help Menu", value='``` Mention The Bot```',inline =True)
    embed.add_field(name="View Meaning of a Word", value='```   $dict word```',inline = True)
    embed.add_field(name="View SFF's List", value='```   .show```',inline = True)
    embed.add_field(name='Basic Commands',value='```.al  --> View Almanac\n\n.tt  --> View TimeTable\n\n.ex  --> View End-Sem-Exam Schedule\n\n.scq --> View Dates of Scheduled Quiz```',inline=False)
    embed.add_field(name="Change Your NickName", value='```Ex: .nick retard ```',inline = True)
    embed.add_field(name="Reset Your NickName", value='```   .nickreset ```',inline = True)
    embed.add_field(name="Upcoming Command", value='``` ```',inline =True)


    await message.reply(embed=embed)
  await b.process_commands(message)

keep_alive()
b.run()
