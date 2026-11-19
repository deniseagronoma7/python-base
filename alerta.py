"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de
umidade do ar sendo que caso será exibida uma mensagem de alerta dependendo das
condições:

temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"
temp maior que 30 e temp vezes 3 for maior ou igual a umidade:
    "ALERTA!!! 🥵♒ Perigo de calor úmido"
temp entre 10 e 30: "😀 Normal"
temp entre 0 e 10: "🥶 Frio"
temp <0: "ALERTA!!! ⛄ Frio Extremo."

ex:
python alerta.py
temperatura: 30
umidade: 90
...
"ALERTA!!! 🥵♒ Perigo de calor úmido"
"""

import logging  # Importação • Biblioteca nativa de logs

__version__ = "0.1.0"

#configuração e criação do objeto log
logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s: %(message)s")
log = logging.getLogger("alerta") # variavel curta 'log'

def ler_numero(mensagem):  # funçaoreutilizavel coleta e valida os num.
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            log.error("Entrada invalida! Digite apenas números")  # usa log.error

def verificar_clima(temp, umidade):  # Funçao principal regras do clima
    if temp > 45:
        log.critical("ALERTA'!!! 🥵 Perigo calor extremo")
    elif temp >= 30 and temp * 3 >= umidade:
        log.critical("ALERTA!!! 🥵♒ Perigo de calor úmido")
    elif temp >= 10 and temp and temp <= 30:
        log.info(" 😀 Normal")
    elif temp >= 0 and temp < 10:
        log.warning("🥶 frio")
    else:
        log.critical("ALERTA!!! ⛄ Frio Extremo")


# Execução do programa
temperatura = ler_numero("temperatura: ")
umidade = ler_numero("umidade: ")
verificar_clima(temperatura, umidade)
