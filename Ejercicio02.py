#Escribir una función que pida un número entero entre 1 y 10, lea el fichero
#tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número
#introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar
#un mensaje por pantalla informando de ello.

def leer_tabla_multiplicar():
    n = int(input("Introduce un número entero entre 1 y 10: "))
    try:
        with open(f"tabla-{n}.txt", "r") as fichero:
            print(fichero.read())
    except FileNotFoundError:
        print(f"El fichero tabla-{n}.txt no existe.")

leer_tabla_multiplicar()
