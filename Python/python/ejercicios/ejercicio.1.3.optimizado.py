eCurso=1.5
mCurso=2.5
pCurso=4
MCurso=7



v1=(mCurso/eCurso)*10
v1=round(v1,2)
print(f'Ver 10 horas de este curso equivale a ver {v1} horas del curso más rápido')
v2=(pCurso/eCurso)*10
v2=round(v2,2)
print(f'Ver 10 horas de este curso equivale a ver {v2} horas del curso promedio')
v3=(MCurso/eCurso)*10
v3=round(v3,2)
print(f'Ver 10 horas de este curso equivale a ver {v3} horas del curso más lento')
v4=(eCurso/pCurso)*10
v4=round(v4,2)
print(f"Ver 10 hora del curso promedio equivale a ver {v4} horas del curso de dalto")