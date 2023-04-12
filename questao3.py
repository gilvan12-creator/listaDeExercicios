def close(value):
    value = value.lower();
    
    if(value not in ["s", "sim", "yes"]):
        return(True)


while(True):
    print("==============================================\n   Calculo de área e perimetro do Retangulo \n============================================== ");
        
    alt = float(input("Digite a Altura "));
    base = float(input("Digite a Base "));     
         
    if(alt !=  str and base != str):
        area = alt * base;
        peri = (2 * alt) + (2 * base);
        print("A área do Retangulo é %.2f" %area);
        print("O perimetro do Retangulo é %.2f" %peri);
        
    else:
        print("teste");
        
    loop = input("\nDeseja Fazer outro calculo: ");
        
    if(close(loop)):
        break;
       
        
    
   
        
            
        
        
     
        
