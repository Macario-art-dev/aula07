numeros = []
quantidade = int(input("quantos números você quer digitar: "))
for i in range(quantidade):
    numero = int(input(f"escolha o {i+1}º número: "))
    numeros.append(numero)
print(f"números digitados: {numeros}")

print("\nNúmros impares")
for i in numeros:
    if i %2 == 1:
        print(i)

print("Números e ordem crescente\n")
numeros.sort()  
print(f"Numeros {numeros}")
print("Ordem decrescente\n") 
numeros.sort(reverse=True) 
print(f"Ordem decrescente {numeros}")
print("Elimine um Número")  
numero_r= int(input("elimine um numero: "))
numeros.remove(numero_r)
numeros.sort(reverse=True)
print(f"numeros eliminados: {numeros}")