with open("apresentacao.txt") as minhaApresentacao:
	minhaVariavel = minhaApresentacao.read()
print(minhaVariavel)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

import csv
planilha = []

def imprimirAventuras(planilha):
	for eduardo in planilha:
		print(f"Aventura: {eduardo['Aventura']}")

def aventuraEspecifica(planilha):
	print(planilha[9])

def removerAventura(planilha):
	for dudu in planilha:
		if 'Aventura' in dudu:
			del dudu['Aventura']
	return planilha

with open("rpg.csv", "r") as minhaPlanilha:
	novaVariavel = csv.DictReader(minhaPlanilha)
	for n in novaVariavel:
		planilha.append(n)

print(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

imprimirAventuras(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

aventuraEspecifica(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

resultado = removerAventura(planilha)
print(resultado)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

escolha = input("Escolha entre as opções a e b: ")
while escolha != "a" and escolha != "b":
    escolha = input("Seu imbecil, é só continue
if escolha == "a":
    print("Escolheu a")
elif escolha == "b":
    print("Escolha b")
