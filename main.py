from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes
from dotenv import load_dotenv
import os


load_dotenv()

TOKEN = os.getenv("TOKEN")

BOT_USERNAME: Final = "@ikwame_bot"


#comments
async def start_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Thanks for Chattting with me! I am ikwame's bot")


async def help_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Available Commands :-
    /youtube - To get the youtube URL
    /linkedin - To get the LinkedIn profile URL
    /github - To get gmail URL
    /geeks - To get the GeeksforGeeks URL""")


async def custom_command(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("type your preferred command and I'm ready to execute")

#_Responses
async def github_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Github Url => https://github.com/Ikwame91")


async def youtube_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Youtube Link =>https://youtu.be/FMV8pbz0sN8?si=9jZrlLKWrfmioPIU")

async def linkedIn_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")

async def geeks_url(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("GeeksforGeeks URL => https://www.geeksforgeeks.org/")

async def unknown_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)
def handle_response(text: str)-> str:
    processed: str = text.lower()
    if "hi" in processed:
        return "Hi this is Ikwame's bot, How can I assist you?"

    if "hello" in processed:
        return "Hey How can I assist you"
    
    if "how are you" in processed:
        return "I am Good"
    
    if "i love python" in processed:
        return "The recommended code is below don't forget to subscribe"
    
    return " Can't Understand you properly please come again......"


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
    app.add_handler(CommandHandler('linkedin', linkedIn_url))
    app.add_handler(CommandHandler('github', github_url))
    app.add_handler(CommandHandler('geeks', geeks_url))
    app.add_handler(CommandHandler('youtube', youtube_url))
    

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #H Errors
    app.add_error_handler(error)


    #polls the bot
    print("Polling")
    app.run_polling(poll_interval=3)
    

    

