import os
import discord
from discord import channel
from discord.ext import commands
from discord.message import MessageReference
from discord_components import Button, Select, SelectOption, ComponentsBot, DiscordComponents
from webserver import keep_alive
from discord_buttons_plugin import *
import asyncio
import dnspy
import time
import _thread
import datetime
from pip._vendor import requests
from math import floor
import flask
from discord.colour import Colour
# from discord_buttons_plugin import *
import random
b = commands.Bot(command_prefix='.',intents=discord.Intents.all())
buttons = ButtonsClient(b)
reminder=[]
from pymongo import MongoClient
c = discord.Client()
from wordnik import *
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'l7s5ukux5iy7i5qprh4b348xcr8tymlbvy2f7ysepcno637il'
client = swagger.ApiClient(apiKey, apiUrl)
a=[]
rem=[]
# import io
# import pytesseract
#import opencv
# import numpy as np
# from PIL import Image
import json
from PIL import Image
from PIL import ImageFilter

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

cluster=MongoClient("mongodb+srv://GoViper:GoViper#123@bot-cluster.qe1ds.mongodb.net/test?retryWrites=true&w=majority")
db=cluster["test"]
coll=db["current"]
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


# async def change_nickname() :
#   await asyncio.sleep(5)
#   amanbot =await guild.fetch_member(788616065042219031)
#   while not b.is_closed() :
#       names=["goddessofchaos"]
#       s= random.choice(names)
#       print('changed')
#       await amanbot.edit(nick=s)
#       await asyncio.sleep(5)


# b.loop.create_task(change_nickname())
   


async def change() :
  while not b.is_closed() :
      await buttons.send(
        content = "**Vote to Support**",
        channel = "850060723747815425",
        components = [
          ActionRow([
            Button(
              style = ButtonType().Link,
              label = "Vote RB",
              url = f"https://top.gg/bot/873590828986171423/vote"
            ),
            Button(
              style = ButtonType().Link,
              label = "Vote VS",
              url = f"https://top.gg/bot/850639416669110272/vote"
            )
          ])
        ]
      )
      await asyncio.sleep(3*60*60)
      print('Sent!')


b.loop.create_task(change())
  



@b.command()
async def funny(ctx, m : discord.Member) :
  try :
    await ctx.reply(file=discord.File(f'images/{m.id}.png'))
  except :
    await ctx.reply('Get Rekt!, No Funny moment recorded')


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
  async def threading():
    if(1):
      total_seconds_wait=5
      fg=0
      flag=0
      while total_seconds_wait:
        results=coll.find({})
        for result in results :
            if(floor(time.time())>=result["current"]+6*60*60):
                asyncio.run_coroutine_threadsafe(b.get_channel(850060723747815425).send("vote"), c.loop).result()
                coll.update_one(
                    {"gg": 1},
                        {
                              "$set":{
                                      "current": floor(time.time())
                                    }
                        }
                    )
                print('Sent!')
        if(fg==0):
            now = floor(time.time())
            fg=1
        if(now+1<=floor(time.time())):
            fg=0
            total_seconds_wait-=1
        if(total_seconds_wait==0):
            total_seconds_wait=5
  def between_callback():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(threading())
    loop.close()
  _thread.start_new_thread(between_callback,())


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




def get_string(imageLink):
    pytesseract.pytesseract.tesseract_cmd = 'pytesseract.exe'
    response = requests.get(imageLink)
    img = Image.open(io.BytesIO(response.content))
    text = pytesseract.image_to_string(img)
    return text



