#tradutor1.clear() remove todos elementos do dicionário

tradutor ={}
tradutor["pineapple"]= "abacaxi"


tradutor1={}
tradutor1={"pineapple":"abacaxi","apple":"maça", "orange":"laranja"}
print ("pineapple" in tradutor)

print ("laranja" in tradutor1.values()) # variavel.values imprimindo valores do dicinário

#alterando o valor na chave 

tradutor1={"pineapple":"abacaxi","apple":"maça", "orange":"laranja"}
print(tradutor1)
tradutor1 ["apple"] = "goiaaba"
print (tradutor1)

dados= {"crossfox":{"km":35000,"ano":2005},"DS5":{"km":17000,"ano":2015},"Fusca":{"km":130000,"ano":1979},"Jetta":{"km":56000,"ano":2011},"Passat":{"km":62000,"ano":1999}}
print (dados["Fusca"])

print(dados.get("Gol","veiculo não encontrado")) #get busca uma variavel em especifico

