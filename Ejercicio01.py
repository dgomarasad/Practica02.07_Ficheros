#Escribir una función que pida un número entero entre 1 y 10 y guarde en un
#fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, 
#donde n es el número introducido.
def guardar_tabla_multiplicar():
    n = int(input("Introduce un número entero entre 1 y 10: "))
    if 1 <= n <= 10:
        with open(f"tabla-{n}.txt", "w") as fichero:
            for i in range(1, 11):
                fichero.write(f"{n} x {i} = {n * i}\n")
        print(f"Tabla del {n} guardada en tabla-{n}.txt")
    else:
        print("El número debe estar entre 1 y 10.")

guardar_tabla_multiplicar()

