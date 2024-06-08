class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def moverse(self):
        return f"{self.nombre} se está moviendo"

class Perro(Animal):
    def ladrar(self):
        return f"{self.nombre} dice: ¡Guau!"

# Uso
perro = Perro("pepito")
print(perro.moverse())
print(perro.ladrar())
