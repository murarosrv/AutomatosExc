import json
import csv
import sys
import time

def carregar_automato(caminho_arquivo):
    with open(caminho_arquivo, 'r') as f:
        dados = json.load(f)
    return dados["initial"], dados["final"], dados["transitions"]

def carregar_testes(caminho_arquivo):
    testes = []
    with open(caminho_arquivo, 'r') as f:
        leitor = csv.reader(f, delimiter=';')
        for linha in leitor:
            if linha:
                testes.append((linha[0], int(linha[1])))
    return testes

def construir_grafo_transicoes(transicoes):
    grafo = {}
    for trans in transicoes:
        origem = trans['from']
        simbolo = trans['read']
        destino = trans['to']
        grafo.setdefault(origem, {}).setdefault(simbolo, []).append(destino)
    return grafo

def epsilon_closure(estados, grafo):
    stack = list(estados)
    closure = set(estados)
    while stack:
        estado = stack.pop()
        for prox in grafo.get(estado, {}).get(None, []):
            if prox not in closure:
                closure.add(prox)
                stack.append(prox)
    return closure

def executar_automato(palavra, estado_inicial, estados_finais, grafo):
    inicio = time.time()
    estados_atuais = epsilon_closure([estado_inicial], grafo)
    for simbolo in palavra:
        novos_estados = set()
        for estado in estados_atuais:
            destinos = grafo.get(estado, {}).get(simbolo, [])
            for dest in destinos:
                novos_estados.update(epsilon_closure([dest], grafo))
        estados_atuais = novos_estados
        if not estados_atuais:
            break
    fim = time.time()
    tempo = round(fim - inicio, 3)
    return int(any(estado in estados_finais for estado in estados_atuais)), tempo

def escrever_saida(caminho_saida, resultados):
    with open(caminho_saida, 'w') as f:
        for palavra, esperado, obtido, tempo in resultados:
            f.write(f"{palavra};{esperado};{obtido};{tempo:.3f}\n")

def main():
    if len(sys.argv) != 4:
        print("Uso: python Automato.py automato.aut testes.in saida.out")
        return

    automato_path, testes_path, saida_path = sys.argv[1], sys.argv[2], sys.argv[3]

    estado_inicial, estados_finais, transicoes = carregar_automato(automato_path)
    testes = carregar_testes(testes_path)
    grafo = construir_grafo_transicoes(transicoes)

    resultados = []
    for palavra, esperado in testes:
        obtido, tempo = executar_automato(palavra, estado_inicial, estados_finais, grafo)
        resultados.append((palavra, esperado, obtido, tempo))

    escrever_saida(saida_path, resultados)

if __name__ == "__main__":
    main()
