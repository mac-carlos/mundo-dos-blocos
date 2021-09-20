# Mundo dos Blocos

## Introdução

No mundo dos blocos (A, B, C) existem apenas 3 pilhas possíveis aonde os referidos blocos podem ser deixados/empilhados. Levando em consideração que neste problema não é exigida uma empilhadeira para movimentação dos blocos, desenvolva uma solução (em Python) para este problema partindo do princípio da aleatoriedade da disposição dos blocos no cenário. O estado OBJETIVO para esse problema é aquele em que a disposição na PILHA CENTRAL esteja: CBA, onde C é a base e A o topo da pilha. Lembre-se de que existem restrições nesse mundo, tal qual, só pode ser movimentado um bloco por vez, e não existe a possibilidade de movimentar um bloco qualquer desde que existam outro(s) bloco(s) acima deste. Você também pode deixar a cargo do usuário inserir as informações a respeito do estado inicial e do estado objetivo, desde que já exista a forma aleatória de inicialização do cenário no código. Deve-se implementar uma das buscas vistas no conteúdo de Busca em Espaço de Estados (BFS ou DFS). A saída deve ser: SUCESSO ou FALHA, pois quando há sucesso, você deve mostrar o CAMINHO que foi encontrado do estado inicial até o estado objetivo. 

* Será adicionado um bônus de 0.1 no fim do semestre para aqueles que desenvolverem soluções para o mundo dos blocos com mais do que apenas 3 blocos e 3 pilhas. Ou seja, o usuário deve inserir com quantos blocos e quantas pilhas o cenário deveria ter. 

* Para casos, onde não exista forma de movimentação (principalmente quando se eleva o número de blocos), deve-se reiniciar o sistema, alertando o usuário de que não existe meio possível de sair daquela posição aleatória e chegar ao objetivo.

## Uso

*Você precisa do Python instalado na máquina*

1. No CMD clone o repositório com

```bash
https://github.com/mac-carlos/mundo-dos-blocos.git
```

2. Va até a pasta do código

```bash
cd mundo-dos-blocos/codigo
```

3. Rode o algoritmo

```bash
py main.py
```

## Licença 

Este projeto está sobre a [Licença MIT](LICENSE).