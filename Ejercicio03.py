#Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero
#tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla
#la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por
#pantalla informando de ello.
def mostrar_linea_tabla():
    n = int(input("Introduce un número entero entre 1 y 10 para la tabla: "))
    m = int(input("Introduce un número entero entre 1 y 10 para la línea: "))
    
    try:
        with open(f"tabla-{n}.txt", "r") as fichero:
            lineas = fichero.readlines()
            print(lineas[m - 1].strip())
    except FileNotFoundError:
        print(f"El fichero tabla-{n}.txt no existe.")
    except IndexError:
        print(f"La línea {m} no existe en el fichero tabla-{n}.txt.")

mostrar_linea_tabla()
