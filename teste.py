listNumb = []
numb = int(input("Digite um valor: "))
quant = 2
while(quant <= numb):
    if numb % quant == 0:
        listNumb.append(quant)
        numb = numb // quant
    elif(numb % quant != 0):
        quant += 1
print(listNumb)

quantVeto = {}
for i in listNumb:
    if i in quantVeto:
        quantVeto[i] += 1
    else:
        quantVeto[i] = 1    
for fator, cont in quantVeto.items():
    print(f"{fator} aparece {cont} vez(es)")

        
    




    

