# Programa que determina si un número ingresado es negativo o no

# Entradas:
# Solicita al usuario que ingrese un número (puede ser decimal o entero).

# Salidas:
# Muestra si el número es negativo o no. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Convierte la entrada a número y verifica si es menor que cero.

print("Este algoritmo determina si un número es negativo o no.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita número
    num = float(input("Ingresa un número: "))

    # Proceso: verifica si es negativo
    if num < 0:
        # Salida: es negativo
        print(f"El número ingresado ({num}) es negativo.")
    else:
        # Salida: no es negativo
        print(f"El número ingresado ({num}) no es negativo.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa un número.")