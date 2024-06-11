with open("apresentacao.txt") as minhaApresentacao:
	minhaVariavel = minhaApresentacao.read()
print(minhaVariavel)

import csv
planilha = []

def imprimir(planilha):
	for eduardo in planilha:
		print(f"Aventura: {eduardo['Aventura']}")

with open("rpg.csv", "r") as minhaPlanilha:
	novaVariavel = csv.DictReader(minhaPlanilha)
	for n in novaVariavel:
		planilha.append(n)

print(planilha)

imprimir(planilha)