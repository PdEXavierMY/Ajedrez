p1 = "peón negro"
t1 = "torre negro"
c1 = "caballo negro"
a1 = "alfil negro"
k1 = "rey negro"
q1 = "reina negro"
p2 = "peón blanco"
t2 = "torre blanca"
c2 = "caballo blanca"
a2 = "alfil blanca"
k2 = "rey blanca"
q2 = "reina blanca"
tablero = [[t1, c1, a1, k1, q1, a1, c1, t1], [p1, p1, p1, p1, p1, p1, p1, p1], [], [], [], [], [p2, p2, p2, p2, p2, p2, p2, p2], [t2, c2, a2, k2, q2, a2, c2, t2]]
def desplegar_tablero():
    for i in tablero:
        print(tablero[i])
desplegar_tablero()