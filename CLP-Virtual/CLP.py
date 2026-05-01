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

# ENTRADAS DIGITAIS — %IX
IX = {
    "%IX0.0": False,  # btn-ligar
    "%IX0.1": False,  # btn-emergencia
    "%IX0.2": False,  # sensor-presenca-massa
    "%IX0.3": False,  # porta-forno
}

# SAÍDAS DIGITAIS — %QX
QX = {
    "%QX0.0": False,  # resistencia-forno
    "%QX0.1": False,  # motor-esteira
    "%QX0.2": False,  # alarme
    "%QX0.3": False,  # luz-status
}

# ENTRADAS ANALÓGICAS — %IW
IW = {
    "%IW0": 0.0,  # temp-forno
    "%IW1": 0.0,  # temp-massa
    "%IW2": 0,    # velocidade-esteira
    "%IW3": 0.0,  # pressao-prensa
    "%IW4": 0.0,  # umidade-massa
}

# MEMÓRIA INTERNA — %MW
MW = {
    "%MW0": 0,    # contador-biscoitos
    "%MW1": 0.0,  # tempo-forno
    "%MW2": 0.0,  # tempo-turno
}


# BLOCO DE DADOS — DB (mapeamento dos nomes das tags)
DB = {
    "btn-ligar":             "%IX0.0",
    "btn-emergencia":        "%IX0.1",
    "sensor-presenca-massa": "%IX0.2",
    "porta-forno":           "%IX0.3",
    "resistencia-forno":     "%QX0.0",
    "motor-esteira":         "%QX0.1",
    "alarme":                "%QX0.2",
    "luz-status":            "%QX0.3",
    "temp-forno":            "%IW0",
    "temp-massa":            "%IW1",
    "velocidade-esteira":    "%IW2",
    "pressao-prensa":        "%IW3",
    "umidade-massa":         "%IW4",
    "contador-biscoitos":    "%MW0",
    "tempo-forno":           "%MW1",
    "tempo-turno":           "%MW2",
}


#threading.Thread(target=
#.start()
#round(random.uniform(68, 82)