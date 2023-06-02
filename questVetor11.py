listNumb = []
listApro = []
listRep = []
quant = 1
while(quant <= 5):
    numb =int(input("Digite a {} nota: ".format(quant)))
    if (numb >= 0 and numb <=10):
        listNumb.append(numb)
        quant+=1
    else:
        print("Nota invalida\nFavor digite um valor entre 0 e 10")
soma = 0
for i in listNumb:
    soma += i
media = soma/len(listNumb)   
print("A media geral da turma foi de {}".format(media))

for i in listNumb:
    if i < media:
        listRep.append(i)
    elif i >= media:
        listApro.append(i)
print("A quantida de alunos aprovados {}".format(len(listApro)))
print(listApro)
print("A quantidade de alunos reprovados foi de {}".format(len(listRep)))
print(listRep)

        
