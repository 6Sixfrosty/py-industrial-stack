import random
import threading
import time
import os
import subprocess

OS = os.name

def clear_console():
    if OS == 'nt':
        subprocess.call('cls', shell=True)
    else:
        subprocess.call('clear', shell=True)

analog_input = {"DB1.temperature": 0.0}
digital_input = {"DB1.button1": False}

def leitura_temperatura():
    while not digital_input["DB1.button1"]:
        clear_console()
        analog_input["DB1.temperature"] = round(random.uniform(68, 82), 2)
        print(f"Temperature: {analog_input['DB1.temperature']} °F")
        time.sleep(1)
    clear_console()
    print("Leitura encerrada.")

def aguarda_botao():
    input()
    digital_input["DB1.button1"] = True

t1 = threading.Thread(target=leitura_temperatura)
t2 = threading.Thread(target=aguarda_botao)

t1.start()
t2.start()