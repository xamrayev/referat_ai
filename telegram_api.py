import telebot
from ai_surov import gpt_surov
from doc_creator import doc_creator
from io import BytesIO
from dotenv import dotenv_values
from users_functions import new_user

config = dotenv_values(".env")

bot = telebot.TeleBot(config["TELEGRAM_API"])


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	user_id = message.from_user.id  # Get the user's ID
	bot.reply_to(message, f"Your user ID is {user_id}")

	# bot.replyto(message, "Referat mavzusini kiriting")

@bot.message_handler(commands=['yarat'])
def doc_yarat(message):
	user_id = message.from_user.id
	new_user(user_input=user_id)
	bot.reply_to(message, "Sizga 5 ta limit ajratildi")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	referat_mavzusi=message.text
	referat_izoh = gpt_surov(referat_mavzusi)
	print("1-bosqich")
	doc_creator(referat_mavzusi, referat_izoh)
	doc=open("./generated_doc.docx", "rb")
	print("2-bosqich")
	bot.send_document(message.chat.id, doc)
	print("tugadi")

bot.infinity_polling()