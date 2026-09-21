# ===================================================
# ENTRADA/SAÍDA DE DADOS E OPERADORES EM PYTHON
# ===================================================

# ---------------------------------------------------
# 1. ENTRADA E SAÍDA DE DADOS
# input(): lê dados inseridos pelo usuário (sempre retorna uma string/texto)
# print(): exibe informações no console/tela
# ---------------------------------------------------

# Entrada de dados (solicitando informações ao usuário)
nome = input("Digite o seu nome: ")

# Convertendo a entrada (input) para número inteiro (int) ou decimal (float)
idade = int(input("Digite a sua idade: "))
altura = float(input("Digite a sua altura em metros (ex: 1.75): "))

# Saída de dados formatada com f-string (f"...")
print(f"\nOlá, {nome}! Você tem {idade} anos e mede {altura}m de altura.")


# ---------------------------------------------------
# 2. OPERADORES ARITMÉTICOS
# Realizam cálculos matemáticos básicos e avançados
# ---------------------------------------------------

a = 10
b = 3

soma = a + b           # Adição: 13
subtracao = a - b      # Subtração: 7
multiplicacao = a * b  # Multiplicação: 30
divisao = a / b        # Divisão (resultado decimal): 3.3333...
divisao_inteira = a // b # Divisão inteira (despreza as casas decimais): 3
resto = a % b          # Módulo (resto da divisão de 10 por 3): 1
potencia = a ** b      # Exponenciação (10 elevado a 3): 1000

print(f"\nOperações entre {a} e {b}:")
print(f"Soma: {soma} | Divisão Inteira: {divisao_inteira} | Resto: {resto} | Potência: {potencia}")


# ---------------------------------------------------
# 3. OPERADORES DE COMPARAÇÃO (RELACIONAIS)
# Comparam dois valores e retornam True (Verdadeiro) ou False (Falso)
# ---------------------------------------------------

igual = (a == b)       # Igual a: False
diferente = (a != b)   # Diferente de: True
maior = (a > b)        # Maior que: True
menor_igual = (a <= b) # Menor ou igual a: False

print(f"\nComparações: {a} é maior que {b}? {maior} | {a} é igual a {b}? {igual}")


# ---------------------------------------------------
# 4. OPERADORES LÓGICOS
# Combinam condições booleanas (and, or, not)
# ---------------------------------------------------

tem_carteira = True
tem_carro = False

# and: Retorna True se AMBAS as condições forem verdadeiras
pode_dirigir = (idade >= 18) and tem_carteira

# or: Retorna True se PELO MENOS UMA condição for verdadeira
vai_de_transporte = tem_carro or True

# not: Inverte o valor booleano (True vira False, False vira True)
bloqueado = not pode_dirigir

print(f"\nPode dirigir? {pode_dirigir}")
print(f"Acesso bloqueado? {bloqueado}")


# ---------------------------------------------------
# 5. OPERADORES DE ATRIBUIÇÃO
# Utilizados para definir ou atualizar o valor de uma variável
# ---------------------------------------------------

pontos = 100
pontos += 10   # Equivalente a: pontos = pontos + 10 (Resultado: 110)
pontos -= 25   # Equivalente a: pontos = pontos - 25 (Resultado: 85)
pontos *= 2    # Equivalente a: pontos = pontos * 2  (Resultado: 170)

print(f"\nPontuação final após atribuições: {pontos}")