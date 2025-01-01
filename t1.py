import json 
from pynput 
import mouse 
# Список для хранения координат нажатий левой кнопки мыши 
clicks = []  
def on_click(x, y, button, pressed):     
    if button == mouse.Button.left and pressed:         
        
# При нажатии левой кнопки мыши добавляем координаты в список 
# 
        print(f"Left mouse button clicked at ({x}, {y})")         
        clicks.append({"button": "left", "position": (x, y)})  
        # Установка слушателя событий мыши 
        listener = mouse.Listener(on_click=on_click) 
        listener.start()  
        input("Press Enter to stop listening for mouse events...")  
        # Остановить слушатель 
        listener.stop()  # Сохранение координат в файл key.json в формате JSON
        with open('key.json', 'w') as f:     
            json.dump(clicks, f)  
            print("Mouse clicks saved to key.json.")