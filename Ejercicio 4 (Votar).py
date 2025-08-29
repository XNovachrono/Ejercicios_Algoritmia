# Programa que determina si una persona cumple los requisitos para votar en Colombia

# Entradas:
# Solicita la edad (entero) y la nacionalidad (cadena de texto) de la persona.

# Salidas:
# Indica si la persona puede votar y, si no, la razón. Si la entrada es inválida, muestra un mensaje de error.

# Procesos:
# Verifica si la edad es mayor o igual a 18 y si la nacionalidad es colombiana.

print("Este algoritmo te dirá si una persona cumple los requisitos para votar.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita edad y nacionalidad
    edad = int(input("Ingresa la edad de la persona: "))
    nacionalidad = input("Ingresa la nacionalidad (ej: Colombiana): ")

    # Proceso: verifica requisitos
    if edad >= 18 and nacionalidad.lower() == "colombiana":
        # Salida: cumple requisitos
        print("La persona cumple con los requisitos para votar.")
    else:
        # Salida: no cumple requisitos
        print("La persona NO cumple con los requisitos para votar.")

        if edad < 18:
            print("Razón: Es menor de edad.")
        if nacionalidad.lower() != "colombiana":
            print("Razón: No es de nacionalidad colombiana.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida para la edad. Por favor, ingresa un número entero.")