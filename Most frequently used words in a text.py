def top_3_words(text):
    lista = text.split('\n')
    lista2 = list(i.split(' ') for i in lista)

    somaLista = []
    for i in lista2:
        somaLista.extend(i)



    letra1 = 0
    letra2 = 0
    letra3 = 0
    for indice, palavra in enumerate(set(somaLista)):
        quantidade = text.count(palavra)
        if quantidade > letra1:
            letra1 = quantidade
        elif quantidade > letra2:
            letra2 = quantidade
        elif quantidade > letra3:
            letra3 = quantidade

    return lista


print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income."""))
