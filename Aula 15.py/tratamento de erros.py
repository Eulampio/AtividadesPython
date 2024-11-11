try:
    a=int(input("digite uma palavra"))
except:
    print ("digite apenas numeros")


try:
    a=int(input("digite uma palavra"))
except ValueError:
    print ("digite apenas numeros")
except:
    print ("errro desconhecido")


try:
    a=int(input("digite uma palavra"))
except ValueError:
    print ("digite apenas numeros")
except:
    print ("errro desconhecido")
finally:
    print("final do algoritimo")