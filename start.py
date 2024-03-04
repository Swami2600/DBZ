# start_logic.py

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    """Send a welcome message when the user starts the bot and present a character selection menu."""
    # Retrieve the user's first name
    user_name = update.message.from_user.first_name

    # Welcome the user by name
    update.message.reply_text(f"Welcome, {user_name}!")

    # Create character selection menu with inline buttons
    keyboard = [
        [InlineKeyboardButton("Piccolo", callback_data="You have selected Piccolo")],
        [InlineKeyboardButton("Future Trunks", callback_data="You have selected Future Trunks")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Send the character selection menu to the user
    update.message.reply_text("Please select your character:", reply_markup=reply_markup)
