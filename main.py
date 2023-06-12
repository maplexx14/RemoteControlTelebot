#Импорт библиотек
import telebot
from telebot import types
import os
import webbrowser
from sound import Sound

#Подключение бота
bot = telebot.TeleBot("token")
print("Бот запущен")

#Работа команды /start
@bot.message_handler(commands=['start'])
def start(message):

    btn = types.KeyboardButton("Создать файл")
    btn1 = types.KeyboardButton("Открыть браузер")
    btn2 = types.KeyboardButton("Открыть сайт")
    btn3 = types.KeyboardButton("Открыть приложение")
    btn4 = types.KeyboardButton("Открыть заранее выставленные приложения")
    btn5 = types.KeyboardButton("Выключить компьютер")
    btn6 = types.KeyboardButton("Перезагрузить компьютер")
    btn7 = types.KeyboardButton("Спящий режим")
    btn8 = types.KeyboardButton("Открыть проводник")
    btn9 = types.KeyboardButton("Изменить громкость")
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
    bot.send_message(message.from_user.id, "Это приложение для удаленного доступа", reply_markup = markup)


#Ответ на кнопки
@bot.message_handler(content_types=['text'])
def plat(message):
    #Выключение компа
    if message.text == "Выключить компьютер":
        os.system("shutdown /s")

    elif message.text == "Перезагрузить компьютер":
        os.system("shutdown /r")

    elif message.text == "Спящий режим":
        os.system("shutdown /h")

    elif message.text == "Открыть приложение":
        msg = bot.send_message(message.from_user.id, "Вставьте полный путь к файлу")
        bot.register_next_step_handler(msg, openApp)


    elif message.text == "Открыть браузер":
        webbrowser.register('Chrome', None,
                            webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
        webbrowser.get(using = "Chrome").open_new_tab("ya.ru")

    elif message.text == "Открыть сайт":
        nac = bot.send_message(message.from_user.id, "Введите URL сайта")
        bot.register_next_step_handler(nac, search)

    elif message.text == "Открыть проводник":
        os.startfile("C:\Windows\explorer.exe")

    elif message.text == "Создать файл":
        name = bot.send_message(message.from_user.id, "Введите имя и тип файла, который хотите создать")
        bot.register_next_step_handler(name, openfile)


    #Действия со звуком
    elif message.text == "Изменить громкость":
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        btn1 = types.KeyboardButton("Добавить громкость на 2")
        btn2 = types.KeyboardButton("Убавить громкость на 2")
        btn3 = types.KeyboardButton("Ввести свое значение")
        btn4 = types.KeyboardButton("Убрать звук")
        btn5 = types.KeyboardButton("Прибавить звук на максимум")
        btn6 = types.KeyboardButton("Назад")


        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)

        bot.send_message(message.from_user.id, "Выберите действие со звуком", reply_markup=markup)

    if message.text == "Добавить громкость на 2":
        Sound.volume_up()

    elif message.text == "Убавить громкость на 2":
        Sound.volume_down()

    elif message.text == "Убрать звук":
        Sound.mute()

    elif message.text == "Прибавить звук на максимум":
        Sound.volume_max()

    elif message.text == "Ввести свое значение":
        vol = bot.send_message(message.from_user.id, "Введите значение")
        bot.register_next_step_handler(vol, corr)

        # Действие назад
    elif message.text == "Назад":

        btn = types.KeyboardButton("Создать файл")
        btn1 = types.KeyboardButton("Открыть браузер")
        btn2 = types.KeyboardButton("Открыть сайт")
        btn3 = types.KeyboardButton("Открыть приложение")
        btn4 = types.KeyboardButton("Открыть заранее выставленные приложения")
        btn5 = types.KeyboardButton("Выключить компьютер")
        btn6 = types.KeyboardButton("Перезагрузить компьютер")
        btn7 = types.KeyboardButton("Спящий режим")
        btn8 = types.KeyboardButton("Открыть проводник")
        btn9 = types.KeyboardButton("Изменить громкость")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9)
        bot.send_message(message.from_user.id, "Это приложение для удаленного доступа", reply_markup=markup)


#Срабатывание открытия сайтов
def search(message):
    nic = message.text.split()[0]
    webbrowser.get(using=f"Chrome").open_new_tab(nic)


def openfile(message):
    nic = message.text.split()[0]
    open(nic, "w")


def corr(message):
    vol = int(message.text.split()[0])
    Sound.volume_set(vol)

def openApp(message):

    msg = message.text.split()
    
    os.startfile(str(msg))
#Зацикливание бота
bot.polling(none_stop=True, interval=0)
