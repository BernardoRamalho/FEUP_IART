# TODO: Porque estamos demasiado cansados para pegar nisto já :D

https://www.youtube.com/watch?v=ZxXKISVkH6Y -> Link do video para como criar o environment.

https://github.com/genyrosk/gym-chess -> Link do Chess Environment

### 1. Criar __init__.py com a info do environment na raiz da pasta

#### 2. Criar pasta env com o environment per se.

##### 2.1 Defenir o environment

- [ X ] Defenir espaço de ações (numero de peças * numero de posições no tabuleiro)
- [ X ] Função para dado um estado e um jogador -> calcular jogadas possíveis
- [ ] Função que dado um estado e uma jogada, efetua-a -> retorna novo estado -> Função que mapeia jogadas em actions e vice versa
- [ ] Defenir observation space (que neste caso é o estado porque é o que o agent "vê")
- [ ] Defenir __init__ e reset do environment
- [ ] Defenir step do agent (o que calcula e efetua um passo do agent)

##### Que queremos:

- Rewards/1000 episodes

- Tempo que demora a treinar/1000 episódios

- Comparar QL vs SARSA
