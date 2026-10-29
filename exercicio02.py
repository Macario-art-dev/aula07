print("O usuário escolhe os números")
numeros = []
quantidade = int(input("quantos números você quer digitar na lista? "))
for i in range(quantidade):
    numero = int(input(F"Digite o {i+1}º número:  "))
    numeros.append(numero)
print(f"Números digitados: {numeros}")

#mostrar somente os números pares
print("Números pares")
for i in numeros:
    if i %2 ==0:
        print(i)
        
