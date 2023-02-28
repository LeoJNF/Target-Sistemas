#SEQUÊNCIA DE FIBONACCI


s1 = s3 = 0 # Declarando as primeiras sequencias do Fibonacci
s2 = 1

num = int(input("Informe seu numero: "))#Entrada do numero escolhido pelo usuário
print(f"{s1} - {s2} - ", end='') # Imprimido as primeiras sequencias do Fibonacci
while True:
    s3 = s1 + s2 #Calculando sempre o proximo numero, somando o numero atual com o anterior
    print(f'{s3} - ', end='')
    s1 = s2 # Redefininfo o numero anterior
    s2 = s3 # Redefinindo o numero atual
    if s2 >= num: #se o numero atual for maior ou igual o valor definido pelo usuario o laço para
        break

print("pertence") if s3 == num else print("Nao Pertence") #Verificando se faz parte da sequencia de Fibonacci

