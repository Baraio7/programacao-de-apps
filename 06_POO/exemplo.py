# Classe: o modelo (planta)
class Celular:
    def __init__(self, marca, modelo, cor, saudebateria, ligado=False):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.saudebateria = saudebateria
        # O estado inicial pode ser definido diretamente aqui ou pelo parâmetro
        self.ligado = ligado

    # Métodos: os comportamentos do objeto (DEVEM ficar indentados dentro da classe!)
    def ligar(self):
        # Corrigido: transformamos a saúde da bateria em número para poder testar
        # Se a saúde for 0 (ou string "0"), avisa que está sem bateria
        if str(self.saudebateria) == "0" or str(self.saudebateria) == "0%":
            print(f"O {self.modelo} está sem bateria! Coloque para carregar.")
        else:
            self.ligado = True
            print(f"O {self.modelo} foi ligado com sucesso! Status: Carregado.")

    def desligar(self):
        self.ligado = False
        print ("Desligado")


# Objetos: Criados a partir da classe (as casas)
# Dica: Boas práticas em Python pedem nomes de variáveis em minúsculo (celular1)
# Passamos os booleanos True/False sem aspas para o Python entender como comando, não texto
celular1 = Celular("Motorola", "Edge 60 Pro", "Cinza", "100%", True)
celular2 = Celular("Apple", "Iphone XS", "Vermelho", "74%", False)

# Acessando e alterando atributos
print("--- Ficha do celular 1 ---")
print(f"Marca: {celular1.marca}")
print(f"Modelo: {celular1.modelo}")
print(f"Cor: {celular1.cor}")
print(f"Saúde da Bateria: {celular1.saudebateria}")
print(f"Está ligado? {celular1.ligado}")

print("\n--- Ficha do celular 2 ---")
print(f"Marca: {celular2.marca}")
print(f"Modelo: {celular2.modelo}")
print(f"Cor: {celular2.cor}")
print(f"Saúde da Bateria: {celular2.saudebateria}")
print(f"Está ligado? {celular2.ligado}")

# Chamando métodos
print("\n--- Testando os Métodos ---")
celular1.ligar()
celular2.ligar()