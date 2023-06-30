import logging
from telegram import ReplyKeyboardRemove, Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
import chatgpt

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
        chatgpt.bot(update.message.text),
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