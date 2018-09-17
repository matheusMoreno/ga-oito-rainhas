# Oito Rainhas
Algoritmo genético que resolve o problema das oito rainhas. Feito para um trabalho da cadeira de Inteligência Artificial do curso de Engenharia Eletrônica na UFRJ.

## Regras do Algoritmo

1. Começamos com 6 pais, nossa geração zero, criados aleatoriamente. Para facilitarmos o código e a lógica do problema, tanto os pais quanto gerações subsequentes terão 1 rainha por linha, para não nos preocuparmos com rainhas em linhas iguais.
2. O gene de cada pai é formado por 8 inteiros entre 1 e 8 (inclusive). O primeiro valor é a coluna que se encontra a rainha da primeira linha, o segundo é a coluna que se encontra a rainha da segunda linha e assim sucessivamente.
3. Recombinamos os pais entre si, escolhendo de maneira aleatória que gene será herdado (do pai A ou B). Como temos muitas combinações possíveis, vamos nos limitar a 2 cruzamento por par de pais, gerando então 30 filhos.
4. Inserimos uma mutação (também aleatória!) em 6 filhos escolhidos aleatoriamente. A mutação consiste na substituição de um valor do gene por outro.
5. Contamos quantos ataques ocorrem por configuração e selecionamos as 5 melhores (menor número de ataques, menor não-aptidão) e um aleatório, descartando o resto.
6. Repetimos o processo a cada nova geração, até termos 5 gerações.
