import itertools

import itertools


def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


"""
def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for indice, letraString in enumerate(string):
            for stringRetorno in permutations(string[:indice] + string[indice + 1:]):
                result.add(letraString + stringRetorno)

    return list(result)
"""

"""
def permutations(string):
    l  = []
    lista = list(itertools.permutations(string))
    letra = ''
    for index, i in enumerate(lista):
        letra = ''
        for j in range(len(lista[index])):
            letra += lista[index][j]
        if l.count(letra) == 0:
            l.append(letra)
    return l

"""

# print(permutations('aabb'))
lista = []
for p in set(itertools.permutations('aabb')):
    lista.append(''.join(p))
print(lista)
