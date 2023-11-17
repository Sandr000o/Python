eCurso=1.5
mCurso=2.5
pCurso=4
MCurso=7


d1=100-(eCurso/mCurso)*100
print(f'La diferencia porcentual respecto al curso más rapido es {d1}%')
d2=100-(eCurso/pCurso)*100
print(f'La diferencia porcentual respecto al curso promedio es {d2}%')
d3=100-(eCurso/MCurso)* 1000 // 10
print(f'La diferencia porcentual respecto al curso más lento es {d3}%')

