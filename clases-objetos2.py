class calculadora:
    #declaracion de metodo de inicializacion
    def __init__(self, numero):
        self.resultado = numero

  #metodos encargados de realizar las operaciones matematicas      
    def sumar(self, numero):
        self.resultado += numero    #aparte de almacenar y sumar va a cambiar el resultado

    def restar(self, numero):
        self.resultado -= numero

    def multiplicar(self, numero):
        self.resultado *= numero

    def dividir(self, numero):
        if numero !=0:
            self.resultado /= numero
        else:
            print("Error, no se puede dividir por 0") 

#metodo para pasar el resultado
    def resultado(self):
        return self.resultado
    
#Objetos que van a interpretar esta clase, con valor inicial de 0
calculo = calculadora(0)
calculo.sumar(5)
calculo.multiplicar(3)
calculo.dividir(4)
calculo.restar(1)

#variable de control que va a representar el resultado
Resultado = calculo.resultado
print(Resultado)