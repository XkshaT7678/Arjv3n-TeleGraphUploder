#Akay MADE BY @AKBORANA1 AND HELP BAHUT LOGO NE KI HAI THNX TO ALL 
import os
from telegraph import upload_file
import pyrogram
from pyrogram import filters, Client
from sample_config import Config
from pyrogram.types import (
    InlineQueryResultArticle, InputTextMessageContent,
    InlineKeyboardMarkup, InlineKeyboardButton,
    CallbackQuery, InlineQuery)

Tgraph = Client(
   "Telegra.ph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)

@Tgraph.on_message(filters.photo)
async def uploadphoto(client, message):
  msg = await message.reply_text("`Wait plz akay server RAVAN download the photo😎⚡`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`RAVAN HAVE DOWNLOADED THE PHOTO🥳🥳, sending Akay server to u ⚡`")
  try:
    tlink = upload_file(img_path)
  except:
    await msg.edit_text("`somthing went wrong akay server slow please try again`") 
  else:
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
    os.remove(img_path) 

@Tgraph.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("`WAIT AND tab tak @akborana ko join kr lo`")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("`OH GIF Ravan Sending😎 Plz wait 😂⚡`")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Yrr kuch galt hai ya Akay server me problem hai please tty again any questions ask @akborana1😔") 
  else:
    await message.reply_text("Yrr it's too big file 5mb se kam de dena 😎 ")

@Tgraph.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`r͛u͛k͛o͛ z͛a͛r͛a͛ s͛a͛b͛a͛r͛ k͛a͛r͛o͛😂😂😂`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`tu bhi kya yaad krega Ravan tere liye bhej rha😂`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Please ask @Akborana1 yrr kuch galt hai😶") 
  else:
    await message.reply_text("Size Should Be Less Than 5 mb😶😑")

@Tgraph.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/akborana'),
        InlineKeyboardButton('⚡D̸E̸V͎E͎L͢O͢P̶E̶R̶⚡ ', url='https://t.me/akborana1')],
    [
	  InlineKeyboardButton('REPO', url=' https://github.com/akborana/RAVAN-TELEGRAPH')]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>Hello I am  RAVAN 😈😉,
        
a telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to Telegraph
        
Made BY ⚡😎  @AKBORANA1  """,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )

@Tgraph.on_message(filters.command(["help"]))
async def help(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/akborana'),
        InlineKeyboardButton('REPO', url=' https://github.com/akborana/RAVAN-TELEGRAPH')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""⚡⚡⚡⚡⚡
        
 BHAI MUJHE PLZ YAAR 5MB KA NICHE ,GIF YA PHOTO YA VID SEND KARNA OK MERE pro master @akborana1 K?😊⚡

i'll upload it to telegra.ph and give you the direct link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Tgraph.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(Tgraph, update.message)
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.delete()
        await home(Tgraph, update.message)

Tgraph.run()

