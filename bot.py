# bot.py or main.py

from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from start_logic import start
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a function to handle inline button callbacks
def button(update, context):
    query = update.callback_query
    query.answer()

    # Delete the character selection menu message
    context.bot.delete_message(chat_id=query.message.chat_id, message_id=query.message.message_id)

    # Handle the user's choice of character
    if query.data == 'piccolo':
        query.message.reply_text("You have chosen Piccolo as your character.")
    elif query.data == 'future trunks':
        query.message.reply_text("You have chosen Future Trunks as your character.")

def main():
    # Create an Updater object and pass in your bot's token
    updater = Updater("7146430123:AAGoNlsZdiJAqWFixZCNFMTItbpxQQ0Vvo0", use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register callback query handler
    dp.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
