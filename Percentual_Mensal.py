
mensal = {'SP': 67836.46, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'outros': 19849.53}

tmensal = sum(mensal.values())#Soma total dos estados

for x, y in mensal.items():
    por = y * 100 / tmensal#Calculando a porcentagem de cada estado
    print(f'{x} teve o percentual = {por:.2f}%')#imprimindo o valor formatado
