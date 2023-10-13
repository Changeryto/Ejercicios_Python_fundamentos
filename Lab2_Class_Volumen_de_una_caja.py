class Caja:
    def __init__(self, alto, ancho, largo):
        self.alto = alto
        self.ancho = ancho
        self.largo = largo
        
    def volumen(self):
        return (self.alto * self.largo * self.ancho)
    
al = float(input("¿Alto de la caja?: "))
an = float(input("¿Ancho de la caja?: "))
lar = float(input("¿Largo de la caja?: "))
caja = Caja(al, an, lar)
print("El volumen de la caja es", caja.volumen(), "Unidades")