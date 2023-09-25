
#Creando una función simple con un parámetro
def saludar(nombre):
    print(f'Hola {nombre} bienvenido')
    
saludar("Juan")

#Definir sexo
def salu(nombre,sexo):
    sexo=sexo.lower()
    if sexo=="mujer":
        adjetivo="maestra"
        
    elif sexo=="hombre":
        adjetivo="maestro"
    else:
        adjetivo="crack"
    
    print(f'Hola {adjetivo} {nombre} como andas')
        
salu("Juan","Hombre")
salu("Cami","mujer")
salu("Arturo","nose")

#Crear funciones que retornan valores

def crearContraseñasRandom(num):
    chars="abcdefghij"
    numEntero=str(num)
    num= int(numEntero[0])
    c1=num-2
    c2=num
    c3=num-5
    clave=f'{chars[c1]}{chars[c2]}{chars[c3]}{num*2}'
    return(clave,num)
    
clave,primerNumero=crearContraseñasRandom(4)
frase= f'Tu contraseña nueva es {clave} '
print(frase)
print(f'El número utilizado para generar la contraseña fue : {primerNumero}')