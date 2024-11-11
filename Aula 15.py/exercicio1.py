grupo={"jamilizinha":{"idade":21},"Duda":{"idade":23}, "Alê":{"idade":33},"pedro":{"idade":51},"raquel":{"idade":31}}
print(grupo["Alê"]["idade"])

dic={}
dic={"jamilizinha":21,"Duda":23, "Alê":33, "pedro":51,"raquel":31}
for i in dic.values():
    print (i)


dic={}
dic={"jamilizinha":21,"Duda":23, "Alê":33, "pedro":51,"raquel":31}
for i in dic.values():
    print (i, " - ", dic[i])