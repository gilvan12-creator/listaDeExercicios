
def close(value):
    value = value.lower();
    
    if(value not in ["s", "sim", "yes"]):
        return(True)


    


while(True):
    print("================================= \n  Conversão de Dolar para Real\n================================= ");
    print("1 - Real Para Dolar\n" "2 - Dolar para Real");
    
    
    
    
    option = input("Digite a Opção de Sua Escolha: ");
    
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
                
       
        
        loop = input("Deseja converter outro valor: ");
        
        if(close(loop)):
            break;
           
    elif(option != int):
        print("Valor Digitado Invalido, Favor Digite Apenas Numeros")
        
    else:
        print("Valor Digitado Invalido, Favor Digite uma Opção Valida")
