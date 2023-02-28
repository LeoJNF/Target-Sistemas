import json

with open("dados.json") as dados:
    info = json.load(dados)


menor = maior = x = 0
cont = cont2 = 0 #contadores

for z in info:
    cont += 1
    if z['valor'] > 0: #caso for final de semana ou feriado não entra na conta
        cont2 += 1
        x += z['valor'] #Somando o valor total de faturamento
        if cont == 1:
            maior = menor = z['valor'] # O primeiro valor que entra é o maior e o menor
        else:
            if menor > z['valor']: #se a variavel 'menor' for maior que o valor lido, este valor lido se torna o menor
                menor = z['valor']
            if maior < z['valor']: #se a variavel 'maior' for menor que o valor lido, este valor lido se torna o maior
                maior = z['valor']

print(f"Maior Faturamento = {maior:.2f} \nMenor Faturamento = {menor:.2f}") #Imprimindo Maior e menor valor

media = x / cont2 #Calculo da media

print(f'\nMédia mensal = {media:.2f}') #Imprimindo a media

print('\nDias do mês superior a média mensal')
print('-----------------------------------')
for z in info: #Imprimindo os dias que foi superior a média mensal
    if z['valor'] > media:
        print(f'Dia: {z["dia"]}         Valor: {z["valor"]:.2f}')
