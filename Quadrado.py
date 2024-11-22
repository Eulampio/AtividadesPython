class Qdd:    
    def __init__(self,lado):
        self.lado=lado
    def mostra_area(self):
        area=self.lado**2
        print(area)
    def mudar_valor_lado(self, mudar_lado):

        self.lado=mudar_lado
        print(self.lado)
        area= self.lado**2
        print(area)
vlo=Qdd(2)
vlo.mostra_area()
vlo.mudar_valor_lado(7)

