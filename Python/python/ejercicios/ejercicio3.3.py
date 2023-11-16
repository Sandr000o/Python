

def fibonacci(num):
    a,b=0,1
    lista=[]
    for i in range(num):
        if a+b> num :
            print(lista)
            return lista
        else :
            
            lista.append(b)
            print(lista)
            a,b =b,a+b


resultado =fibonacci(20)
print(resultado)
