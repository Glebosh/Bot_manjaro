import telegram
import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.ext import MessageHandler, Filters
from telegram import InlineQueryResultArticle, InputTextMessageContent

TOKEN = '5484155734:AAELvAPIUJ7SSItY00aVn8226KFQZZrQJsE'

PEPE = (f'⢠⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠬⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠬⠬⠭⠥⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⡄\n'
f'⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠶⢶⣤⠀⠀⣷⡆⠀⢀⣴⠖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇\n'
f'⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⠈⣷⠀⢸⣇⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷\n'
f'⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠀⠀⠀⠀⣿⠀⢸⡟⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n'
f'⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠿⣄⣀⣠⡾⠃⠀⣼⡇⠀⠈⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n'
f'⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n'
f'⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿\n'
f'⣿⠀⠀⣿⡛⣛⠛⢳⡤⠀⣠⡾⠛⠛⠻⣦⡀⠀⣰⠞⠛⠛⠳⣄⠀⠀⡿⡇⠀⠀⢀⣾⡇⠀⢸⠛⠛⠛⠛⠃⣤⣿⠛⠛⠛⠳⡄⠀⠀⡧\n'
f'⣿⠀⠀⣿⣧⣯⣤⣾⠁⠀⡏⠀⠀⠀⠀⠘⣗⢸⡇⠀⠀⠀⠀⠘⡆⠀⡇⢹⡄⠀⣼⢹⡇⠀⢸⣦⣤⣤⣥⠄⠘⣿⣀⣀⣀⣴⠇⠀⠀⡗\n'
f'⣿⠀⠀⣿⡀⠀⠀⠙⡏⠀⣧⡀⠀⠀⠀⣸⡏⠘⣧⠀⠀⠀⠀⣸⠇⠀⡇⠈⣷⣸⠇⢸⡇⠀⢸⠀⠀⠀⠀⠀⠀⣿⠉⠙⠻⣅⠀⠀⠀⣿\n'
f'⣿⠀⠀⠻⠷⣶⠶⠚⠁⠀⠈⠛⠶⠶⠞⠋⠀⠀⠈⠓⠶⠶⠞⠁⠀⠀⠇⠀⠸⠟⠀⢸⡇⠀⠸⡶⠶⠶⠶⠦⠀⠿⠀⠀⠀⠘⠷⡄⠀⣿\n'
f'⣿⢤⣦⣤⣴⣶⣶⣶⣶⣶⣶⣶⣦⣤⣴⣦⣤⣤⣤⣤⣤⣤⣴⣤⣤⣤⣤⣶⣶⣦⣶⣤⣦⡴⣤⣶⣶⠶⣶⣶⣦⣤⣤⣤⣤⣤⣦⣴⣤⡿\n'
f'⠃⠀⠀⠀⠀⠀⣽⢿⡟⠀⣼⡟⣡⣾⡯⠿⠛⠛⠻⢯⣍⡁⢀⣩⠟⣫⡥⠿⠷⠿⠿⣌⡻⣟⣿⣭⡿⢷⣄⠈⠻⣮⣷⡀⠀⠀⠀⠀⠀⠀\n'
f'⡇⠀⠀⠀⠀⢰⣿⣿⠀⢰⣏⣼⣻⡵⠟⠉⢀⣈⣉⣛⣶⣬⣿⠾⠋⢀⣀⣠⡤⣤⣤⣤⠿⣾⣿⣷⣙⠷⣝⢷⡀⠸⣞⣧⠀⠀⠀⠀⠀⠀\n'
f'⡇⠀⠀⠀⠀⠈⡿⣿⠀⣿⣶⠟⠋⣠⠴⠚⠋⠁⠀⠀⢉⣻⡿⠀⠞⠋⢉⣴⠿⠋⣉⡤⢤⣶⡿⠿⠽⣷⡜⣧⣷⠀⣿⣼⠄⠀⠀⠀⠀⠀\n'
f'⡃⠀⠀⠀⠀⠀⡇⣿⠀⣿⡇⠀⠀⠁⠀⠀⠀⣠⣴⣾⣿⣍⣉⣶⠶⠶⠯⣅⣠⠾⠋⣿⣟⣿⢿⣦⡀⠀⢹⡼⣿⠀⣿⣿⠀⠀⠀⠀⠀⠀\n'
f'⠇⠀⠀⠀⠀⠀⡇⣿⡁⣿⡇⠀⠀⢀⣠⡴⢛⣽⠞⢡⣞⣹⡿⠻⣧⡄⠀⡾⠁⠀⠀⣿⣿⢿⣶⣿⣧⣤⣾⣷⡟⠀⢸⢸⠀⠀⠀⠀⠀⠀\n'
f'⠁⠀⠀⠀⠀⠀⡇⣿⡁⣿⣇⠀⠀⠋⠉⢾⣏⠀⠀⢸⣿⣏⣿⣿⣿⣧⡴⠛⠦⠤⠴⠿⠛⠛⠋⣉⣽⣿⣿⢻⡇⠀⢸⢸⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⡇⣿⠀⢸⣿⠀⠀⢀⣠⣤⣬⣽⣶⣶⣿⣟⡛⠉⣉⣀⣀⣀⣀⣀⣀⣤⣴⣶⠾⠋⢁⣼⣿⣿⠀⠀⢸⣸⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⡇⣿⠀⠘⣿⡆⢸⣟⠁⠠⣤⣤⣌⣉⡉⠉⠉⠉⠉⠉⠉⠉⣉⣉⣭⣥⣤⣶⠶⠚⢻⡿⣷⡟⠀⠀⣾⢻⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⡇⣿⠀⠀⢿⣇⠀⠙⠻⠷⣶⣤⣄⣈⣉⡉⠉⠉⠉⠉⢉⣹⣉⣋⣁⣀⣤⣤⣴⠾⢿⡿⠋⠀⠀⣰⢯⠟⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⣇⣿⠀⠀⠘⣿⣧⣄⡀⠀⠀⠀⠀⠀⠉⠉⠛⠛⠛⠛⠛⠉⠉⠉⠀⠀⢀⣀⣠⣶⣿⣄⣀⡴⢞⡡⠋⠀⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⠹⣟⣧⡀⠀⠘⢿⣟⠿⢶⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣴⡾⠿⠛⠉⠈⣿⣿⢻⡖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⠀⢹⣿⣷⣄⠀⢀⣿⠀⠀⠈⠉⠛⠛⠛⠛⠛⠛⠹⠋⠁⠀⠉⠈⠀⠀⠀⠀⠀⠀⠈⢿⣧⣙⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀\n'
f'⠀⠀⠀⠀⠀⠀⠀⡼⣿⡟⠻⣷⣾⣟⠀⠐⠀⠀⠀⣠⣤⣤⣤⣤⣤⣤⣄⣤⣠⡄⣀⣀⣤⣤⣄⠀⠀⠀⢻⣿⣜⡆⠀⠀⠀⠀⠀⠀⠀⠀\n')

