def imprimeMultiplos(n,mayor):
    i=1
    while(i<=mayor):
        print(n*i,"\t",end="")
        i+=1
    print()

i=1
while i<=6:
    imprimeMultiplos(i,1)
    i+=1
    

def imprimeTablaMult(mayor):
    i=1
    while(i<=mayor):
        imprimeMultiplos(i,i)
        i+=1

imprimeTablaMult(3)