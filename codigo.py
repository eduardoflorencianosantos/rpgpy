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

escolha = input("Digite 'continue' para avançar: ")
while escolha != "continue":
    escolha = input("Não foi possível avançar. Digite 'continue': ")
if escolha == "continue":
    print("Pode avançar, boa sorte!")
