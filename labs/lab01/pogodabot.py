import telebot

bot = telebot.TeleBot("2115511291:AAFqBR2y-h1_BgUVIBbuDt_Xg6e8FYOaWSw")

@bot.message_handler(content_types=['text'])
def send_mes(message):
	bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)