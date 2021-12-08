figuras = {
    't1' : "torre negro",
    'c1' : "caballo negro",
    'a1' : "alfil negro",
    'k1' : "rey negro",
    'q1' : "reina negro",
    'p1' : "peón negro",
    't2' : "torre blanca",
    'c2' : "caballo blanca",
    'a2' : "alfil blanca",
    'k2' : "rey blanca",
    'q2' : "reina blanca",
    'p2' : "peón blanco",
    }

def desplegar_tablero():
    for i in tablero:
        print(i)

tablero = [["t1", "c1", "a1", "k1", "q1", "a1", "c1", "t1"], ["p1", "p1", "p1", "p1", "p1", "p1", "p1", "p1"], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["p2", "p2", "p2", "p2", "p2", "p2", "p2", "p2"], ["t2", "c2", "a2", "k2", "q2", "a2", "c2", "t2"]]
print("El significado de cada símbolo es el siguiente" + str(figuras))
desplegar_tablero()

#Partimos suponiendo que conocemos las reglas del juego y sabemos que se puede y que no se puede hacer

def mover_acabar1():
    partida1 = True
    decision1 = input("Jugador 1, ¿Quiere mover ficha(escriba 1) o terminar la partida(escriba 2)?")
    if decision1 == 2:
        partida1 = False
    return partida1

def mover_acabar2():
    partida2 = True
    decision2 = input("Jugador 2, ¿Quiere mover ficha(escriba 1) o terminar la partida(escriba 2)?")
    if decision2 == 2:
        partida2 = False
    return partida2

def mover_ficha():
    ficha = list(map(int, input("Eliga la ficha que quiere mover(usando las coordenadas): ").rstrip().split()))
    posicion = list(map(int, input("Eliga la posición a la que la quiere mover(usando las coordenadas): ").rstrip().split()))
    for i in range(8):
        for j in range(8):
            if [i, j] == posicion:
                simbolo = tablero[ficha[0]][ficha[1]]
                tablero[i][j] = simbolo
                tablero[ficha[0]][ficha[1]] = "  "
    return tablero

def jugar_una_ronda(juego):
    j1 = mover_acabar1()
    if j1 == True:
        print("Jugador 1:")
        mover_ficha()
        desplegar_tablero()
        print("Jugador 2:")
        mover_ficha()
        desplegar_tablero()
    else:
        j2 = mover_acabar2()
        if j2 == True:
            print("Jugador 1, debe mover ficha:")
            mover_ficha()
            desplegar_tablero()
            print("Jugador 2:")
            mover_ficha()
            desplegar_tablero()
        else:
            print("Gracias por jugar")
            juego = False
    return tablero and juego

def jugar():
    print("Vamos a jugar al ajedrez")
    print("A continuación se desplegará el tablero")
    print("Para mover ficha o referirse a una casilla deberán indicarla con coordenadas, leyendo el tablero de arriba a abajo, de izquierda a derecha, siendo la primera la casilla 0, 0, la segunda la 0, 1 y así hasta la 7, 7")
    juego = True
    while juego:
        jugar_una_ronda(juego)

if __name__ == "__main__":
    jugar()