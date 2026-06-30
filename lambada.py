idade_ana = 20

calcular_idade_avo = lambda idade: idade * 3

idade_avo = calcular_idade_avo(idade_ana)

print(f"Se Ana tem {idade_ana} anos, seu avô tem {idade_avo} anos.") 

numeros = [1, 5, 8, 12, 15, 20, 27, 30]

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares) 

palavras = ["abacaxi", "banana", "Amora", "melancia", "azeite", "laranja"]

comecam_com_a = list(filter(lambda p: p.lower().startswith('a'), palavras))

print(comecam_com_a) 

