#JUEGO NUMERO 2: ADIVINA EL NUMERO
import random

def guess_the_number(x):
    
    print("===========================")
    print("  Bienvenido(a) al Juego! ")
    print("===========================")
    print("Tu meta es adivinar el número generado por la computadora")
    
    numero_aleatorio = random.randint(1, x) #Numero aleatorio entre 1 y x
    
    prediccion = 0
    
    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) #El usuario ingresa su prediccion
        if prediccion < numero_aleatorio:
            print("Intenta otra vez. Este número es muy pequeño.")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez. Este número es muy grande.")
    
    print(f"Felicidades! Adivinaste el número {numero_aleatorio} correctamente")


guess_the_number(10)  # Llamada a la función con el rango de números del 1 al 10
        