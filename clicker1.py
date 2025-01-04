import json
import time
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController

# Загрузка координат из JSON файла
def load_coordinates(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

# Инициализация контроллеров для мыши и клавиатуры
mouse = Controller()
keyboard = KeyboardController()

# Задержка после каждого клика
CLICK_DELAY = 0.1  # 100 мс

# Функция для клика по координатам
def click_at(x, y):
    mouse.position = (x, y)
    time.sleep(CLICK_DELAY)  # Задержка перед кликом
    mouse.click(Button.left)  # Указываем левую кнопку мыши
    print(f"Clicked at ({x}, {y})")

# Функция для ввода текста
def type_text(text):
    time.sleep(CLICK_DELAY)  # Задержка перед вводом текста
    for char in text:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)  # Задержка между нажатиями клавиш

# Основная функция для выполнения всех действий
def perform_transaction(user_id, transfer_amount, coordinates_file):
    # Загружаем координаты
    coordinates = load_coordinates(coordinates_file)

    # Клик по всем кнопкам из файла JSON с их координатами
    for button_name, (x, y) in coordinates.items():
        click_at(x, y)

        if button_name == "Поиск участника (поле)":
            # После клика по "Поиск участника", вводим ID пользователя
            print(f"Вводим ID пользователя: {user_id}")
            type_text(str(user_id))

        elif button_name == "Пользователь":
            # После клика по пользователю, нажимаем кнопку "Выдать"
            click_at(x, y)  # клик на пользователя

        elif button_name == "Выдать":
            # После клика по "Выдать", вводим сумму перевода
            print(f"Вводим сумму перевода: {transfer_amount}")
            type_text(str(transfer_amount))
            click_at(x, y)  # клик на кнопку "Выдать"
            break  # Выход после выполнения всех действий

# Пример входных данных (ID пользователя и сумма перевода)
user_id = "12345"
transfer_amount = "1000.00"

# Путь к файлу с координатами
coordinates_file = "coordinates.json"

# Выполнение транзакции
perform_transaction(user_id, transfer_amount, coordinates_file)
