# Simulador de Autômatos Finitos

Este projeto implementa um simulador de autômatos finitos (AFD, AFND, com transições vazias) que lê a especificação de uma máquina em formato JSON, um conjunto de palavras de teste em CSV, e gera um arquivo de saída com os resultados.

##  Objetivo

Simular o funcionamento de autômatos finitos com base em uma descrição formal da máquina de estados e uma série de palavras de entrada, validando se são aceitas ou rejeitadas.

##  Estrutura de Arquivos

- `automato.aut`: JSON com a definição da máquina.
- `testes.in`: CSV com palavras de entrada e resultado esperado.
- `saida.out`: saída gerada contendo os resultados da simulação.

### Exemplo de `automato.aut`

```json
{
  "initial": 0,
  "final": [4, 7],
  "transitions": [
    {"from": 0, "read": "a", "to": 1},
    {"from": 0, "read": "a", "to": 3},
    {"from": 2, "read": "a", "to": 3},
    {"from": 3, "read": "b", "to": 2},
    {"from": 4, "read": "a", "to": 4},
    {"from": 7, "read": "c", "to": 1},
    {"from": 4, "read": null, "to": 0}
  ]
}
