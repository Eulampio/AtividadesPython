class rtg:    
    def __init__(self,ladoA,ladoB):
        self.ladoA=ladoA
        self.ladoB=ladoB
    def mudar_valor_dos_lados(self,valor_lados):
        valor_lados= self.ladoA+self.ladoB*(2)
        print(valor_lados)

rtg1=rtg(2,5)
rtg1.mudar_valor_dos_lados("")
