alunos = []

while True:
    print("\n===== Sistema Escolar do Ivone de Palma =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Excluir aluno")
    print("4 - Procurar aluno")
    print("5 - Alterar aluno")
    print("6 - Sair")

    opcao = int(input("Digite algum numero para prosseguir: "))

    if opcao == 1:
        nome = input("Cadastre o nome do aluno: ")
        idade = int(input("Fale a idade do aluno: "))
        if 13 <= idade <= 35:
            aluno = {
                "nome": nome,
                "idade": idade
            }

            alunos.append(aluno)
            print("Aluno cadastrado com sucesso!")
        else:
            print("Idade inválida! Só é permitido cadastrar alunos entre 13 e 35 anos.")
    elif opcao == 2:
        if len(alunos) == 0:
            print("Nenhum aluno cadastrado.")
        else:
            print("\n--- Lista de Alunos ---")
            for i, aluno in enumerate(alunos):
                print(f"{i} - Nome: {aluno['nome']} | Idade: {aluno['idade']}")

    elif opcao == 3:
        if len(alunos) == 0:
            print("Não há alunos para excluir.")
        else:
            for i, aluno in enumerate(alunos):
                print(f"{i} - {aluno['nome']}")

            indice = int(input("Digite cadastrado para excluir o nome da lista: "))
            if 0 <= indice < len(alunos):
                removido = alunos.pop(indice)
                print(f"Aluno {removido['nome']} removido com sucesso!")
            else:
                print("Índice inválido.")

    elif opcao == 4:
        busca = input("Digite o nome cadastrado para encontrar o Aluno: ").lower()
        encontrados = []

        for aluno in alunos:
            if busca in aluno["nome"].lower():
                encontrados.append(aluno)

        if len(encontrados) == 0:
            print("Nenhum aluno encontrado.")
        else:
            print("\n--- Alunos encontrados ---")
            for aluno in encontrados:
                print(f"Nome: {aluno['nome']} | Idade: {aluno['idade']}")

    elif opcao == 5:
        if len(alunos) == 0:
            print("Não há alunos para alterar.")
        else:
            print("\n--- Altere o nome cadastrado ---")
            for i, aluno in enumerate(alunos):
                print(f"{i} - Nome: {aluno['nome']} | Idade: {aluno['idade']}")

            indice = int(input("Digite o número do aluno: "))

            if 0 <= indice < len(alunos):
                novo_nome = input("Digite o novo nome: ")
                nova_idade = input("Digite a nova idade: ")

                alunos[indice]["nome"] = novo_nome
                alunos[indice]["idade"] = nova_idade

                print("Aluno atualizado com sucesso!")
            else:
                print("Índice inválido.")

    elif opcao == 6:
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!")
print("Obrigado por utilizar nosso sistema! ")


def evoluir(self):
    self.nivel += 1
    aumento = 10
    self.ataque += aumento
    print(f"🌟 {self.nome} evoluiu para o nível {self.nivel}! Ataque aumentou em {aumento} (novo ataque: {self.ataque})")