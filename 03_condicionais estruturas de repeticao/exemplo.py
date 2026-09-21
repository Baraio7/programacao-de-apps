# ===================================================
# CONDICIONAIS E ESTRUTURAS DE REPETIÇÃO EM PYTHON
# ===================================================

# ---------------------------------------------------
# 1. CONDICIONAIS (if, elif, else)
# Usadas para tomar decisões com base em condições booleanas (True/False)
# ---------------------------------------------------

idade = 18

if idade < 12:
    # Executado se a condição 'idade < 12' for verdadeira
    status = "Criança"
elif idade < 18:
    # Executado se a condição anterior for falsa e 'idade < 18' for verdadeira
    status = "Adolescente"
else:
    # Executado se nenhuma das condições anteriores for verdadeira
    status = "Adulto"

print(f"Com {idade} anos, a pessoa é: {status}")


# ---------------------------------------------------
# 2. ESTRUTURA DE REPETIÇÃO: FOR
# Utilizada quando sabemos quantas vezes repetir ou quando percorremos uma sequência
# ---------------------------------------------------

# Exemplo A: Percorrendo um intervalo de números com range(início, fim_não_incluso)
print("\n--- Repetição com range() ---")
for i in range(1, 4):
    print(f"Contagem: {i}")

# Exemplo B: Iterando sobre uma lista
print("\n--- Percorrendo uma lista ---")
linguagens = ["Python", "JavaScript", "C++"]
for ling in linguagens:
    print(f"Linguagem: {ling}")


# ---------------------------------------------------
# 3. ESTRUTURA DE REPETIÇÃO: WHILE
# Executa um bloco de código enquanto uma condição permanecer verdadeira
# ---------------------------------------------------

print("\n--- Repetição com while ---")
contador = 3

while contador > 0:
    print(f"Contagem regressiva: {contador}")
    # Atualiza a variável para evitar um loop infinito
    contador -= 1

print("Fim da contagem!")