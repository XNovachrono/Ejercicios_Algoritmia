# Programa que determina si un número está fuera del rango [-100, 100]

# Entradas:
# Solicita al usuario un número (puede ser decimal o entero).

# Salidas:
# Indica si el número está dentro o fuera del rango. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Verifica si el número está fuera del rango especificado.

print("Este algoritmo te dirá si un número está fuera del rango [-100, 100].")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita número
    num = float(input("Ingresa un número: "))

    # Proceso: verifica rango
    if num > 100 or num < -100:
        # Salida: fuera de rango
        print(f"El número {num} está fuera del rango.")
    else:
        # Salida: dentro de rango
        print(f"El número {num} está dentro del rango.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa un número.")