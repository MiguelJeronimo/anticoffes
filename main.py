import cv2
from pynput import keyboard
from pynput.keyboard import KeyCode
from camara.Camara import Camara
from utils.Data import Data
from utils.Windows import Windows
from utils.matches import matches

data = Data()
windows = Windows()
def on_press(key:KeyCode):
    try:
        print(f"{str(key)}")
        if str(key) == "Key.space":
            data.wire_txt("dictionary/frases.txt", 'a', " ")
        data.wire_txt("dictionary/frases.txt", 'a', key.char)
    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    #detener el script al precionar esc
    if key == keyboard.Key.enter:
        text = data.read_txt('dictionary/frases.txt')
        json = data.read_json('dictionary/dictionary.json')
        match = matches(text, json['dictionaty'])
        if match:
            print(f"Detectamos que quisieron poner: {text}")
            windows.blocked()
            cam = cv2.VideoCapture(0)
            camera = Camara(camera=cam, cv2=cv2)
            camera.capture("coffes")
            camera.close()
        # Stop listener
        return False
    if key == keyboard.Key.space:
        text = data.read_txt('dictionary/frases.txt')
        json = data.read_json('dictionary/dictionary.json')
        match = matches(text, json['dictionaty'])
        if match:
            print(f"Detectamos que quisieron poner: {text}")
            windows.blocked()
            cam = cv2.VideoCapture(0)
            camera = Camara(camera=cam, cv2=cv2)
            camera.capture("coffes")
            camera.close()

    if key == keyboard.Key.esc:
        data.wire_txt("dictionary/frases.txt", 'w', "")
        # Stop listener
        return False

if __name__ == '__main__':
    # Collect events until released
    print(f"""
      AAAAA  N   N TTTTT III  CCCCC OOO  FFFFF FFFFF EEEEE SSSSS
      A   A  NN  N   T    I   C     O   O F     F     E     S
      AAAAA  N N N   T    I   C     O   O FFFF  FFFF  EEEE  SSSS
      A   A  N  NN   T    I   C     O   O F     F     E         S
      A   A  N   N   T   III  CCCCC OOO  F     F     EEEEE SSSSS

                            by Mike :)                      
    """)
    print("Ejecutandose............................")
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()

    # ...or, in a non-blocking fashion:
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release)
    listener.start()