#! /usr/bin/env python3
'''Hello World multi Linguas.

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada ex:

    export LANG=PT_BR

Execução:

    python hello.py
'''


__version__="0.1.2"
__author__="Denise Gomes"
__license__="Unlicense"


import os

current_language = os.getenv("LANG", "en_US")[:5]

#msg = "Hello, World!"

# set (Hash Table) - O(1) - constante
# dicts (Hash Table)

#Ordem Complexidade O(n)
#if current_language == "pt_BR":
    msg = "Olá, Mundo!"
#elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
#elif current_language == "es_SP":
    msg = "Hola, Mundo!"
#elif current_language == "fr_FR":
    msg = "Bonjour Monde"
    
#print(msg)


msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])





__version__="0.0.3"
__author__="Denise Gomes"

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo",
    "fr_FR": "Bonjour, Monde!",
}

print(msg[current_language])




    
    

