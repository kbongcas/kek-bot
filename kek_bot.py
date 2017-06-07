import discord
from discord.ext.commands import Bot
import clientDetails
import urllib.request, json
import poll_runner
import poll
import threading

#bot setup 
kek_bot = Bot(command_prefix="!")

@kek_bot.event
async def on_ready():
    print("Client logged in")
    print(kek_bot.user.name)
    print(kek_bot.user.id)
    print('---------')

@kek_bot.command() 
async def helpme():
    return await kek_bot.say("Its all ogre now")

#@kek_bot.command()
#async def somebody():
#
#    voiceChannel = kek_bot.get_channel("314772019545767949")
#    if voiceChannel is None:
#        print("Channel not present")
#        return None
#    await kek_bot.join_voice_channel(voiceChannel)
#   print("has joined a voice channel" + kek_bot.user.name)

@kek_bot.command()
async def pollstart():
    string2parse = "Did I just make a python program?|yah|notreally|sure|imreaddy"
    poll1 = poll.Poll()
    poll1.create_poll(string2parse)

    t = threading.Thread(target=poll_runner.split, args=())
    t.start()
    poll1.vote("kevin","1")
    t.join()
    poll1.close_poll()
    await kek_bot.say(poll1.find_winners())

kek_bot.run(clientDetails.BOT_TOKEN)
        


