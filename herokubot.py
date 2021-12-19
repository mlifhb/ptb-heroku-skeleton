import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def start(update, context):
    update.effective_message.reply_text("Hi!")


def command(update,context):
  if update.effective_chat.id in admins:
    base_command = update.message.text
    if "block" in base_command and not "unblock" in base_command:
      id = int(base_command.replace("/block","").replace("@USBcrushbot",""))
      user_active_button[users.index(id)]=-1
      context.bot.send_message(chat_id=group[0], text="بلاک شد. برای آنبلاک کردن:"+"              /unblock"+str(id))
      context.bot.send_message(chat_id = id, text="شما بلاک شدید")
      return
    if "unblock" in base_command:
      id = int(base_command.replace("/unblock","").replace("@USBcrushbot",""))
      user_active_button[users.index(id)]=0
      context.bot.send_message(chat_id=group[0], text="آنبلاک شد. برای بلاک کردن:"+"              /block"+str(id))
      context.bot.send_message(chat_id = id, text="شما آنبلاک شدید")
      return
    #if "send" in base_command:

def text(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    context.bot.send_message(chat_id=group[0], text=update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")


def photo(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['photo'][-1]['file_id']
    Caption = update.message['caption']
    context.bot.sendPhoto(chat_id = group[0],caption = Caption,photo = fileID)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")

def video(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['video']['file_id']
    Caption = update.message['caption']
    context.bot.sendVideo(chat_id = group[0],caption = Caption,video = fileID)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")
def audio(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['audio']['file_id']
    Caption = update.message['caption']
    context.bot.sendAudio(chat_id = group[0],caption = Caption,audio = fileID)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")

def voice(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['voice']['file_id']
    Caption = update.message['caption']
    context.bot.sendVoice(chat_id = group[0],caption = Caption,voice = fileID)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")

def sticker(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['sticker']['file_id']
    #Caption = update.message['caption']
    context.bot.sendSticker(chat_id = group[0],sticker = fileID)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")


def gif(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['animation']['file_id']
    Caption = update.message['caption']
    context.bot.send_animation(chat_id = group[0],animation = fileID,caption = Caption)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")

def video_message(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['video_note']['file_id']
    #Caption = update.message['caption']
    context.bot.sendVideoNote(chat_id = group[0],video_note = fileID)
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")

def document(update, context):
  #id = Message.document.file_id
  if user_active_button[users.index(update.effective_chat.id)]==1:
    context.bot.send_message(chat_id=group[0], text=str(update.effective_chat)+"              /block"+str(update.effective_chat.id))
    fileID = update.message['document']['file_id']
    FileName = update.message['document']['file_name']
    Caption = update.message['caption']
    context.bot.sendDocument(chat_id = group[0],document = fileID,filename = FileName, caption = Caption )
    context.bot.send_message(chat_id=update.effective_chat.id , text="ارسال شد")
    deactive = users.index(update.effective_chat.id)
    user_active_button[deactive] = 0
  elif user_active_button[users.index(update.effective_chat.id)]==-1:
    context.bot.send_message(chat_id=update.effective_chat.id , text="در حال حاضر به علت بلاک بودن امکان ارسال پیام ندارید")
  else:
    context.bot.send_message(chat_id=update.effective_chat.id , text="متوجه نشدم")
    


if __name__ == "__main__":
    # Set these variable to the appropriate values
    TOKEN = "5087750187:AAF3PIit5UxuPa5AZNL1QwHJ6Jm-N0d9skI"
    NAME = "tbhh21"

    # Port is given by Heroku
    PORT = os.environ.get('PORT')

    # Enable logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logger = logging.getLogger(__name__)

    # Set up the Updater
    updater = Updater(TOKEN)
    dp = updater.dispatcher
     start_handler = CommandHandler('start', start)
    text_handler = MessageHandler(Filters.text & (~Filters.command), text)
    photo_handler = MessageHandler(Filters.photo & (~Filters.command), photo)
    video_handler = MessageHandler(Filters.video & (~Filters.command), video)
    audio_handler = MessageHandler(Filters.audio & (~Filters.command), audio)
    voice_handler = MessageHandler(Filters.voice & (~Filters.command), voice)
    sticker_handler = MessageHandler(Filters.sticker & (~Filters.command), sticker)
    gif_handler = MessageHandler(Filters.animation & (~Filters.command), gif)
    document_handler = MessageHandler(Filters.document & (~Filters.command), document)
    videomessage_handler = MessageHandler(Filters.video_note & (~Filters.command),video_message)
    commands = MessageHandler(Filters.command, command)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(text_handler)
    dispatcher.add_handler(photo_handler)
    dispatcher.add_handler(video_handler)
    dispatcher.add_handler(audio_handler)
    dispatcher.add_handler(voice_handler)
    dispatcher.add_handler(sticker_handler)
    dispatcher.add_handler(gif_handler)
    dispatcher.add_handler(document_handler)
    dispatcher.add_handler(videomessage_handler)
    dispatcher.add_handler(commands)

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=f"https://{NAME}.herokuapp.com/{TOKEN}")
    updater.idle()
