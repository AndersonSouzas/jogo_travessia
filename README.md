# Jogo Travessia do Deserto

Você é um viajante que precisa atravessar um deserto perigoso montado em seu camelo. Você está sendo perseguido por nativos hostis, e sua missão é chegar ao oásis antes que eles te alcancem. Durante a jornada, você deve gerenciar sua sede, o cansaço do camelo e a distância entre você e os nativos.

## Regras do Jogo

1. Você pode avançar uma curta ou longa distância a cada turno.
2. Você pode parar para beber água e saciar sua sede.
3. Você pode descansar, o que recupera a energia do camelo, mas os nativos se aproximam.
4. Se sua sede ficar muito alta, você morre de desidratação.
5. Se o camelo se cansar demais, ele pode morrer de exaustão.
6. Se os nativos te alcançarem, você será capturado.

### Ações do Jogador

- **A - Beber água**: O jogador consome uma unidade de água, reduzindo sua sede a zero.
  - Verifique se o jogador ainda tem água disponível. Se não tiver, mostre uma mensagem informando que a água acabou.
  
- **B - Avançar uma pequena distância**: O jogador avança uma pequena distância, aumentando a sede e o cansaço do camelo. Os nativos também avançam.
  - Gere um número aleatório entre 5 e 12 para a distância percorrida pelo jogador.
  - Aumente a sede e o cansaço do camelo.
  - Atualize as posições do jogador e dos nativos com números aleatórios.

- **C - Avançar uma longa distância**: O jogador avança uma grande distância, o que aumenta significativamente a sede e o cansaço do camelo. Os nativos também avançam, mas o jogador percorre uma distância maior.
  - Gere um número aleatório entre 10 e 20 para a distância percorrida.
  - Aumente a sede e o cansaço do camelo de forma mais intensa.
  - Atualize as posições do jogador e dos nativos com valores aleatórios.

- **D - Descansar**: O jogador para para descansar, o que reduz o cansaço do camelo a zero, mas os nativos se aproximam.
  - Faça com que os nativos avancem uma distância aleatória considerável (valores entre 7 e 14).

- **E - Verificar status**: O jogador pode visualizar o status atual, incluindo:
  - Distância percorrida
  - Sede
  - Cansaço do camelo
  - Distância dos nativos
  - Quantidade de água restante

- **F - Desistir**: O jogador desiste da travessia e o jogo termina.

## Fatores para Gerenciamento

- **Sede**: Aumenta quando o jogador avança. Se a sede atingir um limite crítico, o jogador morre.
- **Cansaço do camelo**: Aumenta quando o jogador avança. Se o camelo ficar muito cansado, ele pode morrer de exaustão.
- **Distância dos nativos**: Os nativos avançam a cada turno. Se eles alcançarem o jogador, o jogo termina com a captura do jogador.
