# """
# Faça um programa de terminal que exibe ao usuário uma listas dos quartos
# disponiveis para alugar e o preço de cada quarto, esta informação está
# disponível em um arquivo de texto separado por virgulas.

# `quartos.txt`
# # codigo, nome, preço
# 1,Suite Master,500
# 2,Quarto Familia,200
# 3,Quarto Single,100
# 4,Quarto Simples,50

# O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado
# e a quantidade de dias e no final exibe o valor estimado a ser pago.

# O programa deve salvar esta escolha em outro arquivo contendo as reservas

# `reservas.txt`
# # cliente, quarto, dias
# Denise,3,12

# Se outro usuário tentar reservar o mesmo quarto o programa deve exibir uma
# mensagem informando que já está reservado.
# """

# import os  # ferramentas

# # importação e leitura dos quartos
# def carregar_quartos(caminho="quartos.txt"): #criar funçoes
#     """Lê os quartos disponíveis e retorna um dicionário {codigo: (nome, preco)}."""
#     quartos = {} # chave e valor
#     with open(caminho, "r", encoding="utf-8") as arquivo: # abrir o arquivo/(r)leitura
#         for linha in arquivo: # ler arquivo linha por linha
#             linha = linha.strip() # Limpar texto
#             if not linha or linha.startswith("#"): # condição
#                 continue  # Ignora linhas vazias e comentários
#             codigo, nome, preco = linha.split(",") # separar em tres variaveis
#             quartos[codigo.strip()] = (nome.strip(), float(preco.strip())) # salvar e converter
#     return quartos #devolver resultados

# # leituras das Reservas Existentes
# def carregar_reservas(caminho="reservas.txt"):
#     """Retorna um conjunto (set) com os códigos dos quartos já reservados."""
#     reservados = set() # criar conhunto vazio
#     if not os.path.exists(caminho): # verificar existencia
#         return reservados  # Se o arquivo não existe, nenhum quarto está reservado

#     with open(caminho, "r", encoding="utf-8") as arquivo:
#         for linha in arquivo:
#             linha = linha.strip()
#             if not linha or linha.startswith("#"):
#                 continue
#             _, quarto, _ = linha.split(",") # pegar só o num do quarto
#             reservados.add(quarto.strip()) # quarto ocupado
#     return reservados # devolver o conjunto vazio

# # salvando nova Reserva
# def salvar_reserva(cliente, quarto, dias, caminho="reservas.txt"): # receber dados do cliente
#     """Adiciona a nova reserva ao final do arquivo reservas.txt."""
#     arquivo_novo = not os.path.exists(caminho) # checar
#     with open(caminho, "a", encoding="utf-8") as arquivo:# abrir arquivo
#         if arquivo_novo:# condição
#             arquivo.write("# cliente, quarto, dias\n")# escrever cabeçalho
#         arquivo.write(f"{cliente},{quarto},{dias}\n") # escrever dados

# # Programa interação com o usuário
# def main(): # onde o programa acontece
#     quartos = carregar_quartos() # buscar quartos disponiveis
#     reservados = carregar_reservas() # buscar quartos ocupados

#     print("=== QUARTOS DISPONÍVEIS ===") # exibir titulo na tela
#     for codigo, (nome, preco) in quartos.items(): # percorrer dicionario
#         status = " [RESERVADO]" if codigo in reservados else "" # condiçao. marcar aviso se estiver ocupado
#         print(f"{codigo} - {nome}: R$ {preco:.2f}/dia{status}") # preço em 2 casas decimais
#     print("-" * 27)

#     cliente = input("Digite seu nome: ").strip() # perguntar o usuário
#     codigo_escolhido = input("Digite o número do quarto: ").strip() # perguntar quarto

#     # Validação de existência e disponibilidade
#     if codigo_escolhido not in quartos:
#         print("Erro: Quarto inválido.")
#         return

#     if codigo_escolhido in reservados:
#         print("Aviso: Este quarto já está reservado!")
#         return

#     dias = int(input("Quantidade de dias: "))
#     nome_quarto, preco_diaria = quartos[codigo_escolhido]
#     valor_total = preco_diaria * dias

#     salvar_reserva(cliente, codigo_escolhido, dias)

#     print(f"\nReserva confirmada para {cliente} ({nome_quarto})!")
#     print(f"Valor estimado a ser pago: R$ {valor_total:.2f}")


# if __name__ == "__main__": #  Garantir que o código só rode se este arquivo for executado diretamente.
#     main()

import os  # Ferramentas do sistema


# 1. Leitura dos quartos
def carregar_quartos(caminho="quartos.txt"):
    quartos = {}  # Dicionário vazio: {codigo: (nome, preco)}
    with open(caminho, "r", encoding="utf-8") as arquivo:  # Abrir para leitura ("r")
        for linha in arquivo:  # Ler linha por linha
            linha = linha.strip()  # Limpar espaços e quebras de linha
            if not linha or linha.startswith("#"):  # Pular vazia ou comentário
                continue
            codigo, nome, preco = linha.split(",")  # Separar na vírgula
            quartos[codigo.strip()] = (nome.strip(), float(preco.strip()))  # Salvar e converter preço
    return quartos  # Devolver dicionário preenchido


