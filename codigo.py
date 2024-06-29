// Importa biblioteca para manipular csv
import csv

// Função que abre e lê o arquivo txt
with open("apresentacao.txt") as minhaApresentacao:
	minhaVariavel = minhaApresentacao.read()
// Imprime o arquivo txt
print(minhaVariavel)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

// Declara vetor vazio
planilha = []

// Função que imprime apenas 'Aventuras' da planilha
def imprimirAventuras(planilha):
	// Imprime cada linha do csv dicionarizado
	for eduardo in planilha:
		print(f"Aventura: {eduardo['Aventura']}")

// Função que imprime apenas uma 'Aventura' específica
def aventuraEspecifica(planilha, elementoEspecifico):
	// Imprime cada linha do csv dicionarizado
	for eduardo in planilha:
		if eduardo == elementoEspecifico:
			print(f"Aventura: {eduardo['Aventura']}")

// Função que remove apenas uma 'Aventura' específica
def removerAventura(planilha, elementoRemovido):
	// Imprime cada linha do csv dicionarizado
	for eduardo in planilha:
		if eduardo != elementoRemovido:
			print(f"Aventura: {eduardo['Aventura']}")

// Função que solicita ao usuário digitar 'continue' para avançar, caso não digite corretamente, o usuário não avançará
def funcaoContinue():
	escolha = input("Digite 'continue' para avançar: ")
	// Se o usuário não digitar certo, aparecerá uma mensagem negativa
	while escolha != "continue":
    		escolha = input("Não foi possível avançar. Digite 'continue': ")
	// Se o usuário digitar corretamente, aparecerá uma mensagem positiva
	if escolha == "continue":
    		print("Pode avançar, boa sorte!")
	// Retorna todas as modificações para a variável 'escolha'
	return escolha

// Função que abre e lê o arquivo csv
with open("rpg.csv", "r") as minhaPlanilha:
	novaVariavel = csv.DictReader(minhaPlanilha)
	// Coloca cada linha do csv em um elemento do vetor
	for n in novaVariavel:
		planilha.append(n)

// Imprime a planilha dicionarizada em formato de um vetor de objetos
print(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

// Função 1 declarada
imprimirAventuras(planilha)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

// Índice do vetor específico declarado
elementoEspecifico = planilha[9]
// Função 2 declarada
aventuraEspecifica(planilha, elementoEspecifico)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

// Índice do vetor específico declarado
elementoRemovido = planilha[19]
// Função 3 declarada
removerAventura(planilha, elementoRemovido)

print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

// Função 4 declarada
funcaoContinue()