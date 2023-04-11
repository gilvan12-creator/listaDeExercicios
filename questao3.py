print("================================= \n"
        "  Conversão de Dolar para Real \n"
        "================================= ");
print("1 - Real Para Dolar\n" "2 - Dolar para Real");

option = int(input("Digite a Opção de Sua Escolha: "));




if(option == 1 or option == 2):
    
    match option:
        case 1:
            valor = float(input("Digite o Valor em Real: "));
            calc = valor / 3.9
            print("O valor Digitado equivale a US$ %.2f" %calc)
    
        case 2:
            valor = float(input("Digite o Valor em Dolar: "));
            calc = valor * 3.9
            print("O valor Digitado equivale a R$ %.2f" %calc)
            
    print("================================= \n1 - Para Converter outro Valor \n2 - Para Encerrar o Sistema\n=================================\n")
    
    loop = int(input("Digite a Opção de Sua Escolha: "));
       
        
else:
    print("Valor Digitado Invalido")


   
