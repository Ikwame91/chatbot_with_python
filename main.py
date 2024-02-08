from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes




TOKEN: Final ="6547895565:AAEWbMIewlKZ1-xg5LeDu-W8twAW38D3yYY"
BOT_USERNAME: Final = "@ikwame_bot"


#comments
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text("Hello! Thanks for Chattting with me! I am ikwame's bot")


async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text(" I am ikwame and Im ready to provide you with any lesropic divop")


async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await Update.message.reply_text("type your preferred command and I'm ready to execute")

#_Responses

def handle_response(text: str)-> str:
    processed: str = text.lower()

    if "hello" in processed:
        return "Hey How can I assist you"
    
    if "how are you" in processed:
        return "I am Good"
    
    if "I love python" in processed:
        return "The recommended begog is below \n don't forget to subscribe"
    
    return " Can't Understand you properly please come again"


async def handle_message(update:Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text : str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response : str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update:Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting bot.......')
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #H Errors
    app.add_error_handler(error)


    #polls the bot
    print("Polling")
    app.run_polling(poll_interval=3)

    

