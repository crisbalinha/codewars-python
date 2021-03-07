def is_interesting(number, awesome_phrases):
    if number <= 99:
        return 0
    elif number <= 0 or number > 1000000000:
        return 0
    else:
        # Verificar numeros com Zero seguido
        d = str(number)[1:]
        d = d.count('0')
        if d == int(len(str(number))) - 1:
            print('Numeros com 0')
            return 2

        # Numeros em Ordem Crescente ou Decrescente
        numeroInterassante = 0
        guarda = []
        guarda2 = str(number)
        for i in range(len(guarda2)):
            guarda.append(int(guarda2) % 10)
            guarda2 = str(int(guarda2) // 10)

        # Maoir para menor = Crescente, Menor para Maior = Descrecente
        if (sorted(guarda, reverse=True) == guarda):
            return 2
        elif (sorted(guarda) == guarda):
            return 2

        primeiro_digito = str(number)[:1]
        primeiro_digito = primeiro_digito.count(primeiro_digito)
        if (primeiro_digito == len(str(number))):
            return 2


print(is_interesting(1336, [1337, 256]))
