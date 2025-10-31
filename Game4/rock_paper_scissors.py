#JUEGO A: ROCK, PAPER, SCISSORS
# El usuario juega contra la computadora en el clásico juego de piedra, papel o tijeras

import random


def jugar():
    usuario = input("Escoge una opción: 'pi' para piedra, 'pa' para papel o 'ti' para tijeras: \n").lower()
    computadora = random.choice(['pi', 'pa', 'ti'])
    
    if usuario == computadora:
        return "¡Empate! La computadora también eligió " + computadora
    
    if gano_el_jugador(usuario, computadora):
        return "¡Ganaste! La computadora eligió " + computadora
    
    return "¡Perdiste! La computadora eligió " + computadora
    

def gano_el_jugador(jugador, oponente):
    #Devuelve True si gana el jugador.
    #Piedra gana a tijera (pi > ti).
    #Tijera gana a papel (ti > pa).
    #Papel gana a piedra (pa > pi).
    
    if ((jugador == 'pi' and oponente == 'ti') or (jugador == 'ti' and oponente == 'pa') or (jugador == 'pa' and oponente == 'pi')):
        return True
    else:
        return False
    

print(jugar())