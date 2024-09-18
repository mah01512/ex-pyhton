lado1= float(input("digite o primeiro lado: "))
lado2= float(input("digite o segundo lado: "))
lado3= float(input("digite o terceiro lado: "))

if lado1==lado2==lado3:
  print("o triângulo é equilátero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
  print("o triângulo é isósceles")
else:
  print("o triângulo é escaleno")