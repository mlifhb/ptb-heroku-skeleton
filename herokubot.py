import logging
import os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="در حال ارسال پیام هستید:")

    user = update.effective_chat.id in users
    if not user:
      users.append(update.effective_chat.id)
      user_active_button.append(0)
    if user_active_button[users.index(update.effective_chat.id)] != -1:
      user_active_button[users.index(update.effective_chat.id)]=1


def echo(update, context):
    update.effective_message.reply_text(update.effective_message.text)


if __name__ == "__main__":
    users=[]
    group = ['-1001697966543']
    user_active_button = []
    admins = [-1001697966543]
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
    # Add handlers
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the webhook
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN,
                          webhook_url=f"https://{NAME}.herokuapp.com/{TOKEN}")
    updater.idle()
