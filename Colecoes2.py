def iniciando_com_conjuntos_e_operacoes():

    # Dada uma lista:
    lista_de_numeros = [1, 2, 3, 4, 4, 9, 31, 16]
    print(f"Lista Original: {lista_de_numeros}")

    # Um conjunto por definição não possui elementos repetidos e diferente da lista, não possui uma ordem para os
    # elementos contidos nele.
    criando_um_conjunto = set(lista_de_numeros)
    print(f"Conjunto Criado: {criando_um_conjunto}\n")

    # Um conjunto imutavel não pode ter seus elementos alterados por nenhum método
    criando_um_conjunto_imutavel = frozenset(lista_de_numeros)
    print(criando_um_conjunto_imutavel, "\n")

    criando_um_conjunto.add(15)  # Adiciona um elemento ao conjunto
    criando_um_conjunto.remove(31)  # Remove um elemento do conjunto e retorna erro caso esse elemento não exista
    criando_um_conjunto.discard(4)  # Remove um elemento do conjunto se ele pertencer ao conjunto
    criando_um_conjunto.clear()  # Remove todos os elementos de um conjunto

    print("Teoria dos conjuntos:")

    conjunto1 = {"Mayara", "Yan", "Fabio", 49, 7}
    conjunto2 = {(13, 27), 2, 7, 3, 49, 6, 5, "Yan", 78, 63}

    intersecao = conjunto1 & conjunto2
    uniao = conjunto1 | conjunto2
    uniao_exclusiva = conjunto1 ^ conjunto2
    diferenca = conjunto1 - conjunto2

    print(f"Conjunto 1: {conjunto1}")
    print(f"Conjuntos 2: {conjunto2}\n")
    print(f"Retorna os elementos que pertecem ao conjunto1 e ao conjunto 2: {intersecao}")
    print(f"Retorna os elementos que pertecem ao conjunto1 ou ao conjunto 2: {uniao}")
    print(f"Retorna os elementos que pertecem exclusivamente ao conjunto1 ou ao conjunto 2: {uniao_exclusiva}")
    print(f"Retorna os elementos que pertecem ao conjunto1 e não ao conjunto 2: {diferenca}\n")


iniciando_com_conjuntos_e_operacoes()
