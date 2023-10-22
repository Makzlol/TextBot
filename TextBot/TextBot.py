import types
import telebot, os, datetime

from logging import basicConfig, INFO, Logger
from dotenv import load_dotenv
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage

load_dotenv()
dir_logs = 'logs/'
name_current_logs = f'{datetime.datetime.now().date()}'
logs_format = '.txt'
logger = Logger('Bot', INFO)
bot = telebot.TeleBot(os.getenv('SECRET'))
button_text_reg_log = 'Регистрация/Вход'
state_storage = StateMemoryStorage()
Start_text = f'Приветствую тебя в команде писальщиков текстов, -name-\n\n'
			 
class Change:
	NAME = '-name-'

class States(StatesGroup):
	Register = State()
	Login = State()
	Start = State()

if not os.path.exists(f'{dir_logs}{name_current_logs}{logs_format}'):
	basicConfig(filemode='w', filename=f'{name_current_logs}{logs_format}', level=INFO)
else:
	basicConfig(filemode='a', filename=f'{name_current_logs}{logs_format}', level=INFO)

start_keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True).add(
	telebot.types.KeyboardButton(
		text=button_text_reg_log
	)
)

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
	bot.send_message(message.chat.id, Start_text.replace(Change.NAME, message.from_user.full_name), reply_markup=start_keyboard)
	bot.set_state(message.from_user.id, States.Start, message.chat.id)
	
bot.add_custom_filter(telebot.custom_filters.StateFilter(bot))
bot.infinity_polling()