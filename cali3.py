import pynput
from pynput.mouse import Listener
import json
import threading

# Глобальные переменные для хранения координат
click_coordinates = []
file_path = "coordinates.json"

# Функция для обработки кликов мыши
def on_click(x, y, button, pressed):
    if pressed:
        click_coordinates.append((x, y))
        print(f"Clicked at: {x}, {y}")
        save_coordinates_after_click()

# Функция для сохранения координат после каждого клика
def save_coordinates_after_click():
    with open(file_path, "w") as json_file:
        json.dump(click_coordinates, json_file, indent=4)
    print(f"Coordinates updated in {file_path}")

# Основная функция для запуска слушателя кликов
def start_listener():
    with Listener(on_click=on_click) as listener:
        listener.join()

# Запуск слушателя в фоновом потоке
listener_thread = threading.Thread(target=start_listener)
listener_thread.daemon = True  # Поток завершится, если основной поток завершится
listener_thread.start()

print("Listening for mouse clicks... Press Ctrl+C to stop.")
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Exiting program.")
