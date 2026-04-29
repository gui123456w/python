import random
class Pokemon:
    def __init__(self, nome, tipo, vida, ataque):
        self.nome = nome
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.nivel = 1

    def atacar(self, inimigo):
        dano = random.randint(self.ataque - 5, self.ataque + 5)
        inimigo.vida -= dano
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")

    def evoluir(self):
        self.nivel += 1
        aumento = 10
        self.ataque += aumento
        print(
            f" {self.nome} evoluiu para o nível {self.nivel}! Ataque aumentou em {aumento} (novo ataque: {self.ataque})")

    def status(self):
        print(f"{self.nome} | Tipo: {self.tipo} | Vida: {self.vida}")

    def curar(self):
        self.curar += 20
        aumento = 20
        self.vida += aumento
        print(f"{self.curar} Vida aumento {self.vida} aumento {aumento} ")


pikachu = Pokemon("Pikachu", "elétrico", 139, 7)
rayquaza = Pokemon("Rayquaza", "dragão e voador", 27, 4)
kyogre = Pokemon("Kyogre", "água", 32, 2)
solgaleo = Pokemon("Solgaleo", "psíquico e aço", 12, 9)
jupiter = Pokemon("Jupis", "Ferro", 50, 7)

lista_pokis = [pikachu, rayquaza, kyogre, solgaleo, jupiter]

print("Escolha de Jogadores para Pokebolinha:")
for i, p in enumerate(lista_pokis):
    print(f"{i + 1} - {p.nome}")

escolha = int(input("Digite um número: ")) - 1
jogador = lista_pokis[escolha]

inimigo = random.choice(lista_pokis)
while inimigo == jogador:
    inimigo = random.choice(lista_pokis)

print(f"\nVocê escolheu {jogador.nome}")
print(f"Inimigo escolheu {inimigo.nome}\n")

while jogador.vida > 0 and inimigo.vida > 0:
    print("\n1 - Atacar\n2- Ver status\n3- Fugir \n4- Carinho e cura \n5- Evoluir")

    opcao = input("Escolha: ")

    if opcao == "1":
        jogador.atacar(inimigo)

        if inimigo.vida > 0:
            inimigo.atacar(jogador)

    elif opcao == "2":
        jogador.status()
        inimigo.status()

    elif opcao == "3":
        print("Você fugiu!")
        break
    elif opcao == "4":
        cura = random.randint(5, 15)
        jogador.vida += cura
        print(f" Você fez um carinho em {jogador.nome} e ele recuperou {cura} de vida!")

    elif opcao == "5":
        jogador.evoluir()


    else:
        print("Opção inválida!")

if jogador.vida <= 0:
    print("Você perdeu a batalha...")
elif inimigo.vida <= 0:
    print("Você venceu a batalha!")