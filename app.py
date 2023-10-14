import logging, os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

load_dotenv()
TOKEN = os.getenv('TOKEN')
PORT = int(os.getenv('PORT'))
WEB_HOOK_URL = os.getenv('WEB_HOOK_URL')
USE_WEBHOOK = os.getenv('USE_WEBHOOK') == 'True'

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# respond to /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message ="Hi, i'm a telegram bot, type /test or /whoiam please"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# respond to /test command
async def test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message ="You just typed /test command, and it's working, youpi !"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def whoiam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(str(update))
    message ="you are {0} {1}".format(update.message.from_user.first_name,update.message.from_user.last_name)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

# respond to non command
async def upper_user_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message.text.upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

   

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    verify_handler = CommandHandler('test', test)
    verify_handler = CommandHandler('whoiam', whoiam)
    application.add_handler(start_handler)
    application.add_handler(verify_handler)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, upper_user_message))

    if USE_WEBHOOK:
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=WEB_HOOK_URL
        )
    else:
        application.run_polling()