@b.event
async def on_message(message) : 
  if(message.content=="vote") :
      embed=discord.Embed(title="Vote to Support",color=discord.Color.dark_grey())
      embed.description="**`|`Reminder Bot**`|`**VS Code Bot`|`**"
      # embed.add_field(name="RB",value="```Reminder Bot```",inline=True)
      # embed.add_field(name="VS",value="```VS Code Bot```",inline=True)
      await buttons.send(
        channel = message.channel.id,
        embed=embed,
        components = [
          ActionRow([
            Button(
              style = ButtonType().Link,
              label = "Vote RB",
              url = f"https://top.gg/bot/873590828986171423/vote"
            ),
            Button(
              style = ButtonType().Link,
              label = "Vote VS",
              url = f"https://top.gg/bot/850639416669110272/vote"
            )
          ])
        ]
      )
  if message.content=="vote" :
    await message.delete()
  # if message.attachments and message.content.startswith('.ocr'):
  #     try :
  #           link = message.attachments[0].url
  #           content = get_string(link)
  #           await message.reply(content)
  #     except :
  #        await message.reply('Not Convertable!')
  # def rmbc(stg):
  #   stg = stg.replace('[', '')
  #   stg = stg.replace(']', '')    
  #   return stg
  # if message.content.startswith('test'):
  #   try :
  #     b.embeds = []
  #     mesg = viper
  #     app_id = "c6cda02a"
  #     app_key = "2ecbb3e71e167ce2eceaaa7e20e00b4c"
  #     language = "en"
  #     word_id = mesg
  #     url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
  #     r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
  #     # url = 'https://dictionaryapi.com/products/json'
  #     # prms = {"term" : mesg};
  #     # res = requests.get(url, params = prms);
      
  #     # print("code {}\n".format(r.status_code))
  #     # print("text \n" + r.text)
  #     print("json \n" + json.dumps(r.json()))
  #     defs = r.json()
  #     for i in range (len(defs['list'])):
  #       embed=discord.Embed(title=f"Meaning of {mesg}", color=discord.Color.dark_grey())
  #       # embed.add_field(name="Definition", value=f"```{rmbc(defs['list'][i]['definitions'])}```", inline=False)
  #       # embed.add_field(name="Example", value=f"```{rmbc(defs['list'][i]['example'])}```", inline=False)
  #       # embed.add_field(name="Link", value=rmbc(defs['list'][i]['permalink']), inline=False)
  #       b.embeds.append(embed);
  #     buttons = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] 
  #     current = 0
      
    
  #     for button in buttons:
  #       await msg.add_reaction(button)
        
  #     while True:
  #       try:
  #           reaction, user = await b.wait_for("reaction_add", check=lambda reaction, user: user == message.author and reaction.emoji in buttons, timeout=None)

  #       except asyncio.TimeoutError:
  #           return print("test")

  #       else:
  #           previous_page = current        
  #           if reaction.emoji == u"\u23EA":
  #               current = 0
                
  #           elif reaction.emoji == u"\u2B05":
  #               if current > 0:
  #                   current -= 1
                    
  #           elif reaction.emoji == u"\u27A1":
  #               if current < len(b.embeds)-1:
  #                   current += 1

  #           elif reaction.emoji == u"\u23E9":
  #               current = len(b.embeds)-1

  #           for button in buttons:
  #               await msg.remove_reaction(button, message.author)

  #           if current != previous_page:
  #               await msg.edit(embed=b.embeds[current])
  #   except :
  #     if(message.author.id==777840921227689984) :
  #       await message.reply('Sir Viper, Kindly ensure that wheather u have typed correct word or not.')
  #     else :
  #       await message.reply('No such word exists....Get Some Help ASAP!')
  # if message.author.bot :
  #       if discord.Status.online==message.author.status :
  #         results=coll.find({})
  #         for result in results :
  #             if(result["member"]==f'{message.author}') :
  #               coll.delete_one({"member" : f'{message.author}'})
  #       if discord.Status.idle==message.author.status:
  #             flag=0
  #             results=coll.find({})
  #             for result in results :
  #               if(result["member"]==f'{message.author}') :
  #                 flag=1
  #                 break
  #             if(flag==0 and  f'{message.author}'!='._.braindead._.#5109') :
  #               coll.insert_one({"member" : f'{message.author}'})
  #               await message.reply('Congo U have been added to SFF :), Type .show to see the list')
            
  #       if discord.Status.dnd==message.author.status:
  #             f=0
  #             results=coll.find({})
  #             for result in results :
  #               if(result["member"]==f'{message.author}') :
  #                 f=1
  #                 break
  #             if(f==0 and  f'{message.author}'!='._.braindead._.#5109') :
  #               coll.insert_one({"member" : f'{message.author}'})
  #               await message.reply('Congo U have been added to SFF :), Type .show to see the list')
  #             await message.reply("U are in **DND** now, u shouldn't be getting disturbed ryt? :)")

  #       if discord.Status.offline==message.author.status :
  #             fl=0
  #             results=coll.find({})
  #             for result in results :
  #               if(result["member"]==f'{message.author}') :
  #                 fl=1
  #                 break
  #             if(fl==0 and  f'{message.author}'!='._.braindead._.#5109') :
  #               coll.insert_one({"member" : f'{message.author}'})
  #               await message.reply('Congo U have been added to SFF :), Type .show to see the list')
  #             await message.reply("U are **Offline** now, how the hell r u texting :(")
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
      button = [u"\u23EA", u"\u2B05", u"\u27A1", u"\u23E9"] 
      current = 0
      msg = await message.reply(embed=b.embeds[current])
      #     components = [
      #     #  ActionRow([
      #       Button(
      #         label = "First",
      #         custom_id = "First",

      #       ),

      #       Button(
      #         label = "Previous",
      #         custom_id = "Previous"

      #       )
      #     #   Button(
      #     #     label = "Next",
      #     #     custom_id = "Next",
      #     #   ),
      #     #   Button(
      #     #     label = "Last",
      #     #     custom_id = "Last",
      #     #   )
      #     #  ])
      #      ]
      #     )
      # except :
      #   print('error')
      for butt in button:
        await msg.add_reaction(butt)
        
      while True:
        try:
            reaction, user = await b.wait_for("reaction_add", check=lambda reaction, user: user == message.author and reaction.emoji in button, timeout=None)
            # interaction = await b.wait_for("button_click", check=lambda inter: inter.custom_id == "button1")
            

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

           




            elif reaction.emoji == u"\u23E9" :
               current = len(b.embeds)-1
        
            
            
	             


            for butt in button:
                await msg.remove_reaction(butt, message.author)

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
    embed.add_field(name="View SFF's List", value='```  .show```',inline = True)
    embed.add_field(name="Vote to Support", value='```   vote```',inline =True)
    embed.add_field(name="View Funny Moments", value='```ex: .funny @retard```',inline =True)
    embed.add_field(name="View Meaning of a Word", value='```    $dict word```',inline = True)
    embed.add_field(name='Basic Commands',value='```.al  --> View Almanac\n\n.tt  --> View TimeTable\n\n.ex  --> View End-Sem-Exam Schedule\n\n.scq --> View Dates of Scheduled Quiz```',inline=False)
    embed.add_field(name="Change Your NickName", value='```Ex: .nick retard ```',inline = True)
    embed.add_field(name="Reset Your NickName", value='```   .nickreset ```',inline = True)


    await message.reply(embed=embed)
  await b.process_commands(message)

