from funcoes import curta_distancia, longa_distancia, nativos_andam, agua_inicial, energia_inicial, sede_inicial
from constantes import CONSTANTES
from pprint import pprint

status = {
'Distancia Até Chegar Ao Oásis': 100,
'Distancia dos Nativos Hostis ': 50,
'Água Disponivel': agua_inicial(),
'Energia do Camelo': energia_inicial(),
'Sede': sede_inicial()
}

escolhas = {
    'A': 'Beber água',
    'B': 'Avançar Curta Distância',
    'C': 'Avançar Longa Distância',
    'D': 'Descansar',
    'E': 'Visualizar Status',
    'F': 'Desistir'
}

jogo = True

while jogo:
        
        pprint(escolhas)
        print()
        escolha = input("Faça seu movimento:")
        escolha = escolha.lower()
        escolha = escolha.strip()
        
        
        #Definição de Movimentos
        if escolha == 'a': #BEBER AGUA
            if status['Água Disponivel'] > 0:
                status['Sede'] = 0
            else:
                print("Sua água acabou")
        
        elif escolha == 'b': #AVANÇAR CURTA DISTÂNCIA
            curta_distancia(status, 'Distancia Até Chegar Ao Oásis', 'Sede', 'Energia do Camelo', 'Distancia dos Nativos Hostis ')
        
        elif escolha == 'c': #AVANÇAR LONGA DISTÂNCIA
            longa_distancia(status, 'Sede', 'Energia do Camelo', 'Distancia Até Chegar Ao Oásis', 'Distancia dos Nativos Hostis ')

        elif escolha == 'd': #DESCANÇAR
            status['Energia do Camelo'] = CONSTANTES.MAX_ENERGIA
            status['Distancia dos Nativos Hostis '] -= nativos_andam()
        
        elif escolha == 'e': #VERIFICAR STATUS
            print("-----------------------------------------")
            print("STATUS ATUAL:")
            pprint(status)
            print("-----------------------------------------")

        elif escolha == 'f': #DESISTIR
            print("Você desistiu")
            jogo = False
        
        else:
            print("Movimento fora das opções")
            print("Escolha de novo:")
            print()

        if status['Distancia Até Chegar Ao Oásis'] <= 0:
            print("PARABÉNS! Você chegou ao Oasis e está a salvo")
            jogo = False
        
        if status['Distancia dos Nativos Hostis '] <= 0:
            print("Você foi capturado pelos nativos hostis e perdeu o jogo")
            jogo = False
        
        if status['Sede'] == CONSTANTES.MAX_SEDE:
            print("Você morreu por desidratação e perdeu o jogo")
        
        if status['Energia do Camelo'] == 0:
            print("Seu camelo morreu de cansaço e os nativos hostis te capturaram\nFIM DE JOGO")
            jogo = False