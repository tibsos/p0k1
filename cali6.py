import pynput
from pynput.mouse import Listener
import json
import threading
import time

# Глобальные переменные для хранения координат
click_coordinates = {}
file_path = "coordinates.json"
button_counter = 1  # Счётчик для наименования кнопок (кнопка 1, кнопка 2 и т.д.)
requested_button = None  # Переменная для хранения текущей запрашиваемой кнопки

# Функция для обработки кликов мыши
def on_click(x, y, button, pressed):
    global button_counter, requested_button
    if pressed and requested_button is not None:
        # Проверяем, что был клик на нужной кнопке
        button_name = f"кнопка {button_counter}"
        if button_name == requested_button:
            # Сохраняем координаты для этой кнопки
            click_coordinates[button_name] = (x, y)
            print(f"Clicked at: {x}, {y} (for {button_name})")
            save_coordinates_after_click()
            
            # Переходим к следующей кнопке
            button_counter += 1
            requested_button = None  # Сбросить текущую запрашиваемую кнопку
            request_next_button()

# Функция для сохранения координат после каждого клика
def save_coordinates_after_click():
    with open(file_path, "w") as json_file:
        json.dump(click_coordinates, json_file, indent=4, ensure_ascii=False)
    print(f"Coordinates updated in {file_path}")

# Функция для запроса следующей кнопки
def request_next_button():
    global requested_button
    if button_counter <= 9:
        requested_button = f"кнопка {button_counter}"
        print(f"Please click on {requested_button}...")
    else:
        print("Calibration complete.")
        return

# Основная функция для запуска слушателя кликов
def start_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

# Функция для калибровки окна
def calibration_instructions():
    print("Starting calibration process...")
    # Запрашиваем первую кнопку
    request_next_button()

# Запуск калибровки
calibration_instructions()

# Запуск слушателя в фоновом потоке
listener_thread = threading.Thread(target=start_listener)
listener_thread.daemon = True  # Поток завершится, если основной поток завершится
listener_thread.start()

print("Listening for mouse clicks... Press Ctrl+C to stop.")
try:
    while True:
        time.sleep(1)  # Добавляем небольшую задержку, чтобы не использовать много ресурсов
except KeyboardInterrupt:
    print("Exiting program.")
