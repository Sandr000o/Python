

texto=input("Ingrese el texto que va a decir : ")
palabras=texto.split(" ")
cPalabras=len(palabras)

pxs=cPalabras/2

print(f'Para decir el texto completo que consta de {cPalabras} tardara {pxs} segundos')

if(pxs>60):
    print("Para flaco,tampoco te pedí un testamento")

dalto=pxs*0.7

print(f'Dalto tardaría {dalto} segundo en decir el texto que consta de {cPalabras}')