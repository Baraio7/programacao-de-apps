# ==============================================================================
# GUIA DEFINITIVO: LISTAS E TUPLAS EM PYTHON
# Arquivo preparado para estudo e execução no PyCharm
# ==============================================================================

"""
RESUMO EXPRESSO:
- LISTA [ ]: Mutável (pode alterar, adicionar, remover e reordenar itens).
- TUPLA ( ): Imutável (dados fixos, mais rápida, segura contra alterações).
"""

# ==============================================================================
# 1. LISTAS (Mutáveis: altere, adicione, remova e reordene elementos)
# ==============================================================================

# --- A. Criação, Acesso e Fatiamento (Slicing) ---
frutas = ["maçã", "banana", "laranja", "abacaxi", "kiwi"]

print("--- 1. LISTAS: Acesso e Fatiamento ---")
print("Primeiro item [0]:", frutas[0])     # "maçã"
print("Último item [-1]:", frutas[-1])      # "kiwi"
print("Fatia [1:4]:", frutas[1:4])          # Do índice 1 ao 3: ['banana', 'laranja', 'abacaxi']
print("Lista invertida [::-1]:", frutas[::-1])


# --- B. Modificação e Adição de Elementos ---
print("\n--- 1. LISTAS: Modificação e Adição ---")

# Alterando um item existente por índice
frutas[0] = "morango"

# Formas de adicionar elementos:
frutas.append("uva")                # Adiciona "uva" ao final
frutas.insert(1, "manga")           # Insere "manga" na posição 1 (desloca o restante)
frutas.extend(["pêssego", "amora"]) # Adiciona múltiplos itens ao final da lista

print("Lista após adições:", frutas)


# --- C. Remoção de Elementos ---
print("\n--- 1. LISTAS: Remoção ---")

frutas.remove("laranja") # Remove a 1ª ocorrência do valor "laranja"
removido = frutas.pop(2) # Remove e RETORNA o item do índice 2 (se omitido o índice, remove o último)
del frutas[0]            # Apaga o elemento no índice 0 (ou fatias inteiras)

print(f"Item removido com pop(2): {removido}")
print("Lista após remoções:", frutas)


# --- D. Ordenação e Busca ---
print("\n--- 1. LISTAS: Ordenação e Busca ---")
numeros = [42, 10, 5, 23, 10, 88]

print("Contagem do número 10:", numeros.count(10)) # Quantas vezes aparece
print("Índice do número 23:", numeros.index(23))    # Posição do item

numeros.sort()                  # Ordena a lista original (crescente)
print("Lista em ordem crescente:", numeros)

numeros.sort(reverse=True)      # Ordena a lista original (decrescente)
print("Lista em ordem decrescente:", numeros)


# --- E. List Comprehension (Criação Rápida e Elegante) ---
print("\n--- 1. LISTAS: Compreensão de Listas ---")
quadrados = [x**2 for x in range(1, 6)]         # [1, 4, 9, 16, 25]
pares = [x for x in range(10) if x % 2 == 0]    # [0, 2, 4, 6, 8]

print("Quadrados de 1 a 5:", quadrados)
print("Números pares de 0 a 8:", pares)


# ==============================================================================
# 2. TUPLAS (Imutáveis: estrutura fixa, mais rápida e segura)
# ==============================================================================

print("\n" + "="*50)
# --- A. Criação e Peculiaridades ---
coordenadas = (-23.5505, -46.6333)
servidor = ("localhost", 8080, "HTTP", "v1.0")

# ATENÇÃO: Tupla de apenas UM elemento EXIGE uma vírgula no final!
tupla_unica = ("Python",)
nao_eh_tupla = ("Python") # Python interpreta apenas como uma string entre parênteses

print("--- 2. TUPLAS: Tipos e Criação ---")
print("Tipo de tupla_unica:", type(tupla_unica))    # <class 'tuple'>
print("Tipo de nao_eh_tupla:", type(nao_eh_tupla))  # <class 'str'>

# Tentativa de alteração gera erro TypeError:
# coordenadas[0] = 0.0  # -> Se desconmentar esta linha, o PyCharm apontará erro!


# --- B. Desempacotamento de Tuplas (Unpacking) ---
print("\n--- 2. TUPLAS: Desempacotamento ---")
latitude, longitude = coordenadas
print(f"Latitude extraída: {latitude} | Longitude extraída: {longitude}")

# Desempacotamento avançado usando o operador * (pega o 'resto' dos valores)
host, porta, *protocolos = servidor
print(f"Host: {host} | Porta: {porta} | Detalhes adicionais: {protocolos}")


# --- C. Métodos Disponíveis em Tuplas ---
# Por serem imutáveis, possuem apenas métodos de consulta/leitura
letras = ('a', 'b', 'c', 'a', 'a', 'd')

print("\n--- 2. TUPLAS: Métodos de Consulta ---")
print("Ocorrências da letra 'a':", letras.count('a'))
print("Primeiro índice da letra 'c':", letras.index('c'))


# --- D. Aplicações Práticas do Dia a Dia ---
print("\n--- 2. TUPLAS: Casos Práticos ---")

# 1. Retorno múltiplo de funções (retorna uma tupla implicitamente)
def calcular_estatisticas(valores):
    total = sum(valores)
    media = total / len(valores)
    return total, media  # Retorna (total, media)

soma_total, media_calculada = calcular_estatisticas([10, 20, 30])
print(f"Retorno de Função -> Soma: {soma_total}, Média: {media_calculada}")

# 2. Troca elegante de variáveis sem criar variável temporária
a, b = 5, 10
a, b = b, a  # Inverte os valores
print(f"Valores trocados -> a: {a}, b: {b}")


# ==============================================================================
# 3. QUANDO USAR CADA UMA? (GUIA RÁPIDO DE DECISÃO)
# ==============================================================================
"""
USE LISTA QUANDO:
 - Os dados forem do mesmo tipo e precisarem mudar com frequência.
 - Você precisar adicionar, remover ou reordenar itens constantemente.
   Exemplo: Carrinho de compras, lista de usuários ativos, histórico de tarefas.

USE TUPLA QUANDO:
 - Os dados representarem uma entidade fixa e imutável (registros).
 - O valor dos dados não dever sofrer alterações acidentais.
 - Precisar de leve ganho de desempenho e menor uso de memória RAM.
   Exemplo: Coordenadas GPS (lat, long), configurações do sistema, RGB (255, 255, 255).
"""