dicionario = {1: 'a',
              2: 'b',
              3: 'c',
              4: 'd',
              5: 'e',
              6: 'f',
              7: 'g',
              8: 'h',
              9: 'i',
              10: 'j',
              11: 'k',
              12: 'l',
              13: 'm',
              14: 'n',
              15: 'o',
              16: 'p',
              17: 'q',
              18: 'r',
              19: 's',
              20: 't',
              21: 'u',
              22: 'v',
              23: 'w',
              24: 'x',
              25: 'y',
              26: 'z'

              }

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

"""
def high(x):
    x = x.split()
    soma = 0
    maiorNumero = 0
    maiorPalavra = ''
    for i in range(len(x)):
        for h in range(len(x[i])):
            for y in range(1, len(dicionario) + 1):
                d = dicionario[y]
                if x[i][h] == dicionario[y]:
                    soma += y
        if (soma > maiorNumero):
            maiorPalavra = x[i]
            maiorNumero = soma
        soma = 0
    return maiorPalavra
"""

print(high('man i need a taxi up to ubud'))
