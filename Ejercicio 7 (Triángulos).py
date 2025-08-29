# Programa que determina el tipo de triángulo según las longitudes de sus lados

# Entradas:
# Solicita al usuario las longitudes de los tres lados (números).

# Salidas:
# Indica el tipo de triángulo. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Compara los lados para determinar si es equilátero, isósceles o escaleno.

print("Este algoritmo te dirá si un triángulo es equilátero, isósceles o escaleno.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita lados
    lado1 = float(input("Ingresa la longitud del primer lado: "))
    lado2 = float(input("Ingresa la longitud del segundo lado: "))
    lado3 = float(input("Ingresa la longitud del tercer lado: "))

    # Proceso: determina tipo
    if lado1 == lado2 and lado2 == lado3:
        # Salida: equilátero
        print("El triángulo es equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        # Salida: isósceles
        print("El triángulo es isósceles.")
    else:
        # Salida: escaleno
        print("El triángulo es escaleno.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa números para las longitudes.")