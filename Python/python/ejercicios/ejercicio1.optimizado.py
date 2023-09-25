eCurso=1.5
mCurso=2.5
pCurso=4
MCurso=7

d1= 100-(eCurso/mCurso)*100
print(f'La diferencia porcentual respecto al curso más rapido es {round(d1,2)}%')

d2= 100-(eCurso/pCurso)*100
print(f'La diferencia porcentual respecto al curso promedio es {round(d2,2)}%')

d3= 100-(eCurso/MCurso)*100
print(f'La diferencia porcentual respecto al curso más lento es {round(d3,2)}%')