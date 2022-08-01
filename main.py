import telegram
import logging
# from PIL import Image
from telegram import __version__ as tg_ver
from telegram.ext import Updater

TOKEN = TOKEN
picture = Image.open('ec9.jpg')
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

print(PEPE)

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher


#ERROR config
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


# start handler
from telegram import Update
from telegram.ext import CallbackContext

def start(update: Update, context: CallbackContext):
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello Im bot. GIVE ME YOUR MONEY MOW!')

from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


# echo handler !УБРАНО!
from telegram.ext import MessageHandler, Filters

def echo(update: Update, context: CallbackContext):
    # context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text & (~Filters.command) | Filters.photo & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)


#caps handler
def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


#inline
from telegram import InlineQueryResultArticle, InputTextMessageContent

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

inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


# unkown commands
def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)


#strat polling
updater.start_polling()

#stop polling
# updater.stop()

# bot.send_photo(chat_id='-705446959', photo=open('/home/glebosh/workspace/tgbot/ec9.jpg', 'rb'))
# print(bot.send_message(text='Привет, я робот, который хочет захватить мир!', chat_id='chat_id'))