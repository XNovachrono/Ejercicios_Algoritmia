# Programa que determina si una temperatura es adecuada para congelación

# Entradas:
# Solicita al usuario una temperatura en grados Celsius (número).

# Salidas:
# Indica si la temperatura es adecuada para congelación. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Verifica si la temperatura es menor o igual a 0°C.

print("Este algoritmo te dirá si una temperatura es adecuada para congelación.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita temperatura
    temperatura = float(input("Ingresa la temperatura en grados Celsius (°C): "))

    # Proceso: verifica congelación
    if temperatura <= 0:
        # Salida: adecuada para congelación
        print(f"La temperatura {temperatura}°C es adecuada para congelación.")
    else:
        # Salida: no adecuada para congelación
        print(f"La temperatura {temperatura}°C no es adecuada para congelación.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa un número para la temperatura.")