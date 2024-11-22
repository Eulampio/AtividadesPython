class ControleRemoto:    
    def __init__(self,cor,altura,profundidade,largura):
        self.cor=cor
        self.altura=altura
        self.profundidade=profundidade
        self.largura=largura

        def mudar_canal(self,botao):
            botao=float(input())
            if botao=="+":
                print("almentar canal")
            elif botao=="-":
                print("diminuir canal")
            elif botao== "D" or botao =="d":
                print("desligar")
            elif botao== "L" or botao =="l":
                print("desligar")
            else:
                print("valor Invalido")
                
