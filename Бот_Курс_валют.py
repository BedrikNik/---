import telebot
from extensions import APIException, BotExtensions

bot = telebot.TeleBot('5939265566:AAEUf9jwHo0kRy2CfmxJnRzdzbblarfs4BM')


@bot.message_handler(commands=['start', 'help'])
def handle_help(message: telebot.types.Message):
    bot.send_message(message.chat.id, f"Приветствую!\n\n"
                                      f"Чтобы узнать стоимость, введите команду в следующем формате:\n"
                                      f"<имя валюты цену которой нужно узнать> <имя валюты в которой надо узнать цену> <количество первой валюты> ( например USD RUB 100)\n"
                                      f"Допускается не указывать количество (например USD RUB)\n\n"
                                      f"список доступных валют можно узнать по команде /values")


@bot.message_handler(commands=['values'])
def handle_values(message: telebot.types.Message):
    bot.send_message(message.chat.id, BotExtensions.get_values())


@bot.message_handler(content_types=['text'])
def try_convert(message: telebot.types.Message):
    try:
        reply = BotExtensions.process_data(message.text)

    except APIException as ex:
        bot.send_message(message.chat.id, f'Ошибка пользователя:\n{ex}\n')

    except Exception as ex:
        bot.send_message(message.chat.id, f'Что-то пошло не так:\n{ex}\n'
                                          f'Для помощи используйте команду /help\n'
                                          f'Если ничего не помогло, обратитесь к разработчику.')

    else:
        bot.send_message(message.chat.id, reply)


bot.polling()
