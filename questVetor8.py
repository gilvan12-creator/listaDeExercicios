listNumb = []

for i in range(5):
    numb = int(input("Digite o valor: "))
    listNumb.append(numb)
    
menor = listNumb[0]
maior = listNumb[0]

for i in listNumb:
    if i >= maior:
        maior = i
    elif i <= menor:
        menor = i

print("Lista de valor\n{}".format(listNumb))
print("O maior valor é {}".format(maior))
print("O menor valor é {}".format(menor))
