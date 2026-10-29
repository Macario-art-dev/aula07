print("\nEntre com os nomes e coloque em ordem alfabética crescente")
nomes= []
quantidade = int(input("QUANTOS NOMES QUER INSERIR? "))
for i in range(quantidade):
    nome = input(f"{i+1}º Nome: ")
    nomes.append(nome)
nomes.sort(reverse=True)
print(f"Nomes em ordem alfabética {nomes}".title())

nome_remover = input("Escolha um nome para remover da lista: ")
nomes.remove(nome_remover)
print(f"Nomes: {nomes}".title())
