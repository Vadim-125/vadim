import telebot, math
import random as r
from telebot.util import extract_arguments #библиотека для извлечения аргументов
import sympy as sp

#Дальнейшие идеи: 1) Создать полноценную команду /news, например, для того, чтобы просматривать реаьные новости; 
#2) Создать команду /weather, которая будет показывать реальную погоду; 
#3) Создать команду /translate, которая будет в качестве переводчика.
#4) Создать команду /dollar, которая будет показывать курс доллара в тенге.
#5) Создать команду /convert <валюта> <сумма>, которая будет конвертировать валюты.

#Сейчас:
#1) /calc *Добавить производные и интегральные функции
 

token = '7613709241:AAErGCm3cDtpKpo0jo-imkMjnepGmRy5VpY'
bot = telebot.TeleBot(token)

chat_id = '5119388800'

def auto_send_message():
    try:
        bot.send_message(chat_id, 'Бот успешно запущен!✅\nНапишите /start, чтобы начать.\n\n')
    except Exception as e:
        print(f"Ошибка отправки сообщения: {e}")

@bot.message_handler(commands= ['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    bot.reply_to(message, '''Добро Пожаловать! ;)
Меня зовут Vadim_bot, т.е. я простой чат-Бот, который будет обрабатывать и отвечать на ваши сообщения.
У меня имеется несколько команд, которыми ты можешь воспользоваться в любой момент. Для этого пропиши команду /info, чтобы ознакомиться с моими командами.''')

@bot.message_handler(commands=['info'])
def next_message(message):
    bot.send_message(message.chat.id, '''Мои команды:
1) /start - начальная команда.
2) /info - специальная команда, в которой хранятся все команды Бота.
3) /coin - игра в Орёл и Решка c выпадением очков. Если выпало очко(+2), то супер, а если (+1), то ничего страшного, ещё повезёт.                     
4) /cube - игра в игральный кубик, т.е. по типу броска игрального кубика с выпадением числа от 1 до 6.
5) /car - после написания в строку данной команды вы должны обозначить машину, т.е. обозначить какой марки и выдать ей определённый цвет. Например, /car (марка) (цвет) .                    
6) /get_info - узнать ваши персональные данные. Также, подождите 15 секунд, пока пройдёт обработка данных.
7) /calc - обычный калькулятор для вычисления базовых математических выражений.
8) /calc_hm - калькулятор для вычисления математических выражений из раздела Высшей математики. 
...''')
    
@bot.message_handler(commands=['coin'])
def coin_game(message):
    list_0 = ['Орёл', "Решка"]
    coin = r.choice(list_0)
    point = 0
    if coin == list_0[0]:
        point+=2
    else:
        point+=1
    bot.reply_to(message, f'Сторона: {coin}, Очки: +{point}')

@bot.message_handler(commands=['cube'])
def cube_game(message):
    cube = r.randint(1, 6)
    bot.reply_to(message, f'Выпало число: {cube}')

@bot.message_handler(commands=['car'])
def car_message(message):
    argument = extract_arguments(message.text)
    if argument:
        bot.reply_to(message, f'Вы отправили: {argument}')
    else:
        bot.reply_to(message, 'Вы ничего не отправили и для того, чтобы отправить сообщение, напишите /car <марка> <цвет>')
    class Car:
        def __init__(self, name, color):
            self.name = name
            self.color = color
            bot.reply_to(message, f'Марка машины: {self.name}, Цвет машины: {self.color}')

    arg = argument.split()
    car = Car(name=arg[0], color=arg[1])

@bot.message_handler(commands=['get_info'])
def get_info(message):
    first_name = message.from_user.first_name or "Не указано"
    last_name = message.from_user.last_name or "Не указано"
    user_id = message.from_user.id 
    username = message.from_user.username or "Не указано"
    bot.reply_to(message, f'''Ваши данные:
Chat ID: {message.chat.id}
ID: {user_id}
Username: @{username}
Фамилия: {first_name}
Имя: {last_name}
''')

@bot.message_handler(commands=['calc'])
def calc_message(message):
    functions = ','.join(dir(math))
    bot.send_message(message.chat.id, f'''Добро пожаловать в Калькулятор! В данном калькуляторе имеется большое количество возможностей для проведения любых вычислений, начиная от самых базовых моментов и заканчивая сложными функциями.
Представляю вашему вниманию: {functions}. 
Также, пример: (1+1)*1, sqrt(16), sin(3.14), log(100, 10), e, 1**2 и т.д. Можете написать в чат любое выражение и я вычислю его.''')
@bot.message_handler(func = lambda message: True)
def eval_message(message):
    expression = message.text.strip()
    safe_math = {name: getattr(math, name) for name in dir(math) if not name.startswith("_")} #!!!
    safe_math['cot'] = lambda x: 1/math.tan(x) #!!!
    try:
        result = eval(expression, {"__builtins__": None}, safe_math) #eval - математическая функция для вычисления выражений. которая вcтроена в сам Python.
        bot.reply_to(message, f'Результат: {result}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка: {e}')

@bot.message_handler(commands=['calc_hm'])
def calculate_hm(message):
    bot.send_message(message.chat.id, f'''Добро пожаловать в Калькулятор Высшей математики! В данном калькуляторе имеется большое количество возможностей, например, здесь вы сможете посчитать неопределённый и определённый интеграл, также и производные.
Можете написать в чат любое выражение и я вычислю его.''')
@bot.message_handler(func = lambda message: True)
def message_calc_hm(message):
    bot.reply_to(message, f'''Какую функцию будем вычислять?(1 или 2 - напишите в чат цифру.)
1) Интегральную.
2) Производную.''')
    user = ['1', '2']
    def calculate_derivative(expression, variable):
        try:
            var = sp.symbols(variable)
            expr = sp.sympify(expression)
            derivative = sp.diff(expr, var)
            return f'''Ваша функция f({variable}) = {expr}, т.е. по {variable}: f'({variable}) = {derivative} '''
        except Exception as e:
            bot.reply_to(message, f'Ошибка: {e}')




    if user[0]:
        bot.reply_to(message, 'Вычисляем производную')
        
if __name__ == '__main__':
    auto_send_message()
bot.infinity_polling()
