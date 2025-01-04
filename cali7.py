import pynput
from pynput.mouse import Listener
import json
import time

# Глобальные переменные для хранения координат
click_coordinates = {}
file_path = "coordinates.json"

button_list = [
    "Клуб",
    "Красная кнопка",
    "Прилавок",
    "Поиск участника (поле)",
    "Пользователь",
    'Выдать юзера',
    "Выдать сумму",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."
]

button_index = 0  # Индекс текущей кнопки для калибровки

requested_button = None  # Текущая кнопка, которую нужно кликнуть

# Функция для обработки кликов мыши
def on_click(x, y, button, pressed):
    global button_index, requested_button
    if pressed and requested_button is not None:
        # Сохраняем координаты для текущей кнопки
        click_coordinates[requested_button] = (x, y)
        print(f"Clicked at: {x}, {y} (for {requested_button})")
        save_coordinates_after_click()
        
        # Переходим к следующей кнопке или завершаем программу
        button_index += 1
        if button_index >= len(button_list):
            print("Калибровка завершена. Завершение программы.")
            exit_program()
        else:
            request_next_button()

# Функция для сохранения координат в JSON
def save_coordinates_after_click():
    with open(file_path, "w") as json_file:
        json.dump(click_coordinates, json_file, indent=4, ensure_ascii=False)
    print(f"Coordinates updated in {file_path}")

# Функция для запроса следующей кнопки
def request_next_button():
    global requested_button
    if button_index < len(button_list):
        requested_button = button_list[button_index]
        print(f"Пожалуйста, нажмите на '{requested_button}'...")

# Функция завершения программы
def exit_program():
    print("Exiting program.")
    exit(0)

# Основная функция для начала калибровки
def calibration_instructions():
    print("Начинаем процесс калибровки...")
    # Запрашиваем первую кнопку
    request_next_button()

# Запуск слушателя кликов
def start_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

# Начинаем калибровку
calibration_instructions()

# Запуск слушателя
start_listener()
