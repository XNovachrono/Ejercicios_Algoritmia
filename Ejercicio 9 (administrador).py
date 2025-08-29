# Programa que verifica si un código de acceso corresponde a un administrador

# Entradas:
# Solicita al usuario un código de acceso (entero).

# Salidas:
# Indica si el acceso es concedido o denegado. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Compara el código ingresado con el código secreto.

print("Este algoritmo verifica si un código de acceso corresponde a un administrador.")
input("Presiona la tecla Enter para continuar...")

CODIGO_SECRETO = 12345

try:
    # Entrada: solicita código
    codigo_ingresado = int(input("Ingresa el código de acceso: "))

    # Proceso: verifica código
    if codigo_ingresado == CODIGO_SECRETO:
        # Salida: acceso concedido
        print("Acceso concedido. ¡Eres un administrador!")
    else:
        # Salida: acceso denegado
        print("Acceso denegado. El código ingresado es incorrecto.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa un número entero para el código.")