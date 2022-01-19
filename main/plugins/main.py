import re
from telethon import events

from .. import client
from .. import bot as Drone

from main.plugins.get_msg import get_msg

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False
    
@Drone.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def m(event):
    link = get_link(event.text)
    if not link:
        return
    if 't.me' in link:
        try:
            msg = await get_msg(client, link)
        except Exception as e:
            await event.reply(f'Error: `{str(e)}`')
        await event.client.send_message(event.chat_id, msg) 