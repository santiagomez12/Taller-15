#taller 15
a=int(input("digite un numero:"))
def es_par(numero):
    if a%2==0:
        return True
    else:
        return False
b=es_par(a)
print("el numero es ",b) 
#numero primo 
a=int(input("digite un numero:")) 
def es_primo(numero):
    if a>1:
        contador=0
        for c in range (2,a):
            resto=a%c
            if resto ==0:
                contador+=1
        if contador ==0:
            return True
        else:
            return False
p=es_primo(a)
print("el numero es ",p)   
#operaciones condicionadas
x=int(input("digite un numero:"))
if x<50:
    def_multiplo2=x*10
    
    for i in range(1,def_multiplo2+1):
        if i%x!=0:
            print(i)
        else:
            print("_")
else:
    print("El numero ingresado es mayor a 50")
    
y=int(input("digite un numero:"))
if y>50:
    def_5=a*5
    for u in range(1,def_5+1):
        print("5 veces el numero:",u)
else :
    print("el numero es menor a 50")
#Tabla de multiplicar hasta 50 
a=int(input("digite numero:")) 
def imprimir_tabla(tabla):
    if a>0:
        for m in range (1,51):
        print(a,"*",m,"=",a*m)
n=imprimir_tabla(a)
print (n)

                               
                    
        
                
