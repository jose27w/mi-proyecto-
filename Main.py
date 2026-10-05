print("Gestor de notas v3")

nombre = input("Nombre del alumno: ")
print(f"Hola, {nombre}")

notas = []
for i in range(3):
    nota = float(input(f"Nota {i + 1}: "))
    while nota < 0 or nota > 20:
        nota = float(input("Nota invalida (0-20). Ingresa de nuevo: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
print(f"Promedio de {nombre}: {promedio:.2f}")

if promedio >= 10.5:
    print("Estado: APROBADO")
else:
    print("Estado: DESAPROBADO")
