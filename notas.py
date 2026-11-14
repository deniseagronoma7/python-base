#!/usr/bin/env python
"""bloco de notas

$ notas.py new "Minha Nota"
tag: tech
text:
Anotacao geral sobre carreira de tecnologia

$ notas.py read --tag=tech
...
...
"""
__version__ = "0.1.0" 
""

import os
import sys

# sys.argv guarda tudo no terminal
# Usamos [1:] para ignorar o nome do arquivo (notas.py) e pegar só os comandos
# Define onde o arquivo será salvo
filepath = os.path.join(os.curdir, "notas.txt")

arguments = sys.argv[1:]

# se nao digitou nenhum comando depois de notas.py, o programa avisa e encerra
if not arguments:
    print("uso invalido. Digite 'new' ou 'read' após o nome do arquivo.")
    sys.exit(1)

# Pegamos o primeiro comando digitado (que deve ser "new" ou "read")
comando = arguments[0]

if comando == "new":
    # O segundo item da lista (indice) é o titulo da nota
    # verifica se voçe digitou o titulo da nota depois de 'new'
    if len(arguments) < 2:
        print("Erro: Informe o título da nota entre aspas.")
        sys.exit(1)

    
    titulo = arguments

    # o input () pausa o programa e espera voçe digitar algo e apertar enter
    tag = input("tag: ").strip()
    text = input("text:\n").strip()

    # Abre o arquivo 'notas.txt' no modo "a" (append = adicionar no final sem apagar o que já existe)
    with open(filepath, "a", encoding="utf-8") as arquivo:
        # Grava os 3 dados na mesma linha separados por TAB (\t)
        arquivo.write(f"{titulo}\t{tag}\t{text}\n")

    print("\nNota salva com sucesso!")

elif comando == "read":
      # Verifica se o arquivo 'notas.txt' já existe antes de tentar ler
    if not os.path.exists(filepath):
        print("Nenhuma nota encontrada. Crie uma nota primeiro usando 'new'.")
        sys.exit(1)


     # Procura se você passou algum filtro como --tag=tech
    filtro_tag = ""
    for arg in arguments[1:]:
        if arg.startswith("--tag="):
            filtro_tag = arg.split("=")

    # Abre o arquivo para leitura ("r" = read)
    with open(filepath, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            # Separa a linha de volta nas 3 variáveis usando o TAB (\t)
            titulo, tag, text = linha.strip().split("\t")

             # Se não houver filtro ou se a tag bater com o filtro, mostra na tela
            if not filtro_tag or tag == filtro_tag:
                print(f"\nTítulo: {titulo}")
                print(f"Tag: {tag}")
                print(f"Texto: {text}")
                print("-" * 25)

else:
    print("Comando desconhecido. Use 'new' ou 'read'.")
    

    

