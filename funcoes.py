from random import randint
from constantes import CONSTANTES

def energia_inicial():
    return randint(20, 50)

def agua_inicial():
    return randint(5, 10)

def sede_inicial():
    return randint(40, 60)

def menos_energia():
    return randint(5, 15)

def sede_maior():
    return randint(5, 15)

def obter_longa_distancia():
    return randint(10, 20)

def nativos_andam():
    return randint(7, 14)

def curta_distancia(dicionario, distancia_oasis, sede, energia_do_camelo, distancia_nativos):
    
    if distancia_oasis in dicionario:
        dicionario[distancia_oasis] -= 2

    if sede in dicionario:
        dicionario[sede] += 2

    if energia_do_camelo in dicionario:
        dicionario[energia_do_camelo] -= 2

    if distancia_nativos in dicionario:
        dicionario[distancia_nativos] -= 2


def longa_distancia(dicionario, sede, energia_do_camelo, distancia_oasis, distancia_nativos):
    if sede in dicionario:
        dicionario[sede] += sede_maior()
    if energia_do_camelo in dicionario:
        dicionario[energia_do_camelo] -= menos_energia()
    if distancia_nativos in dicionario:
        dicionario[distancia_nativos] -= obter_longa_distancia()
    if distancia_oasis in dicionario:
        dicionario[distancia_oasis] -= obter_longa_distancia()
