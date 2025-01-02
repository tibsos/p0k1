import tkinter as tk
from tkinter import messagebox
import json

# Глобальные переменные для хранения координат
click_coordinates = []

# Функция для обработки кликов мыши
def on_click(event):
    x, y = event.x_root, event.y_root  # Используем координаты экрана
    click_coordinates.append((x, y))
    print(f"Clicked at: {x}, {y}")
    save_coordinates_after_click()

# Функция для сохранения координат после каждого клика
def save_coordinates_after_click():
    file_path = "coordinates.json"
    with open(file_path, "w") as json_file:
        json.dump(click_coordinates, json_file, indent=4)
    print(f"Coordinates updated in {file_path}")

# Функция завершения и сохранения координат в JSON-файл
def save_coordinates():
    file_path = "coordinates.json"
    with open(file_path, "w") as json_file:
        json.dump(click_coordinates, json_file, indent=4)
    print(f"Coordinates saved to {file_path}")
    root.destroy()

# Создание интерфейса
root = tk.Tk()
root.title("Screen Calibration Tool")

# Устанавливаем размеры окна на весь экран
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# Создание холста для отображения кликов
canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black")
canvas.pack()

# Привязка событий
canvas.bind("<Button-1>", on_click)

# Кнопка для завершения калибровки
finish_button = tk.Button(root, text="Finish Calibration", command=save_coordinates)
finish_button.pack()

# Запуск интерфейса
root.mainloop()
