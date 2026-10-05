NOTA_MINIMA = 10.5

class Alumno:
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def tiene_notas(self):
        return len(self.notas) > 0

    def promedio(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def nota_mas_alta(self):
        return max(self.notas)

    def nota_mas_baja(self):
        return min(self.notas)

    def esta_aprobado(self):
        return self.promedio() >= NOTA_MINIMA

    def estado(self):
        return "APROBADO" if self.esta_aprobado() else "DESAPROBADO"