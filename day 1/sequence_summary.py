from pathlib import Path

def ler_fasta(arquivo):
    sequencias = {}
    nome = ""

    with open(arquivo, "r") as f:
        for linha in f:
            linha = linha.strip()

            if linha.startswith(">"):
                nome = linha[1:]
                sequencias[nome] = ""
            else:
                sequencias[nome] += linha

    return sequencias


def contar_gc(dna):
    g = dna.count("G")
    c = dna.count("C")
    tamanho = len(dna)
    gc = (g + c) / tamanho * 100
    return tamanho, gc


arquivo = r"E:\workspace\code\teste_fasta.txt"

sequencias = ler_fasta(arquivo)

for nome, dna in sequencias.items():
    tamanho, gc = contar_gc(dna)

    print(f"Nome: {nome}")
    print(f"Tamanho: {tamanho}")
    print(f"GC: {gc:.2f}%\n")
