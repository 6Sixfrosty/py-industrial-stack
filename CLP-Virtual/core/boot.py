import json

def inicializar():
    with open("config/clp.json") as f:
        config = json.load(f)

    IO = config["IO"]
    DB = config["DB"]

    return IO, DB
IO, DB = inicializar()