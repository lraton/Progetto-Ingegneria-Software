#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.

"""
First, a few callback functions are defined. Then, those functions are passed to
the Application and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Example of a bot-user conversation using ConversationHandler.
Send /start to initiate the conversation.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 5):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Ciao sono un bot creato per aiutarti attraverso la potenza di chatgpt"
        "Invia /stop per smettere di conversare con me.\n\n"
        "Come posso aiutarti?",
        reply_markup=ReplyKeyboardRemove(),
    )

    return message


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Stores the selected gender and asks for a photo."""
    user = update.message.from_user
    logger.info("Messaggio di %s: %s", user.first_name, update.message.text)
    await update.message.reply_text(
        "Questa sara' la risposta del bot",
        reply_markup=ReplyKeyboardRemove(),
    )

    return message

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s ha fermato la conversazione.", user.first_name)
    await update.message.reply_text(
        "Arrivederci! Spero di essere stato utile", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s ha chiesto aiuto.", user.first_name)
    await update.message.reply_text(
        "Comando help", reply_markup=ReplyKeyboardRemove()
    )


def main() -> None:
    """Run the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("6173029265:AAE70Cm56_mIf0PUGlQkN0mQr-LAQ60Tnjc").build()

    # Add conversation handler with the states GENDER, PHOTO, LOCATION and BIO
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            message: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, message)],
        },
        fallbacks=[CommandHandler("stop", stop),CommandHandler("help", help)],
    )

    application.add_handler(conv_handler)

    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    main()