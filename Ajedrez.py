import os

figuras = {
    't1' : chr(0x265C),
    'c1' : chr(0x265E),
    'a1' : chr(0x265D),
    'k1' : chr(0x265A),
    'q1' : chr(0x265B),
    'p1' : chr(0x265F),
    't2' : chr(0x2656),
    'c2' : chr(0x2658),
    'a2' : chr(0x2657),
    'k2' : chr(0x2655),
    'q2' : chr(0x2655),
    'p2' : chr(0x2659),
    "  " : " "
    }

def desplegar_tablero():
    for i in tablero:
        print(i)

tablero = [["t1", "c1", "a1", "k1", "q1", "a1", "c1", "t1"], ["p1", "p1", "p1", "p1", "p1", "p1", "p1", "p1"], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["p2", "p2", "p2", "p2", "p2", "p2", "p2", "p2"], ["t2", "c2", "a2", "k2", "q2", "a2", "c2", "t2"]]
for i in range(8):
    for j in range(8):
        tablero[i][j] = figuras.setdefault(tablero[i][j])
#Partimos suponiendo que conocemos las reglas del juego y sabemos que se puede y que no se puede hacer

def mover_acabar():
    decision = int(input("¿Quiere mover ficha(escriba 1) o terminar la partida(escriba 2)? "))
    if decision == 2:
        return False
    else:
        return True

def mover_ficha():
    ficha = list(map(int, input("Eliga la ficha que quiere mover(usando las coordenadas): ").rstrip().split()))
    posicion = list(map(int, input("Eliga la posición a la que la quiere mover(usando las coordenadas): ").rstrip().split()))
    for i in range(8):
        for j in range(8):
            if [i, j] == posicion:
                simbolo = tablero[ficha[0]][ficha[1]]
                tablero[ficha[0]][ficha[1]] = "  "
                tablero[i][j] = simbolo
    return tablero

def jugar_una_ronda():
    print("Jugador 1: ", end = "")
    jugador1 = mover_acabar()
    if jugador1 == True:
        print("Jugador 1:")
        mover_ficha()
        desplegar_tablero()
        print("Jugador 2:")
        mover_ficha()
        desplegar_tablero()
        return tablero
    else:
        print("Jugador 2: ", end = "")
        jugador2 = mover_acabar()
        if jugador2 == True:
            print("Jugador 1, debe mover ficha:")
            mover_ficha()
            desplegar_tablero()
            print("Jugador 2:")
            mover_ficha()
            desplegar_tablero()
            return tablero
        else:
            print("Gracias por jugar")
            return False

def jugar():
    print("Vamos a jugar al ajedrez.")
    print("A continuación se desplegará el tablero.")
    print("Para mover ficha o referirse a una casilla deberán indicarla con coordenadas, leyendo el tablero de arriba a abajo, de izquierda a derecha, siendo la primera la casilla 0, 0, la segunda la 0, 1 y así hasta la 7, 7")
    desplegar_tablero()
    print("El significado de cada símbolo es el siguiente " + str(figuras))
    texto = open(input("Eliga el nombre del fichero en el que guardar los tableros: "), "w")
    while jugar_una_ronda() != False:
        jugar_una_ronda()
        texto.write(str(tablero) + os.linesep)
    texto.close()

if __name__ == "__main__":
    jugar()