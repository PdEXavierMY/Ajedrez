figuras_negras = {
    'p1' : "peón negro",
    't1' : "torre negro",
    'c1' : "caballo negro",
    'a1' : "alfil negro",
    'k1' : "rey negro",
    'q1' : "reina negro",
    'e' : "espacio",
    }

figuras_blancas = {
    'p2' : "peón blanco",
    't2' : "torre blanca",
    'c2' : "caballo blanca",
    'a2' : "alfil blanca",
    'k2' : "rey blanca",
    'q2' : "reina blanca",
    'e' : "espacio",
    }

def desplegar_tablero(tablero):
    for i in tablero:
        print(i)
print(figuras.values())
