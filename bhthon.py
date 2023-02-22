from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions
from hijri_converter import Gregorian
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from collections import deque
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from telethon.tl import functions
import time
import asyncio
import logging
import base64
import datetime
from payment import *
from help import *
from config import *
from checktele import *

# -

bhthon.start()

DEVS =[
          5693914475
]


async def join_channel("@alibaashar"):
    try:
        await fifthon(JoinChannelRequest("@bhthon"))
    except BaseException:
        pass
        
        
@bhthon.on.message_handler(commands="\.المطور"
def start(message):
 bot.send_message(message.chat.id.f'''
 https://graph.org/file/fba8925fa68111c916887.mp4
 '''
  )
@bhthon.message_handler(commands=[\.\.الاوامر)
def start(message):
 bot.send_message(message.chat.id,f'''
 اوامر السورس
'''
  )
@bhthon.message_handler(commands=\.فحص)
def start(message):
 bot.send_message(message.chat.id,f'''
 السورس شغال 😄
'''
 )

@bot.message_handler(commands=\.م1
def start(message):
 bot.send_message(message.chat.id,f'''
 المطور - مطور السورس
 اعادة تشغيل = ايقاف الصيد
.حالة الصيد  = وين وصل الصيد؟
.صيد 30000 2 @يوزر قنااتك  = صيد يوزرات
.الانواع = تعرف انواع السورس 

owner_id = 5693914475
@bhthon.on(events.NewMessage(outgoing=False, pattern='/هيا بنا))
async def OwnerStart(event):
    sender = await event.get_sender()
    if sender.id == ownerhson_id :
        order = await event.reply('Ok sir)
        
@bhthon.on(events.NewMessage(outgoing=True, pattern=r"\.اعادة تشغيل"))
async def update(event):
    await event.edit("Ok I will restart the source")
    await bhthon.disconnect()
    await bhthon.send_message("Done!")
