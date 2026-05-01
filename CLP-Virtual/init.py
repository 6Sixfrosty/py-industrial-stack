def inicializar():
    with open("config/io.json") as f:
        IO = json.load(f)

    with open("config/db.json") as f:
        DB = json.load(f)

    return IO, DB

IO, DB = inicializar()
