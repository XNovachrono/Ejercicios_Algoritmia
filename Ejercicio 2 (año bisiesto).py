# Programa que determina si un año es bisiesto

# Entradas:
# Solicita al usuario que ingrese un año (entero).
#
# Salidas:
# Indica si el año es bisiesto o no. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Verifica si el año es divisible entre 4, no divisible entre 100, o divisible entre 400.

print("Este algoritmo determina si un año es bisiesto o no.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita año
    año = int(input("Ingresa un año (por ejemplo, 2024): "))

    # Proceso: verifica si es bisiesto
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        # Salida: es bisiesto
        print(f"El año {año} es bisiesto.")
    else:
        # Salida: no es bisiesto
        print(f"El año {año} no es bisiesto.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa un número entero para el año.")