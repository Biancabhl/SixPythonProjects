#JUEGO NUMERO 3: ADIVINA EL NUMERO COMPUTADORA
# La computadora intenta adivinar el numero que el usuario tiene en mente

import random


def adivina_el_numero_computadora(x):
    
    print("===============================")
    print("    Bienvenido(a) al Juego!    ")
    print("===============================")
    print(f"Selecciona un número entre 1 y {x}. La computadora intentará adivinarlo...")
    
    limite_inferior = 1
    limite_superior = x
    
    respuesta = ""
    while respuesta != "c":
        #Generar Prediccon
        if limite_inferior != limite_superior:
            prediccion = random.randint(limite_inferior, limite_superior)
        else:
            prediccion = limite_inferior  # o limite_superior, ya que son iguales
        
        #Obtener respuesta del usuario
        respuesta = input(f"La predicción de la computadora es {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
        
        if respuesta == "a":
            limite_superior = prediccion -1 
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    print(f"Siiii! La computadora adivinó tu número {prediccion} correctamente!")
    
    
adivina_el_numero_computadora(10) # Llamada a la función con el rango de números del 1 al 10
    