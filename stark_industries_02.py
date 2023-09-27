#Escobar Tobias Fabricio 
#1-J
#Clase 3

#Ejercicio Integrador Data Stark #02 (segunda entregada)

from os import system
system("cls")

from funciones_02 import *

def mostrar_menu():
    for opcion in menu:
        print(opcion)

menu = ["\n1.Mostrar nombres de heroes de genero NB: ", "2.Mostrar heroe mas alto del genero F: ",
        "3.Mostrar heroe mas alto del genero M: ", "4.Mostrar heroe mas debil del genero M: ", 
        "5.Mostrar heroe mas alto del genero NB: ", "6.Mostrar fuerza promedio del genero NB: ",
        "7.Mostrar la cantidad de cada tipo de color de ojos: ", "8.Mostrar la cantidad de cada tipo de color de pelo: ",
        "9.Mostrar los heroes agrupados por color de ojos: ", "10.Mostrar los heroes agrupados por inteligencia: ",
        "11.Salir: \n"]

seguir = True
while seguir:

    mostrar_menu()
    
    while True:
        respuesta = input("Ingresa una opcion: ")
        if respuesta.isdigit():
            respuesta = int(respuesta)
            if 1 <= respuesta <= 11:
                break
        print("Opción no válida. Ingresa un número del 1 al 11.")

    match respuesta:
        case 1:
            mostrar_nombres_nb(lista_personajes)
        case 2:
            genero = "F"
            mostrar = heroe_mas_alto(lista_personajes, genero)
            print(f"El heroe mas alto del genero M es: {mostrar}")
        case 3:
            genero = "M"
            mostrar = heroe_mas_alto(lista_personajes, genero)
            print(f"El heroe mas alto del genero F es: {mostrar}")
        case 4:
            genero = "M"
            mostrar = heroe_mas_debil(lista_personajes, genero)
            print(f"El heroe mas debil del genero M es: {mostrar}")
        case 5:
            genero = "NB"
            mostrar = heroe_mas_debil(lista_personajes, genero)
            print(f"El heroe mas debil del genero NB es: {mostrar}")
        case 6:
            genero = "NB"
            promedio_fuerza_nb(lista_personajes, "NB")
        case 7:
            mostrar = tipo_de_color(lista_personajes, "color_ojos")
            print(mostrar)
        case 8:
            mostrar = tipo_de_color(lista_personajes, "color_pelo")
            print(mostrar)
        case 9:
            mostrar = agrupar_por_caracteristica(lista_personajes, "color_ojos")
            print(mostrar)
        case 10:
            mostrar = agrupar_por_caracteristica(lista_personajes, "inteligencia")
            print(mostrar)
        case 11:
            seguir = False