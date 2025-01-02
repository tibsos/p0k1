import json 
from pynput import mouse 

clicks = []  

def on_click(x, y, button, pressed):  

    if button == mouse.Button.left and pressed:     

        print(f"Left mouse button clicked at ({x}, {y})")         
        clicks.append({"button": "left", "position": (x, y)})  
        listener = mouse.Listener(on_click=on_click) 
        listener.start()  
        input("Press Enter to stop listening for mouse events...")  
        listener.stop()
        with open('key.json', 'w') as f:     
            json.dump(clicks, f)  
            print("Mouse clicks saved to key.json.")