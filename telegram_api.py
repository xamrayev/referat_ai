import telebot
from ai_surov import gpt_surov
from doc_creator import doc_creator
from io import BytesIO

bot = telebot.TeleBot("BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Referat mavzusini kiriting")

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