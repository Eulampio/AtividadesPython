class CadastroNetflix:    
    def __init__(self,Nome,Email,Cpf,Plano,CartaoDeCredito):
        self.Nome=Nome
        self.Email=Email
        self.Cpf=Cpf
        self.Plano=Plano
        self.CartaoDeCredito=CartaoDeCredito

    def exibir(self):
        print(self.Nome)


        