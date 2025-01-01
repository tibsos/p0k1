import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import json

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent

# Глобальные переменные для хранения координат
click_coordinates = []

# Функция для обработки кликов мыши
def on_click(event):
    x, y = event.x, event.y
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
root.title("Image Calibration Tool")

# Загрузка изображения
image_path = os.path.join(BASE_DIR, 'image_png1.png')  # Путь к загруженному изображению
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)

# Создание холста для отображения изображения
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=photo)

# Привязка событий
canvas.bind("<Button-1>", on_click)

# Кнопка для завершения калибровки
finish_button = tk.Button(root, text="Finish Calibration", command=save_coordinates)
finish_button.pack()

# Запуск интерфейса
root.mainloop()
