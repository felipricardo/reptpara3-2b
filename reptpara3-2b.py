"""
Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
em relação ao filme: ótimo – 3, bom – 2, regular – 1. Faça um programa que receba a idade e a opinião de
15 espectadores e que calcule e mostre:
- a média das idades das pessoas que responderam ótimo
- a quantidade de pessoas que respondeu regular
- a percentagem de pessoas que respondeu bom entre todos os espectadores analisados
"""
# inicializa as variáveis
idade_otimo = 0
qtd_otimo = 0
qtd_regular = 0
qtd_bom = 0
opiniao = 0

# pede a opinião e idade dos 15 espectadores
quant_espec = int(input("Digite a quantidade de espectadores: "))
for i in range(quant_espec):
    while opiniao != 1 or 2 or 3:
        idade = int(input("Digite a idade do espectador: "))
        opiniao = int(input("Digite a opinião do espectador (ótimo=3, bom=2, regular=1): "))

        # verifica a opinião do espectador e atualiza as variáveis correspondentes
        if opiniao == 3:
            idade_otimo += idade
            qtd_otimo += 1
            break
        if opiniao == 2:
            qtd_bom += 1
            break
        if opiniao == 1:
            qtd_regular += 1
            break

# calcula a média das idades dos espectadores que responderam ótimo
if qtd_otimo > 0:
    media_idade_otimo = idade_otimo / qtd_otimo
    print("A média das idades das pessoas que responderam ótimo é:", media_idade_otimo)
else:
    print("Nenhum espectador respondeu ótimo.")

# mostra a quantidade de pessoas que responderam regular
print("A quantidade de pessoas que responderam regular é:", qtd_regular)

# calcula a porcentagem de pessoas que responderam bom
porcentagem_bom = (qtd_bom / quant_espec) * 100
print("A porcentagem de pessoas que responderam bom é:", porcentagem_bom, "%")