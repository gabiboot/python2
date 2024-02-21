"""Crea una clase llamada ContadorPalabras que tenga los siguientes métodos:

- __init__: El constructor que inicializa un atributo contador en 0.
- contar: Un método que toma una cadena de texto como argumento y cuenta cuántas palabras 
          contiene esa cadena. Debe incrementar el contador en la cantidad de palabras encontradas.
- obtener_contador: Un método que devuelve el valor actual del contador.

A continuación, crea una instancia de la clase ContadorPalabras, utiliza el método contar 
para contar palabras en una cadena de texto y luego muestra el resultado utilizando el método 
obtener_contador."""

class ContadorPalabras:
    def __init__(self):
        self.contador = 0

    def contar(self, texto):
        # Dividir la cadena en palabras usando el espacio como separador
        palabras = texto.split()

        # Incrementar el contador con la cantidad de palabras encontradas
        self.contador += len(palabras)
        return self.contador

    def obtenerContador(self):   
         return self.contador 

#instancia de clase
contaPala = ContadorPalabras()

#ingreso de texto
texto = input("Ingrese texto -> ")

# Llamar al método obtener_contador para obtener el valor actual del contador
contaPala.contar(texto)

valor = contaPala.obtenerContador()
#Imprimir el resultado
print(valor)