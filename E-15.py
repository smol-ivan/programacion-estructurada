"""
Ejercicio 1.
"""
"""
auth = False
while not auth:
  x = False
  while not x:
    base = input('Ingrese un valor para la base: ')
    if base.isnumeric() and int(base) > 0:
      x = True

  n = False
  while not n:
    exponente = input('Ingrese un valor para el exponente: ')
    if exponente.isnumeric() and int(exponente) >= 0:
      n = True

  if n and x == True:
    auth = True

if exponente != 0:
  total = 1
  for i in range(0, (int(exponente))):
    total = total * int(base)
  print(total)
else:
  print(1)
"""

"""
Ejercicio 2.
"""
numero = False
while not numero:
  n = input('Ingrese el factorial a calcular: ')
  if n.isnumeric() and int(n) >= 0:
    numero = True

total = 1
for i in range(int(n), 0, -1):
  total = total * i

print('El valor del factorial es: ' + total)

