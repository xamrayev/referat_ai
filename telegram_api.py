import telebot
from ai_surov import gpt_surov
from doc_creator import doc_creator
from io import BytesIO
from dotenv import dotenv_values
from users_functions import new_user

config = dotenv_values(".env")

bot = telebot.TeleBot(config["TELEGRAM_API"])

@bot.message_handler(commands=['start'])
def send_welcome(message):
	user_id = message.from_user.id  # Get the user's ID
	user_name = message.from_user.username  # Get the user's name
	bot.send_message(message.chat.id, 
							f"""Assalomu alaykum {user_name}. \n \tXush kelibsiz! 
							🧞 \n \tSizga ✋ ta limit ajratildi.""")



# @bot.message_handler(commands=['yarat'])
# def doc_yarat(message):
# 	user_id = message.from_user.id
# 	new_user(user_input=user_id)
# 	bot.reply_to(message, "Sizga 5 ta limit ajratildi")


@bot.message_handler(commands=["mavzu"])
def mavzu(message):
	msg = bot.send_message(message.chat.id, "Referat mavzusini kiriting")
	bot.register_next_step_handler(msg, echo_all)

def echo_all(message):
	referat_mavzusi=message.text
	referat_izoh = gpt_surov(referat_mavzusi)
	print("1-bosqich")
	msg = bot.send_message(message.chat.id, "1-bosqich")
	doc_creator(referat_mavzusi, referat_izoh)
	doc=open("./generated_doc.docx", "rb")
	print("2-bosqich")
	msg = bot.send_message(message.chat.id, "2-bosqich")
	bot.send_document(message.chat.id, doc)
	print("tugadi")

print("Bot ishga tushdi! \n")
bot.infinity_polling()
