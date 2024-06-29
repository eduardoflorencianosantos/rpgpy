import csv

with open("apresentacao.txt") as minhaApresentacao:
	minhaVariavel = minhaApresentacao.read()
print(minhaVariavel)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

planilha = []

def imprimirAventuras(planilha):
	
	for eduardo in planilha:
		print(f"Aventura: {eduardo['Aventura']}")


def aventuraEspecifica(planilha, elementoEspecifico):
	
	for eduardo in planilha:
		if eduardo == elementoEspecifico:
			print(f"Aventura: {eduardo['Aventura']}")


def removerAventura(planilha, elementoRemovido):
	
	for eduardo in planilha:
		if eduardo != elementoRemovido:
			print(f"Aventura: {eduardo['Aventura']}")


def funcaoContinue():
	escolha = input("Digite 'continue' para avançar: ")
	
	while escolha != "continue":
    		escolha = input("Não foi possível avançar. Digite 'continue': ")
	
	if escolha == "continue":
    		print("Pode avançar, boa sorte!")
	
	return escolha


with open("rpg.csv", "r") as minhaPlanilha:
	novaVariavel = csv.DictReader(minhaPlanilha)
	
	for n in novaVariavel:
		planilha.append(n)

print(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

imprimirAventuras(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elementoEspecifico = planilha[9]

aventuraEspecifica(planilha, elementoEspecifico)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

elementoRemovido = planilha[19]

removerAventura(planilha, elementoRemovido)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

funcaoContinue()