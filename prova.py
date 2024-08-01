soma = 0
inicio = int(input("Digite o Inicio do intervalo "))
fim = int(input("Digite o final do intervalo "))

for numero in range(inicio, fim + 1):
    if numero % 2 == 0:
            soma += numero
    else:
      continue

      print(f"A soma dos números pares no intervalo de {inicio} até {fim} é de {soma} ")