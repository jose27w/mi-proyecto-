NOTA_MINIMA = 10.5

def leer_nota(numero):
    nota = float(input(f"Nota {numero}: "))
    while nota < 0 or nota > 20:
        nota = float(input("Nota invalida (0-20). Ingresa de nuevo: "))
    return nota

def calcular_promedio(notas):
    return sum(notas) / len(notas)

def esta_aprobado(promedio):
    return promedio >= NOTA_MINIMA

def main():
    print("Gestor de notas v4")
    nombre = input("Nombre del alumno: ")
    print(f"Hola, {nombre}")

    notas = []
    for i in range(3):
        notas.append(leer_nota(i + 1))

    promedio = calcular_promedio(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")
    print("Estado:", "APROBADO" if esta_aprobado(promedio) else "DESAPROBADO")

if __name__ == "__main__":
    main()