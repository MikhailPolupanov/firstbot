import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Иди своей дорогой, Сталкер...')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    if text == "хабар" or text == "Хабар!" or text == "Хабар?":
        update.message.reply_text("Ты бы еще консервных банок насобирал…")
    elif text == "пока" or text == "пока!" or text == "пока?":
        update.message.reply_text("Удачной охоты, сталкер!")
    elif text == "привет" or text == "привет!" or text == "привет?":
        update.message.reply_text("Новичков нынче, как собак нерезаных, и всё-то они лучше стариков знают!")
    elif text == "кто ты"  or text == "кто ты!"  or text == "кто ты?":
        update.message.reply_text("На нас лежит огромная ответственность — нужно защитить мир от наступления Зоны! Свободные сталкеры, ветераны и охотники! Вливайтесь в ряды «Долга»! Защитить мир от заразы Зоны — наша общая цель и задача!")
    elif text == "привет меня зовут Юля" or text == "привет, меня зовут Юля" or text == "Привет, меня зовут Юля!" or text == "меня зовут Юля" or text == "меня зовут Юля" or text == "меня зовут юля" or text == "привет меня зовут юля" or text == "Привет меня зовут Юля" or text == "привет меня зовут Юля" or text == "Привет, меня зовут Юля":
        update.message.reply_text("Женщине не место в зоне")
    elif text == "Что ты умеешь?" or text == "Что ты умеешь" or text == "Что ты можешь" or text == "Что ты можешь?":
        update.message.reply_text("Мочить мутантов")
    else:
        update.message.reply_text(text)
        

def main ():
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info('Bot started work')
    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
