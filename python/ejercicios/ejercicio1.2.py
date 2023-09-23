eCurso=1.5
pCurso=4
eCrudo=3.5
pCrudo=5

c1=round((eCrudo-eCurso)/eCrudo*100,1)
print(f'El porcentaje en que se reduce el material de este curso es  {c1}%')
c2=round((pCrudo-pCurso)/pCrudo*100,1)
print(f'El porcentaje en que se reduce el material de curso promedio es  {c2}%')
