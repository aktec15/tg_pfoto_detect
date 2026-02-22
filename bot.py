import telebot
import config


bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    photo = message.photo[-1]
    file_info = bot.get_file(photo.file_id)
    downloaded_file = bot.download_file(file_info.file_path)
    save_path = 'photo.jpg'
    with open(save_path, 'wb') as new_file:
        new_file.write(downloaded_file)
    bot.reply_to(message, 'Фотография сохранена.')
    
    # обработку фотографии
    # бот пишет результат



bot.infinity_polling()

