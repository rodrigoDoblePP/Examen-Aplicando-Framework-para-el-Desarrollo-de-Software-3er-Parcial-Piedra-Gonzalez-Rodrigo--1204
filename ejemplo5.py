print (" ")
print ("Piedra Gonzalez Rodrigo #1204")
print (" ")

import os
from time import sleep

# Función para mostrar el menú
def menu():
    print("...... MENU .......")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    print("/////////////////////")

# Lista global de contactos
miLista = []

# Función para añadir un contacto a la lista
def anadirContacto(nombre):
    miLista.append(nombre)

# Función para mostrar la lista de contactos
def mostrarlista():
    for i, contacto in enumerate(miLista):
        print(f"{i+1}. {contacto}")

# Función para buscar un contacto en la lista
def buscarContacto(nombre):
    if nombre in miLista:
        print("Sí existe")
    else:
        print("No existe")

# Función para editar un contacto
def editarContacto(nombreQuitar, nombreNuevo):
    if nombreQuitar not in miLista:
        print("No existe")
    else:
        for i in range(len(miLista)):
            if miLista[i] == nombreQuitar:
                miLista[i] = nombreNuevo
                print("Nombre modificado!")
    mostrarlista()

# Menú principal
menu()

start = True
while start:
    try:
        elegir = int(input("Opción >> "))  # Entrada de opción

        if elegir == 1:  # Añadir contacto
            anade = input("Dime nombre a agregar: ")
            anadirContacto(anade)
            print(f"{anade} añadido con éxito.")
            print("Lista actualizada.")
        elif elegir == 2:  # Mostrar lista de contactos
            if len(miLista) <= 0:
                print("Lista está vacía.")
            else:
                print("Lista actualizada:")
                mostrarlista()
        elif elegir == 3:  # Buscar contacto
            nombre = input("Nombre a buscar: ")
            buscarContacto(nombre)
        elif elegir == 4:  # Editar contacto
            nombrequitar = input("Nombre que deseas modificar: ")
            nombreNuevo = input("Nombre nuevo: ")
            editarContacto(nombrequitar, nombreNuevo)
        elif elegir == 5:  # Salir
            print("Adiós")
            start = False
        else:
            print("Opción incorrecta.")
            sleep(2)  # Espera de 2 segundos antes de volver a mostrar el menú
    except Exception as e:
        print(f"Error: {e}")
        start = False  # Salir en caso de error
