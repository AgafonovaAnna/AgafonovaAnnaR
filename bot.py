import telebot
import random
from telebot import types

# Загружаем список интересных фактов
f = open('predictions.txt', 'r', encoding='UTF-8')
predictions = f.read().split('\n')
f.close()

# Загружаем список поговорок
f = open('thinks.txt', 'r', encoding='UTF-8')
thinks = f.read().split('\n')
f.close()

f = open('present.txt', 'r', encoding='UTF-8')
present = f.read().split('\n')
f.close()


bot = telebot.TeleBot('token.token')

@bot.message_handler(commands=['start'])
def start(message, res=False):
    # Добавляем кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Предсказание')
    item2 = types.KeyboardButton('Факт')
    item3 = types.KeyboardButton('Идея для подарка')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    mess = (f'Привет, <b>{message.from_user.first_name}</b>! '
            f'\nЧто выберешь?'
            f'\nПредсказание на сегодняшний день'
            f'\nИнтересный факт'
            f'\nИли же хорошую идею для подарка')
    bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)


# Получение сообщений от польз
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт' :
            answer = random.choice(thinks)
    elif message.text.strip() == 'Предсказание':
            answer = random.choice(predictions)
    elif message.text.strip() == 'Идея для подарка':
            answer = random.choice(present)
    else:
            answer = 'Пока что я могу выполнять только те команды, которые есть на кнопках('
    bot.send_message(message.chat.id, answer)

# Запускаем бота
bot.polling(none_stop=True)