# 2. Leitura das reservas existentes
def carregar_reservas(caminho="reservas.txt"):
    reservados = set()  # Conjunto vazio (sem itens repetidos)
    if not os.path.exists(caminho):  # Se arquivo ainda não existe
        return reservados  # Devolver conjunto vazio

    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha or linha.startswith("#"):
                continue
            _, quarto, _ = linha.split(",")  # Pegar apenas o código do quarto
            reservados.add(quarto.strip())  # Adicionar quarto ocupado
    return reservados


# 3. Gravar nova reserva no arquivo
def salvar_reserva(cliente, quarto, dias, caminho="reservas.txt"):
    arquivo_novo = not os.path.exists(caminho)  # Checar se arquivo é inédito
    with open(caminho, "a", encoding="utf-8") as arquivo:  # Modo adicionar ao final ("a")
        if arquivo_novo:
            arquivo.write("# cliente, quarto, dias\n")  # Escrever cabeçalho
        arquivo.write(f"{cliente},{quarto},{dias}\n")  # Escrever dados


# 4. [NOVO] Apagar reserva do arquivo para liberar quarto
def cancelar_reserva(quarto_cancelar, caminho="reservas.txt"):
    if not os.path.exists(caminho):  # Se não há arquivo, não faz nada
        return

    linhas_mantidas = []  # Lista para guardar reservas que vão continuar
    with open(caminho, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            limpa = linha.strip()
            if not limpa or limpa.startswith("#"):  # Manter comentários e linhas vazias
                linhas_mantidas.append(linha)
                continue
            _, quarto, _ = limpa.split(",")  # Pegar número do quarto da linha
            if quarto.strip() != quarto_cancelar:  # Se for DIFERENTE (!=) do cancelado
                linhas_mantidas.append(linha)  # Guardar na lista

    with open(caminho, "w", encoding="utf-8") as arquivo:  # Modo escrita ("w") sobrescreve tudo
        arquivo.writelines(linhas_mantidas)  # Gravar apenas as linhas mantidas


# 5. [NOVO] Mostrar status dos quartos na tela
def exibir_quartos(quartos, reservados):
    print("\n=== STATUS DOS QUARTOS ===")
    for codigo, (nome, preco) in quartos.items():  # Percorrer dicionário
        status = " [RESERVADO]" if codigo in reservados else " [LIVRE]"  # Definir status
        print(f"{codigo} - {nome}: R$ {preco:.2f}/dia{status}")
    print("-" * 26)


# 6. [ATUALIZADO] Fluxo de reserva com validação de dias (try / except)
def fazer_reserva(quartos, reservados):
    exibir_quartos(quartos, reservados)

    cliente = input("Digite seu nome: ").strip()
    codigo_escolhido = input("Digite o número do quarto: ").strip()

    if codigo_escolhido not in quartos:
        print("Erro: Quarto inválido.")
        return

    if codigo_escolhido in reservados:
        print("Aviso: Este quarto já está reservado!")
        return

    # NOVO: Loop com try / except para garantir número inteiro válido
    while True:
        try:
            dias = int(input("Quantidade de dias: "))  # Tentar converter para inteiro
            if dias <= 0:  # Impedir 0 ou dias negativos
                print("Aviso: Digite um número maior que zero.")
                continue
            break  # Se deu certo, sai do loop
        except ValueError:  # Se digitar letras ou símbolos, cai aqui sem quebrar
            print("Erro: Digite apenas números inteiros (ex: 3).")

    nome_quarto, preco_diaria = quartos[codigo_escolhido]
    valor_total = preco_diaria * dias

    print(f"\nResumo: {nome_quarto} por {dias} dia(s) = R$ {valor_total:.2f}")
    confirmar = input("Confirmar reserva? (S/N): ").strip().upper()

    if confirmar == "S":
        salvar_reserva(cliente, codigo_escolhido, dias)
        print(f"Reserva confirmada para {cliente}!")
    else:
        print("Reserva cancelada pelo usuário.")



# 7. [NOVO] Fluxo para liberar quarto reservado
def liberar_quarto(quartos, reservados):
    exibir_quartos(quartos, reservados)

    if not reservados:  # Se conjunto estiver vazio
        print("Não há nenhum quarto reservado no momento.")
        return

    codigo_cancelar = input("Digite o número do quarto para liberar: ").strip()

    if codigo_cancelar not in reservados:  # Validar se realmente estava ocupado
        print("Aviso: Esse quarto não está reservado.")
        return

    cancelar_reserva(codigo_cancelar)  # Chamar função que apaga do arquivo
    print(f"Quarto {codigo_cancelar} liberado com sucesso!")


# 8. [ATUALIZADO] Menu contínuo (while)
def main():
    quartos = carregar_quartos()  # Carregar lista fixa de quartos

    while True:  # Laço infinito até escolher Sair
        reservados = carregar_reservas()  # Atualizar ocupação a cada volta do menu

        print("\n=== MENU DO HOTEL ===")
        print("1 - Ver quartos")
        print("2 - Fazer reserva")
        print("3 - Cancelar reserva (liberar quarto)")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_quartos(quartos, reservados)
        elif opcao == "2":
            fazer_reserva(quartos, reservados)
        elif opcao == "3":
            liberar_quarto(quartos, reservados)
        elif opcao == "4":
            print("Encerrando o sistema. Até logo!")
            break  # Quebrar o laço while e encerrar
        else:
            print("Opção inválida! Escolha de 1 a 4.")


if __name__ == "__main__":
    main()
