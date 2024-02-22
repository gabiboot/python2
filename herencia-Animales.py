"""Crea una superclase llamada Animal con los siguientes métodos:
    __init__(self, nombre): Inicializa el nombre del animal.
    hablar(self): Debe ser un método abstracto (sin implementación) que represente el sonido que hace el animal. 
    Las subclases deben proporcionar una implementación para este método.

Luego, crea dos subclases, Perro y Gato, que hereden de Animal. En estas subclases, implementa el método hablar() 
para representar los sonidos típicos de un perro y un gato respectivamente (por ejemplo, "Guau" y "Miau").

Finalmente, crea instancias de ambas subclases y muestra el nombre y el sonido de cada animal en pantalla."""
from abc import ABC, abstractmethod

class animales:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    @abstractmethod
    def hablar(self):
        pass
    
class pato(animales):
    def hablar(self):
        return f"hola soy un {self.nombre}, mi sonido es {self.sonido} y suena cuek "

class perro(animales):
    def hablar(self):
        return f"hola soy un {self.nombre} mi sonido es {self.sonido} y suena guauguau"


#variable de control
Pato = pato("pato", "grasnar")
Perro = perro("perro", "ladrido")

print(f"es: {Pato.hablar()}")
print(f"es: {Perro.hablar()}")