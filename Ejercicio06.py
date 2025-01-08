#Escribir un programa para gestionar un listín telefónico con los nombres y
#los teléfonos de los clientes de una empresa. El programa debe  incorporar 
#funciones para crear el fichero con el listín si no existe, para consultar el
#teléfono de un cliente, añadir el teléfono de un nuevo cliente y eliminar el 
#teléfono de un cliente. El listín debe estar guardado en el fichero de texto
#listin.txt donde el nombre del cliente y su teléfono deben aparecer separados 
#por comas y cada cliente en una línea distinta.
def crear_listin():
    open("listin.txt", "a").close()  # Crea el archivo si no existe

def consultar_telefono():
    nombre = input("Introduce el nombre del cliente: ")
    try:
        with open("listin.txt") as f:
            for linea in f:
                cliente, telefono = linea.strip().split(",")
                if cliente == nombre:
                    print(f"Teléfono de {nombre}: {telefono}")
                    return
        print("Cliente no encontrado.")
    except FileNotFoundError:
        print("El fichero no existe.")

def agregar_cliente():
    nombre = input("Introduce el nombre del cliente: ")
    telefono = input("Introduce el teléfono: ")
    with open("listin.txt", "a") as f:
        f.write(f"{nombre},{telefono}\n")

def eliminar_cliente():
    nombre = input("Introduce el nombre del cliente a eliminar: ")
    try:
        with open("listin.txt") as f:
            lineas = f.readlines()
        with open("listin.txt", "w") as f:
            for linea in lineas:
                if linea.split(",")[0] != nombre:
                    f.write(linea)
        print(f"Cliente {nombre} eliminado." if any(nombre in l for l in lineas) else "Cliente no encontrado.")
    except FileNotFoundError:
        print("El fichero no existe.")

def menu():
    while True:
        print("\n1. Crear listín\n2. Consultar teléfono\n3. Agregar cliente\n4. Eliminar cliente\n5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1": crear_listin()
        elif opcion == "2": consultar_telefono()
        elif opcion == "3": agregar_cliente()
        elif opcion == "4": eliminar_cliente()
        elif opcion == "5": break

menu()

    
