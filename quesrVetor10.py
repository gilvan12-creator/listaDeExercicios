listNumb = []
quant = 1
while(quant <= 15):
    numb = int(input("Digite a {} nota: ".format(quant)));
    if numb >= 0 and numb <= 10:
        listNumb.append(numb)
        quant+=1
    else:
        print("Valor invalido favor digite um valor entre 0 e 10")
soma = 0
for i in listNumb:
    soma += i
media = soma / len(listNumb)
print("A media geral foi de {}".format(media))
