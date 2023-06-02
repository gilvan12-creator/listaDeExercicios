listNumb = []
quant = 0
for i in range(20):
    numb=int(input("Digite um valor: "))
    listNumb.append(numb)
print(listNumb)
for i in listNumb:
    if i < 0:
        listNumb[quant] = 0
        quant+=1
    else:
        quant+=1
print(listNumb)
