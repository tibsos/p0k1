import json
import time
import pyperclip
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController, Key

# Загрузка данных из JSON файла
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Загрузка координат из JSON файла
def load_coordinates(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Инициализация контроллеров для мыши и клавиатуры
mouse = Controller()
keyboard = KeyboardController()

# Задержка после каждого клика
CLICK_DELAY = 0.1  # 100 мс

# Функция для клика по координатам
def click_at(name, x, y):
    mouse.position = (x, y)
    time.sleep(CLICK_DELAY)  # Задержка перед кликом
    mouse.click(Button.left)  # Указываем левую кнопку мыши
    print(f"Clicked on '{name}' at ({x}, {y})")

# Функция для копирования текста в буфер обмена
def copy_to_clipboard(text):
    pyperclip.copy(text)
    print(f"Text '{text}' copied to clipboard.")

# Функция для вставки текста с помощью Ctrl+V
def paste_from_clipboard():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release('v')
    keyboard.release(Key.ctrl)
    print("Pasted from clipboard.")

# Функция для ввода суммы на циферблате
def enter_amount(amount, coordinates):
    for digit in str(amount):
        if digit in coordinates:
            x, y = coordinates[digit]
            click_at(f"Цифра {digit}", x, y)
        else:
            print(f"Координаты для '{digit}' не найдены!")

# Основная функция для выполнения всех действий
def perform_transaction(user_id, transfer_amount, coordinates_file):
    # Загружаем координаты
    coordinates = load_coordinates(coordinates_file)

    # Клик по кнопке "Поиск участника (поле)"
    if "Поиск участника (поле)" in coordinates:
        click_at("Поиск участника (поле)", *coordinates["Поиск участника (поле)"])
        print(f"Вводим ID пользователя: {user_id}")
        
        # Копируем ID пользователя в буфер обмена
        copy_to_clipboard(user_id)

        # Нажимаем Ctrl+V для вставки ID пользователя
        paste_from_clipboard()

    # Клик по кнопке "Пользователь"
    if "Пользователь" in coordinates:
        click_at("Пользователь", *coordinates["Пользователь"])

    # Клик по кнопке "Выдать юзера"
    if "Выдать юзера" in coordinates:
        click_at("Выдать юзера", *coordinates["Выдать юзера"])

    # Ввод суммы на циферблате
    print(f"Вводим сумму перевода: {transfer_amount}")
    enter_amount(transfer_amount, coordinates)

    # Клик по кнопке "Выдать" снова для подтверждения
    if "Выдать сумму" in coordinates:
        click_at("Выдать (подтверждение)", *coordinates["Выдать сумму"])

    # Нажатие клавиши Escape
    print("Нажимаем Escape для выхода.")
    keyboard.press(Key.esc)
    keyboard.release(Key.esc)
    print("Транзакция завершена.")

# Чтение последнего объекта из lenta_kassa.json
def get_last_transaction(file_path):
    data = load_json(file_path)
    if isinstance(data, list) and len(data) > 0:
        last_transaction = data[-1]
        return last_transaction.get("name"), last_transaction.get("amount")
    else:
        print("Ошибка: файл не содержит данных или имеет некорректный формат.")
        return None, None

# Путь к файлу с координатами
coordinates_file = "coordinates.json"

# Путь к файлу с данными транзакций
lenta_kassa_file = "lenta_kassa.json"

# Получение данных из последнего объекта
user_id, transfer_amount = get_last_transaction(lenta_kassa_file)

if user_id and transfer_amount:
    # Выполнение транзакции
    perform_transaction(user_id, transfer_amount, coordinates_file)
else:
    print("Не удалось выполнить транзакцию: отсутствуют данные.")