def rmbc(stg):
    stg = stg.replace('[', '')
    stg = stg.replace(']', '')    
    return stg

@b.command()
async def dict(ctx, word) :
      b.embeds = []
      current=0
      mesg = word
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
      msg=await ctx.send(embed=b.embeds[current],
      
      components = [[
        Button(
          label = "First",
          custom_id = "First",
        ),
        Button(
          label = "Previous",
          custom_id = "Previous"
        ),
        Button(
          label = "Next",
          custom_id = "Next",
        ),
        Button(
          label = "Last",
          custom_id = "Last",
         
        )
        ]]
      )
 
  # while True :
    
  #   interaction1 = await b.wait_for("button_click", check=lambda inter: inter.custom_id == "Last")
    
  #   async def button_callback(interaction1) :
  #       current=len(b.embeds)-1
  #       await interaction1.response.edit_message(embed=b.embeds[current])

  #   button.call
    

           
# @buttons.click
# async def First(ctx):
#     current = 0
    

# @buttons.click
# async def Previous(ctx):
#               if current > 0:
#                     current -= 1




# @buttons.click
# async def Next(ctx):
#                if current < len(b.embeds)-1:
#                     current += 1




# @b.command()
# async def button(ctx):
#     await ctx.send("Buttons!", components=[Button(label="Button", custom_id="button1")])
  


# @buttons.click
# async def Last(ctx):
#                current = len(b.embeds)-1


# @b.event
# async def on_button_click(interaction):
#     current=

keep_alive()
b.run('ODcyNDgwMDY5NDMwNDMxNzk0.YQqeYg.BrNI68Hbpi2-PD2_07xMeX1MMBo')
