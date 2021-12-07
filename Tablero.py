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
    }

peones_blancos = {
    'p2' : "peón blanco",
    }

def desplegar_tablero():
    for i in tablero:
        print(i)

fichas_negras = list(figuras_negras)
fichas_blancas = list(figuras_blancas)
peon_negro = list(peones_negros)
peon_blanco = list(peones_blancos)
tablero = [[], [], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "], [], []]
tablero[0] = tablero[0] + fichas_negras + [fichas_negras[2]] + [fichas_negras[1]] + [fichas_negras[0]]
tablero[7] = tablero[7] + fichas_blancas + [fichas_blancas[2]] + [fichas_blancas[1]] + [fichas_blancas[0]]
for i in range(8):
    tablero[1] += peon_negro
    tablero[6] += peon_blanco

desplegar_tablero()

#Partimos suponiendo que conocemos las reglas del juego y sabemos que se puede y que no se puede hacer

def mover_acabar():
    partida1 = True
    partida2 = True
    partida = True
    decision1 = input("Jugador 1, ¿Quiere mover ficha(escriba 1) o terminar la partida(escriba 2)?")
    if decision1 == 2:
        partida1 = False
        decision2 =  input("Jugador 2, ¿Quiere mover ficha(escriba 1) o terminar la partida(escriba 2)?")
        if decision2 == 2:
            partida2 = False
            partida = False
    return partida

def jugar_una_ronda():
    print("Jugador 1, ¿Quiere mover ficha o ?")