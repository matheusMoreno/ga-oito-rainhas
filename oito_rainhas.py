# Regras do algoritmo no README.md.
# O codigo foi feito apenas para 6 pais por geracao. Talvez eu mude isso algum dia.

from random import randint
from collections import Counter

def geracao_inicial():
    """Retorna uma lista com 6 pais para a geracao 0, cada um com 8 inteiros em [1, 8]."""
    return [[randint(1, 8) for y in range(8)] for x in range(6)]
    
def recombinacao(pais):
    """Retorna uma lista com filhos gerados de recombinacoes aleatorias."""
    
    filhos = []
    for x in range(6):
        for y in range(6):
            if (x != y):
                filhos += [[(pais[x][k] if (randint(0, 1) == 0) else pais[y][k]) for k in range(8)]]
    return filhos

def mutacao(filhos):
    """Insere um gene de mutacao aleatorio em 6 filhos aleatorios."""
    
    mutantes = []
    index = []
    
    # Para que nao repetamos filhos, esse bloco gera 6 indices diferentes.
    while (len(index) != 6):
        p_i = randint(0, 29)
        if not (p_i in index):
            index += [p_i]
    
    # Inserimos a mutacao em cada filho.
    for i in index:
        mut = filhos[i]
        i_m = randint(0, 7)
        novo_gene = randint(1, 8)
        while (mut[i_m] == novo_gene): # Se o novo valor for o mesmo que o antigo,
            novo_gene = randint(1, 8)  # nao havera mutacao! Precisamos checar isso
        mut[i_m] = novo_gene
        mutantes += [mut]
        
    return mutantes
    
def contagem_ataques(gene_pool):
    """Retorna a quantidade de ataques presentes em cada membro de gene_pool."""
    
    # Para uma das checagens diagonais, precisamos de um vetor de pesos.
    pesos = [7, 5, 3, 1, -1, -3, -5, -7]
    ataques = []
    
    for ser in gene_pool:
        diagonais_1 = [x + ser[x] for x in range(8)]
        diagonais_2 = [x + ser[x] + pesos[x] for x in range(8)]
        qtd = 0
        for l in range(8):
            qtd += Counter(ser)[ser[l]] - 1
            qtd += Counter(diagonais_1)[diagonais_1[l]] - 1
            qtd += Counter(diagonais_2)[diagonais_2[l]] - 1
        ataques += [int(qtd/2)]
    
    return ataques

def melhores_pior(gene_pool, ataques):
    """Escolhe os 5 melhores e um piot ser de gene_pool, baseado em suas qtds de ataques."""
    
    # Juntamos os dois vetores e os organizamos pela quantidade de ataques.
    ser_ataque = [[gene_pool[k], ataques[k]] for k in range(len(gene_pool))]
    organizado = sorted(ser_ataque, key=lambda e: e[1])
    melhor_pior = organizado[:5] + [organizado[randint(5, len(organizado)-1)]]
    
    # Imprimimos na tela os escolhidos.
    for x in melhor_pior:
        print("Gene: {} // Ataques: {}".format(x[0], x[1]))
        
    return [x[0] for x in melhor_pior]
