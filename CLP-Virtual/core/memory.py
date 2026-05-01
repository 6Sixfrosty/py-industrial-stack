from core.boot import IO, DB

def GET(tag):
    return IO[DB[tag]]

def PUT(tag, value):
    IO[DB[tag]] = value