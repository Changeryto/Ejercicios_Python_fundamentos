class Aritmetica:
    """Clase aritmética para realizae suma, resta, etc."""
    def __init__(self, operando1, operando2):
        self.operando1 = operando1 #Inicializando atributos
        self.operando2 = operando2
        
    def sumar(self):
        """Se realiza la operación con los atributos de la clase"""
        return self.operando1 + self.operando2
    
    def restar(self):
        return self.operando1 - self.operando2
    
    def multiplicar(self):
        return self.operando1 * self.operando2
    
    def dividir(self):
        return self.operando1 / self.operando2
        
#Crear un objeto
aritmetica = Aritmetica(2, 4)
print("Resultado de la suma:", aritmetica.sumar())
print("Resultado de la resta:", aritmetica.restar())
print("Resultado de la división:", aritmetica.dividir())
print("Resultado de la multiplicación:", aritmetica.multiplicar())

a = float(input("Número 1: "))
b = float(input("Número 2: "))
aritmetica2 = Aritmetica(a,b)
print("Resultado de la suma", aritmetica2.sumar())
print("Resultado de la reesta:", aritmetica2.restar())
print("Resultado de la multiplicación", aritmetica2.multiplicar())
print("Resultado de la división:", aritmetica2.dividir())