# print(PEPE)


#ERROR config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# start handler
def start(update: Update, context: CallbackContext):
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Picture", callback_data='1'),
            InlineKeyboardButton("Text", callback_data='2'),
        ],
        [InlineKeyboardButton("?", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)

    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
    # context.bot.send_message(chat_id=update.effective_chat.id, text='Hello Im bot. GIVE ME YOUR MONEY MOW!')


# echo handler !УБРАНО!
def echo(update: Update, context: CallbackContext):
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


#caps handler
def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


#inline
def inline_caps(update: Update, context: CallbackContext):
    query = update.inline_query.query
    if not query:
        return
    results = []
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Caps',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)

from telegram.ext import InlineQueryHandler


# unkown commands
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")


# Buttons
def button(update: Update, context: CallbackContext):
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == '1':
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
    if query.data == '2':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Hello Im bot. GIVE ME YOUR MONEY MOW!')

    query.edit_message_text(text=f"Selected option: {query.data}")


# Help
def help(update: Update, context: CallbackContext):
    commands = {'start': 'Starts programm with choice', 'caps ...': 'Reply with CAPS text'}

    context.bot.send_message(chat_id=update.effective_chat.id, text='/start: Starts programm with choice; /caps: Reply with CAPS text')


def main():
    bot = telegram.Bot(token=TOKEN)
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    #Start
    dispatcher.add_handler(CommandHandler('start', start))

    #Echo
    echo_handler = MessageHandler(Filters.text & (~Filters.command) | Filters.photo & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    #Caps
    dispatcher.add_handler(CommandHandler('caps', caps))

    #Inline
    dispatcher.add_handler(InlineQueryHandler(inline_caps))

    #Button
    dispatcher.add_handler(CallbackQueryHandler(button))

    #Help
    dispatcher.add_handler(CommandHandler('help', help))

    #Unknown
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    #strat polling
    updater.start_polling()


if __name__ == '__main__':
    main()


# bot.send_photo(chat_id='-705446959', photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
# print(bot.send_message(text='Привет, я робот, который хочет захватить мир!', chat_id='chat_id'))