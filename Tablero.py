figuras_negras = {
    't1' : "torre negro",
    'c1' : "caballo negro",
    'a1' : "alfil negro",
    'k1' : "rey negro",
    'q1' : "reina negro",
    }

peones_negros = {
    'p1' : "peón negro",
    }

figuras_blancas = {
    't2' : "torre blanca",
    'c2' : "caballo blanca",
    'a2' : "alfil blanca",
    'k2' : "rey blanca",
    'q2' : "reina blanca",
    'p2' : "peón blanco",
    }

peones_blancos = {
    'p2' : "peón blanco",
    }

def desplegar_tablero(tablero):
    for i in tablero:
        print(i)
lista = list(figuras_negras)
print(lista)