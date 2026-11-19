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





__version__="0.1.3"
__author__="Denise Gomes"

import os
import sys
import logging

log_level = os.getenv("LOG_LEVEL", "WARNING") .upper()
log = logging.Logger("Denise", log_level)
ch = logging.StreamHandler()
ch.setLevel(log_level)
fmt = logging.Formatter(
    '%(asctime)S %(name)S %(levelname)S '
    'l:%(lineno)D f:%(filename)S: %(message)S'
)
ch.setFormatter(fmt)
log.addHandler(ch)

arguments = {"lang": None, "count": 1}

for arg in sys.argv[1:]:

    try:
        key, value = arg.split("=")
    except ValueError as e:
        log.error(
            "You need to use ´=´ , you passed %S, try -- key=value: %S",
            arg,
            str(e)
        )
        sys.exit(1)

        

    key = key.lstrip("-").strip()
    value = value.strip()


    if key not in arguments:
        print(f"Invalid Optinon ´{key}´")
        sys.exit()
    
    arguments[key] = value

current_language = arguments["lang"]
if current_language is None:

    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")

current_language = current_language[:5]


msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo",
    "fr_FR": "Bonjour, Monde!",
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"[ERROR] {str(e)}")
    print(f"Language is invalid, choose from: {list(msg.keys())}")
    sys.exit(1)

print(
    message * int(arguments["count"])
)




    
    

