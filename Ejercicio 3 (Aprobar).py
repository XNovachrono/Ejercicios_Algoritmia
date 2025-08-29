# Programa que determina si un estudiante aprobó o reprobó una materia

# Entradas:
# Solicita al usuario la nota del estudiante (número entre 0 y 100).
# Salidas:
# Indica si el estudiante aprobó o reprobó. Si la entrada no es válida, muestra un mensaje de error.

# Procesos:
# Verifica si la nota es mayor o igual a 60 para aprobar.

print("Este algoritmo te dirá si un estudiante aprobó o reprobó.")
input("Presiona la tecla Enter para continuar...")

try:
    # Entrada: solicita nota
    nota = float(input("Ingresa la nota del estudiante (de 0 a 100): "))

    # Proceso: verifica si aprobó
    if nota >= 60:
        # Salida: aprobó
        print(f"El estudiante con nota de {nota} aprobó la materia.")
    else:
        # Salida: reprobó
        print(f"El estudiante con nota de {nota} reprobó la materia.")
except ValueError:
    # Salida: error de entrada
    print("Entrada no válida. Por favor, ingresa un número para la nota.")