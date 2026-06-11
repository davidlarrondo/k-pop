def sumar(v1,v2):
    resultado = v1+v2
    return resultado

def restar(v1,v2):
    resultado = v1-v2
    return resultado

valor1 = int(input("ingrese valor "))
valor2 = int(input("ingrese valor "))

print(f"el resultado es {sumar(valor1,valor2)}")
print(f"el resultado es {restar(valor1,valor2)}")