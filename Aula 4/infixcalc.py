#/ cd python/env
"""Calculadora Infix.

Funcionamento:

[operação] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Uso:
$ infixcalc.py sum 5 2
7

$ infixcalc.py mul 10 5
50

$ infixcalc.py 
operação: sum
n1: 5
n2: 4
9
"""

import os
from datetime import datetime
import sys
argumentos = sys.argv[1:]

# 1. verifica se os dados vieram pelo terminal ou se precisa pedir via input
if not argumentos:
    operacao = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")
    argumentos = [operacao, n1, n2]
elif len(argumentos) !=3:
    print("Numero de argumentos inválido!")
    print("Exemplo: sum 5 2")
    sys.exit(1)


operacao, n1, n2 = argumentos


# 2. valida a operação
operacoes_validas = ("sum", "sub", "mul", "div")
if operacao not in operacoes_validas:
    print("Operação inválida!")
    sys.exit(1)

# 3. Converte os números para float (aceita inteiros e decimais)
try:
    n1 = float(n1)
    n2 = float(n2)
except ValueError:
    print("Os valores n1 e n2 precisam ser numeros!")
    sys.exit(1)


# 4. Faz o cálculo
if operacao == "sum":
    resultado = n1 + n2
elif operacao == "sub":
    resultado = n1 - n2
elif operacao == "mul":
    resultado = n1 * n2
elif operacao == "div":
    resultado = n1 / n2

print(f"O resultado é {resultado}")

# --- Parte nova: Salvando no arquivo de log

# 1. Define o caminho do arquivo na pasta atual
path = os.curdir
filepath = os.path.join(path, "infixcalc.log")


# 2. Pega a data e hora exata da conta
timestamp = datetime.now().isoformat()


# 3. Pega o nome do usuário logado no Windows
user = "Denise Gomes"
user = os.getenv("USER", "Denise Gomes")


# 4. Abre o arquivo e escreve a linha de histórico
with open(filepath, "a") as file_:
    file_.write(f"{timestamp} - {user} - {operacao}, {n1}, {n2} = {resultado}\n")



