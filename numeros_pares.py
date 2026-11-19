"""
faça um programa que imprime os numeros pares de 1 a 200

ex
'python numeros_pares.py'
2
4
6
8
...
"""

__version__ = "0.1.0"  #Identificação

while True: # Repetição contínua
    try: # Proteção contra erro • Execução segura
        limite = int(input("Digite o número final (maior que 0); ")) # Entrada do usuário (input) 
        if limite > 0: # Condição                                              # Conversão para inteiro (int)
            break # Interrupção                                                 # Armazenamento (limite)
        print("por favor, digite um número maior que zero.") # Regra de negócio
    except ValueError: # Captura de erro
        print("Entrada inválida! digite apenas números inteiros.") # Mensagem de erro

numeros_pares = [number for number in range(2, limite + 1, 2)] # List Comprehension

for par in numeros_pares: # Leitura da lista
    print(par) # Saída final




