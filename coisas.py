1) Programa que recebe um número positivo e maior que zero, e calcula várias operações:

python

import math

# Recebe o número positivo
numero = float(input("Digite um número positivo: "))

# Verifica se o número é maior que zero
if numero > 0:
    print(f"A) O número digitado ao quadrado é: {numero ** 2}")
    print(f"B) O número digitado ao cubo é: {numero ** 3}")
    print(f"C) A raiz quadrada do número digitado é: {math.sqrt(numero)}")
    print(f"D) A raiz cúbica do número digitado é: {numero ** (1/3)}")
else:
    print("Por favor, digite um número maior que zero.")

2) Programa que recebe dois números maiores que zero e calcula um elevado ao outro:

python

# Recebe dois números positivos
base = float(input("Digite a base (número positivo): "))
expoente = float(input("Digite o expoente (número positivo): "))

# Verifica se ambos são positivos
if base > 0 and expoente > 0:
    resultado = base ** expoente
    print(f"O resultado de {base} elevado a {expoente} é: {resultado}")
else:
    print("Ambos os números devem ser positivos.")

3) Programa que recebe a medida em pés e faz as conversões:

python

# Recebe a medida em pés
pes = float(input("Digite a medida em pés: "))

# Faz as conversões
polegadas = pes * 12
jardas = pes / 3
milhas = jardas / 1760

# Exibe os resultados
print(f"A medida em polegadas é: {polegadas}")
print(f"A medida em jardas é: {jardas}")
print(f"A medida em milhas é: {milhas}")

4) Programa que calcula a idade de uma pessoa:

python

# Recebe o ano de nascimento e o ano atual
ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

# Calcula a idade
idade = ano_atual - ano_nasc

# Calcula a idade em 2050
idade_em_2050 = 2050 - ano_nasc

# Exibe os resultados
print(f"A) A idade dessa pessoa é: {idade}")
print(f"B) A idade dessa pessoa em 2050 será: {idade_em_2050}")

5) Programa que calcula o preço final de um carro:

python

# Recebe o preço de fábrica, percentual de lucro e percentual de impostos
preco_fabrica = float(input("Digite o preço de fábrica do veículo: "))
percentual_lucro = float(input("Digite o percentual de lucro do distribuidor: "))
percentual_impostos = float(input("Digite o percentual de impostos: "))

# Calcula os valores
lucro = preco_fabrica * (percentual_lucro / 100)
impostos = preco_fabrica * (percentual_impostos / 100)
preco_final = preco_fabrica + lucro + impostos

# Exibe os resultados
print(f"A) O valor correspondente ao lucro do distribuidor é: R${lucro:.2f}")
print(f"B) O valor correspondente aos impostos é: R${impostos:.2f}")
print(f"C) O preço final do veículo é: R${preco_final:.2f}")

6) Programa que calcula o salário a receber com base no salário mínimo:

python

# Recebe o número de horas trabalhadas e o valor do salário mínimo
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))

# Calcula a hora trabalhada e o salário bruto
valor_hora = salario_minimo / 2
salario_bruto = horas_trabalhadas * valor_hora

# Calcula o imposto
imposto = salario_bruto * 0.03

# Calcula o salário a receber
salario_a_receber = salario_bruto - imposto

# Exibe os resultados
print(f"A) O valor da hora trabalhada é: R${valor_hora:.2f}")
print(f"B) O salário bruto é: R${salario_bruto:.2f}")
print(f"C) O imposto é: R${imposto:.2f}")
print(f"D) O salário a receber é: R${salario_a_receber:.2f}")

7) Programa que calcula o saldo bancário após retiradas com CPMF:

python

# Inicializa o saldo bancário
saldo = float(input("Digite o salário inicial do trabalhador (valor do depósito inicial): "))
cheque1 = float(input("Digite o valor do primeiro cheque: "))
cheque2 = float(input("Digite o valor do segundo cheque: "))

# Calcula o saldo após as retiradas
cpmf = 0.0038  # 0,38% de CPMF
total_retiradas = cheque1 + cheque2
cpmf_total = total_retiradas * cpmf

# Atualiza o saldo com as retiradas e CPMF
saldo_final = saldo - total_retiradas - cpmf_total

# Exibe o saldo final
print(f"O saldo final após as retiradas e CPMF é: R${saldo_final:.2f}")

8) Programa que calcula o salário a receber com gratificação e imposto:

python

# Recebe o salário base
salario_base = float(input("Digite o salário base do funcionário: "))

# Calcula o salário a receber
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_a_receber = salario_base + gratificacao - imposto

# Exibe os resultados
print(f"O salário a receber é: R${salario_a_receber:.2f}")

9) Programa que calcula o salário a receber com gratificação fixa e imposto:

python

# Recebe o salário base
salario_base = float(input("Digite o salário base do funcionário: "))

# Calcula o salário a receber com gratificação fixa
gratificacao = 50.00
imposto = salario_base * 0.10
salario_a_receber = salario_base + gratificacao - imposto

# Exibe os resultados
print(f"O salário a receber é: R${salario_a_receber:.2f}")

10) Programa que calcula o valor do rendimento e o valor total após o depósito:

python

# Recebe o valor do depósito e a taxa de juros
deposito = float(input("Digite o valor do depósito: "))
taxa_juros = float(input("Digite a taxa de juros (%): "))

# Calcula o rendimento
rendimento = deposito * (taxa_juros / 100)

# Calcula o valor total após o rendimento
total_com_rendimento = deposito + rendimento

# Exibe os resultados
print(f"O valor do rendimento é: R${rendimento:.2f}")
print(f"O valor total após o rendimento é: R${total_com_rendimento:.2f}")