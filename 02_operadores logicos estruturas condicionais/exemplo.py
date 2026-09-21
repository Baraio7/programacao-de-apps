# 1. Estrutura Condicionais

nota =
6

if nota >= 7:
    print("Aprovado")
else if nota >= 5:
    print("Recuperação")
    else:
    print("Reprovado")

# 2. Condicionais e Operadores Lógicos
# and -> Todas as condições devem ser verdadeiras
# or -> Pelo menos uma condição deve ser verdadeira
# not -> inverte o resultado

idade = 20
ingresso = True

if idade >= 18 and ingresso:
    print("Entrada Permitida")
else:
    print("Entrada não permitida")

# 3. Estrutura de Repetição while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# 4. Estrutura de repetição for
for numero in range(1, 6):
    print(numero)

# 5. percorrendo uma lista
nomes = ["ana", "Carlos", "joão", "maria"]
for nome in nomes:
    print(nome)

    # 6. Break, continue, pass
    for numero in range(1, 11):
        
print(numero)
# break
# continue
# pass
print(numero)