# Made by ~ @Akki_ThePro
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
  msg = await message.reply_text("`Please wait.., I am Uploading it to my Server, Then I will send you..👨‍💻`")
  userid = str(message.chat.id)
  img_path = (f"./DOWNLOADS/{userid}.jpg")
  img_path = await client.download_media(message=message, file_name=img_path)
  await msg.edit_text("`Got That Photo.., Uploading it to you..🤠`\n Made by ~ @Arjv3n_Projectz")
  try:
    tlink = upload_file(img_path)
    await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
    os.remove(img_path)   
  except:
    await msg.edit_text("**Something Went Wrong** Sorry, My server is Slow.. `Please Try Again Later..!`") 


@Tgraph.on_message(filters.animation)
async def uploadgif(client, message):
  if(message.animation.file_size < 5242880):
    msg = await message.reply_text("**Wait a Minute I am Uploding it to you..!** Until you join @Arjv3n_Projectz")
    userid = str(message.chat.id)
    gif_path = (f"./DOWNLOADS/{userid}.mp4")
    gif_path = await client.download_media(message=message, file_name=gif_path)
    await msg.edit_text("**Ohk I Gif..** I am Uploding.. Join ~ @Arjv3n_Projectz")
    try:
      tlink = upload_file(gif_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")   
      os.remove(gif_path)   
    except:
      await msg.edit_text("Getting **Error** in my server..! Forward this messageto @Arjv3n_ProjectzChat") 
  else:
    await message.reply_text("This file is Too Big.. I need a File upto 5mbps only..!")

@Tgraph.on_message(filters.video)
async def uploadvid(client, message):
  if(message.video.file_size < 5242880):
    msg = await message.reply_text("`Hold on, Wait a Minute..!`")
    userid = str(message.chat.id)
    vid_path = (f"./DOWNLOADS/{userid}.mp4")
    vid_path = await client.download_media(message=message, file_name=vid_path)
    await msg.edit_text("`Remember me Don't forget me..!`")
    try:
      tlink = upload_file(vid_path)
      await msg.edit_text(f"https://telegra.ph{tlink[0]}")     
      os.remove(vid_path)   
    except:
      await msg.edit_text("Please ask @Arjv3n_ProjectzChat") 
  else:
    await message.reply_text("Size Should Be Less Than **5 mb**")

@Tgraph.on_message(filters.command(["start"]))
async def home(client, message):
  buttons = [[
        InlineKeyboardButton('Help', callback_data='help'),
        InlineKeyboardButton('Close', callback_data='close')
    ],
    [
        InlineKeyboardButton('Our Channel', url='http://telegram.me/abkorana'),
        InlineKeyboardButton('Made By↗️', url='https://t.me/Akki_ThePro')
    ],
    [
        InlineKeyboardButton("REPO↗️", url="https://github.com/Akshat7678/Arjv3n-TeleGraphUploder")
    ]]

  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text="""<b>Hello, I Am Arjv3n,
        
A telegraph Uploader That Can Upload Photo, Video And Gif
        
Simply send me photo, video or gif to upload to Telegraph
        
Made By ~ @Akki_ThePro</b>""",
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
        InlineKeyboardButton('Our Channel↗️', url='http://telegram.me/Arjv3n_Projectz'),
        InlineKeyboardButton('REPO↗️', url=' https://github.com/Akshat7678/Arjv3n-TeleGraphUploder')
    ]]
  reply_markup = InlineKeyboardMarkup(buttons)
  await Tgraph.send_message(
        chat_id=message.chat.id,
        text=""" 
      
     Please Send me a Pic/Video/Gif which is **Below 5mb**

I'll upload it to telegra.ph and give you the direct link""",
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=message.message_id
    )                           
@Tgraph.on_callback_query()
async def button(Tgraph, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.edit_text(text="**Send me photo/gif/video to Upload them on telegra.ph**\n\n__My Dev: @Akki_ThePro__")
      elif "close" in cb_data:
        await update.message.delete() 
      elif "home" in cb_data:
        await update.message.edit_text(text="**Send me photo/gif/video to Upload them on telegra.ph**\n\n__My Dev: @Akki_ThePro__")
      

Tgraph.run()

