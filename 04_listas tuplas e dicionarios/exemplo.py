# ==========================================
# EXEMPLO DE LISTAS E TUPLAS EM PYTHON
# ==========================================

# 1. LISTAS (Mutáveis: você pode alterar, adicionar e remover elementos)
# Criadas utilizando colchetes []
frutas = ["maçã", "banana", "laranja"]

# Modificando um item da lista existente
frutas[0] = "morango"  # Altera "maçã" para "morango"

# Adicionando um novo elemento ao final da lista
frutas.append("uva")

# Exibindo a lista modificada no console
print("Lista de frutas:", frutas)
# Saída esperada: ['morango', 'banana', 'laranja', 'uva']


# 2. TUPLAS (Imutáveis: os elementos NÃO podem ser alterados após a criação)
# Criadas utilizando parênteses ()
coordenadas = (23.5505, 46.6333)

# Acessando elementos individuais da tupla por índice
latitude = coordenadas[0]
longitude = coordenadas[1]

# Tentativa de alteração (isso causaria um ERRO do tipo TypeError):
# coordenadas[0] = 10.0000

# Exibindo os dados da tupla no console
print(f"Latitude: {latitude}, Longitude: {longitude}")
# Saída esperada: Latitude: 23.5505, Longitude: 46.6333