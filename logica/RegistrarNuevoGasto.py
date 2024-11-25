import json
from menu.menuPrincipal import Designprincipal

def read_file(path):
    with open(f"databases/{path}", "r") as file:
        data = file.read()
        return json.loads(data)

def write_file(data, path):
    with open(f"databases/{path}", "w") as file:
        convertJson = json.dumps(data, indent=4)
        file.write(convertJson)

def add_gasto(database,monto,categoria,descripción):
    database[id]={
             
        "gasto": monto,
        "categoria": categoria,
        "descripción": descripción
}
    write_file(database, "registroGasto.json")

