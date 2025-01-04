import json
import telebot

# Секретный токен
API_TOKEN = "7715486996:AAGOmKN6LG5yyjnOR5nRQ05uZXUGRdrEWkI"
# Имя файла для записи данных
FILE_NAME = "lenta_kassa.json"

bot = telebot.TeleBot(API_TOKEN)

def save_to_file(data):
    """Сохраняет данные в конец JSON файла."""
    try:
        # Открываем файл в режиме чтения и записи
        with open(FILE_NAME, "r+") as file:
            try:
                content = json.load(file)
            except json.JSONDecodeError:
                content = []

            if not isinstance(content, list):
                content = []

            content.append(data)

            # Перемещаем указатель в начало и перезаписываем файл
            file.seek(0)
            json.dump(content, file, indent=4)
    except FileNotFoundError:
        # Если файл не найден, создаем новый
        with open(FILE_NAME, "w") as file:
            json.dump([data], file, indent=4)

@bot.message_handler(content_types=['text'])
def handle_message(message):
    """Обрабатывает входящие сообщения и записывает их в JSON файл."""
    try:
        # Преобразуем текст сообщения в JSON формат
        message_data = json.loads(message.text)

        # Проверяем, содержит ли сообщение нужные ключи
        if "name" in message_data and "amount" in message_data:
            save_to_file(message_data)
            bot.reply_to(message, "Данные сохранены.")
        else:
            bot.reply_to(message, "Некорректный формат данных. Ожидаются ключи 'name' и 'amount'.")
    except json.JSONDecodeError:
        bot.reply_to(message, "Ошибка: сообщение должно быть в формате JSON.")

if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
