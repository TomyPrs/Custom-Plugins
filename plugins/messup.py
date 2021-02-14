from userge import userge, Message, filters
from userge.utils import runcmd
import os

LOG = userge.getLogger(__name__)  # logger object
CHANNEL = userge.getCLogger(__name__)  # channel logger object

# add command handler
@userge.on_cmd("messup", about="help text to this command")
async def messup(message: Message):
   await message.edit("`messing....")
   reply = message.reply_to_message
   stkr = await reply.download("tgs.tgs")
   await runcmd(f"lottie_convert.py {stkr} json.json")
   os.remove(stkr)
   with open("json.json","r") as json:
       jsn = json.read()      
   jsn = jsn.replace('[1]','[20]').replace('[2]','[30]').replace('[3]','[40]').replace('[4]','[50]').replace('[5]','[60]')
   with open("json.json","w") as outfile:
       outfile.write(jsn)
   await runcmd("lottie_convert.py json.json tgs.tgs")
   await message.client.send_sticker(message.chat.id, "tgs.tgs")
   os.remove("json.json")
   os.remove("tgs.tgs")
   await message.delete()
   
   
   
   
