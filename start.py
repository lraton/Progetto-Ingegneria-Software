import json
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

with open("secrets.json") as f:
    secrets = json.load(f)
    api_key = secrets["api_telegram_key"]

messages = []

#Handler per avviare il bot 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    messages.append(
        {"role": "system", "content": "Sei un assistente che funziona su un bot telegram e deve rispondere ad ogni frase ricevuta. Ti comporterai come se fossi un essere umano. Sei stato creato per il progetto di Ingegneria del software 2022/2023 da Filippo Notari. Il tuo nome è IngBot"}
    )
    await update.message.reply_text(
        "Ciao sono un bot creato per aiutarti attraverso la potenza di chatgpt"
        "Invia /stop per smettere di conversare con me.\n\n"
        "Come posso aiutarti?",
        reply_markup=ReplyKeyboardRemove(),
    )

    return message

#Handler per i messaggi ricevuti
async def message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("Messaggio di %s: %s", user.first_name, update.message.text)
    
    messages.append({"role": "user", "content": update.message.text})
    new_message = chatgpt.get_response(messages=messages)
    messages.append(new_message)
    print(messages)

    await update.message.reply_text(
        new_message['content'],
        reply_markup=ReplyKeyboardRemove(),
    )

    return message

#Handler per fermare la chat
async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logger.info("User %s ha fermato la conversazione.", user.first_name)

    messages.clear()

    await update.message.reply_text(
        "Arrivederci! Spero di essere stato utile", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

#Handler per il comando aiuto
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user = update.message.from_user
    logger.info("User %s ha chiesto aiuto.", user.first_name)
    await update.message.reply_text(
        "Per usare il bot usa il comando /start, una volta avviato puoi fare qualsiasi domanda, quando hai finito usa /stop", reply_markup=ReplyKeyboardRemove()
    )

#Main
def main() -> None:
    application = Application.builder().token(api_key).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            message: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, message)],
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    application.add_handler(conv_handler)
    application.add_handler(CommandHandler("help", help))
    application.run_polling()

if __name__ == "__main__":
    main()