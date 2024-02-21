class persona:
    def __init__(self, nombre, edad):
      self.nombre = nombre
      self.edad = edad

    def saludar(self):
       print(f"hola mi nombre es {self.nombre} y mi edad es {self.edad}")  

#Crear una instancia de la clase
persona1 = persona("juan", 32)

#llamar al metodo para instancia de la clase
persona1.saludar()

#crear otra instancia
persona2 = persona("rocio", 1)

#llamado al metodo para segunda instancia
persona2.saludar()