class vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def arrendar(self):
        return f"marca_: {self.marca}, modelo_: {self.modelo} esta encendido"    
    
#clase hijo con datos heredados    
class coche(vehiculo):
  
  def acelerar(self):
      return f"{self.marca}, modelo_: {self.modelo} ---- {self.acelerar}"
  
class moto(vehiculo):
   def retroceso(self):
       return f" {self.marca}, modelo_: {self.modelo} ....... esta retrocediendo {self.retroceso} " 
       

#variable de control
Coche = coche("toyota", "Yaris")
Moto = moto("yamaha", "150") 

print(f"coche marca Y modelo : {Coche.marca} - {Coche.modelo}")
print(f"moto marca Y modelo : {Moto.marca} - {Moto.modelo}")

print(f"{Moto.retroceso()}")
print(f"{Moto.arrendar()}")
