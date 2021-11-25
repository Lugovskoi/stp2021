import pyowm
import telebot
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'ru'  

owm = pyowm.OWM('2158c8392bfa80b602e4110ac47ce933')
bot = telebot.TeleBot("2115511291:AAFqBR2y-h1_BgUVIBbuDt_Xg6e8FYOaWSw")

@bot.message_handler(content_types=['text'])
def send_mes(message):
    mrg = owm.weather_manager()
    place = message.text
    observation = mrg.weather_at_place(place)
    w = observation.weather
    temp = w.temperature('celsius')['temp']
    answer = "В городе " + place + ": " + w.detailed_status + "\n"
    answer += "Температура: " + str(temp) + "\n\n"
    bot.send_message(message.chat.id, answer)

bot.polling(none_stop = True)