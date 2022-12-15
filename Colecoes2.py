def iniciando_com_conjuntos_e_suas_operacoes():

    # Dada uma lista:
    lista_de_numeros = [1, 2, 3, 4, 4, 9, 31, 16]
    print(f"Lista Original: {lista_de_numeros}")

    # Um conjunto por definição não possui elementos repetidos e diferente da lista, não possui uma ordem para os
    # elementos contidos nele.
    criando_um_conjunto = set(lista_de_numeros)
    print(f"Conjunto Criado: {criando_um_conjunto}\n")

    # Um conjunto imutavel não pode ter seus elementos alterados por nenhum método
    criando_um_conjunto_imutavel = frozenset(lista_de_numeros)
    print(f"Conjunto imutavel: {criando_um_conjunto_imutavel}\n")

    # Adiciona um elemento ao conjunto
    criando_um_conjunto.add(15)
    print(f"Método .add() para adicionar um elemento ao conjunto: {criando_um_conjunto}")
    # Remove um elemento do conjunto e retorna erro caso esse elemento não exista
    criando_um_conjunto.remove(31)
    print(f"Método .remove() para remover um elemento do conjunto: {criando_um_conjunto}")
    # Remove um elemento do conjunto se ele pertencer ao conjunto
    criando_um_conjunto.discard(4)
    print(f"Método .discard() para remover um elemento caso ele exista no conjunto: {criando_um_conjunto}")
    # Remove todos os elementos de um conjunto
    criando_um_conjunto.clear()
    print(f"Método .clear() para remover todos os elementos contidos do conjunto: {criando_um_conjunto}\n")

    print("Teoria dos conjuntos:")

    conjunto1 = {"Mayara", "Yan", "Fabio", 49, 7}
    conjunto2 = {(13, 27), 2, 7, 3, 49, 6, 5, "Yan", 78, 63}

    intersecao = conjunto1 & conjunto2
    uniao = conjunto1 | conjunto2
    uniao_exclusiva = conjunto1 ^ conjunto2
    diferenca = conjunto1 - conjunto2

    print(f"Conjunto 1: {conjunto1}")
    print(f"Conjuntos 2: {conjunto2}\n")
    print(f"Retorna os elementos que pertecem ao conjunto 1 e ao conjunto 2: {intersecao}")
    print(f"Retorna os elementos que pertecem ao conjunto 1 ou ao conjunto 2: {uniao}")
    print(f"Retorna os elementos que pertecem exclusivamente ao conjunto 1 ou ao conjunto 2: {uniao_exclusiva}")
    print(f"Retorna os elementos que pertecem ao conjunto 1 e não ao conjunto 2: {diferenca}\n")

    # Manipulando strings para conjuntos:

    texto_base = "Eu gosto de yakisoba e não gosto de refrigerante"

    conjunto_de_letras = set(texto_base)
    conjunto_de_palavras = set(texto_base.split())

    print("Conjuntos com strings: ")
    print("String: ", texto_base)
    print("Retorna um conjunto com todos os elementos dentro da string texto_base: ", conjunto_de_letras)
    print("Retorna um conjunto que contem todos os elementos separado por um espaço: ", conjunto_de_palavras)


def aprendendo_sobre_dicionarios():
    # Criando um dicionario

    abreviacao_estados = {
        "Sao Paulo": "SP",
        "Pernambuco": "PE",
        "Distrito Federal": "DF",
        "Paraiba": "PB"
    }

    # Como pesquisar o valor de uma chave
    valor_chave_sao_paulo = abreviacao_estados["Sao Paulo"]

    # Método .get(key, return value) procura usando o primeiro argumento como chave e retorna o segundo argumento
    # caso a chave não seja encontrada no dicionário
    valor_chave_rio_de_janeiro = abreviacao_estados.get("Rio de Janeiro", "Estado não encontrado")

    # Dicionários tambem suportam List Comprehension
    exemplo_list_comprehension_com_dicionarios = {estado for estado in abreviacao_estados if len(estado) >= 10}

    print("Dicionário", abreviacao_estados, "\n")
    print("Valor contido na chave 'Sao Paulo' => ", valor_chave_sao_paulo)
    print("Utilizando List Comprehension => ", exemplo_list_comprehension_com_dicionarios)
    print("Retorno de um chave não existente com o método .get() => ", valor_chave_rio_de_janeiro, "\n")

    print("Outra Forma de criar dicionários: varivável = dict(key=value)")
    usuario_e_idade = dict(Yan=27, Mayara=27, Fabio=51)
    usuario_e_idade2 = dict(Fabiana=53, Ruzinete=78)
    print("new_dictionary = dict(Yan=27, Mayara=27, Fabio=51) => ", usuario_e_idade, "\n")

    print("Alterando elementos em um dicionário: \n")

    usuario_e_idade["Yasmin"] = 15
    print("Adicionar uma nova chave ou alterar uma chave existente: dict_name[key] = value => ", usuario_e_idade)

    del usuario_e_idade["Fabio"]
    print("Remover uma chave de um dicionário: del dict_name['key'] => ", usuario_e_idade)

    usuario_e_idade.pop("Yasmin", "Usuário não encontrado")
    print(f"Remove, casos exista, uma chave do dicionário usando o comando: dict_name.pop(key, message). Caso não "
          f"exista, retorna a mensagem => {usuario_e_idade}")

    usuario_e_idade.update(usuario_e_idade2)
    print(f"Juntar 2 dicionários: dict_name1.update(dict_name2) => {usuario_e_idade}")

    print("Transformando um dicionário em uma lista: list(dict_name) => ", list(usuario_e_idade), "\n")

    print("Imprimindo as chaves e seus valores: ")

    print("Chaves: ")
    for elemento in usuario_e_idade.keys():
        print(elemento)
    print("\n")
    print("Valores: ")
    for elemento in usuario_e_idade.values():
        print(elemento)
    print("\n")
    print("Chaves e Valores: ")
    for elemento in usuario_e_idade.items():
        print(elemento)
    print("\n")

    print("Verificando se há uma chave em um dicionario:\n")

    print("Dicionário: ", usuario_e_idade)
    print(f"A chave 'Fabio' existe no dicionário usuario_e_idade: ", "Fabio" in usuario_e_idade)
    print(f"A chave 'Yan' existe no dicionário usuario_e_idade: ", "Yan" in usuario_e_idade, "\n")

    print("Verificando se há um valor em um dicionario:\n")
    print("Dicionário: ", usuario_e_idade)
    print("O Valor 30 existe no dicionário usuarios_e_idade: ", 30 in usuario_e_idade.values())
    print("O Valor 27 existe no dicionário usuarios_e_idade: ", 27 in usuario_e_idade.values())


def contagem_de_dicionarios_padrao():
    texto_base = "Meu nome é Yan meu carro tem quatro portas tenho dois gatos e meu nome completo é Yan Victor" \
                 " Borba Araújo".lower().split()

    aparicoes = {}

    for palavra in texto_base:
        apareceu = aparicoes.get(palavra, 0)
        aparicoes[palavra] = apareceu + 1

    print(aparicoes)


def contagem_de_dicionarios_com_defaultdict():
    from collections import defaultdict

    texto_base = "Meu nome é Yan meu carro tem quatro portas tenho dois gatos e meu nome completo é Yan Victor " \
                 "Borba Araújo".lower().split()

    aparicoes = defaultdict(int)

    for palavra in texto_base:
        aparicoes[palavra] += 1
    print(aparicoes)

    class Conta:
        def __init__(self):
            print("Criando um conta")

    # Ao definimos o valor default do dicionario como 0 através do defaultdict(int), dizemos ao programa que quando
    # não houver um valor inicial, o código deve assumir que o valor da chave é 0.
    print("\nForma de escrita do defaultdict: dictionary_name = defaultdict(default_factory)\n")
    print("Exemplos de default_factory:")
    print("int() = ", defaultdict(int))
    print("float() = ", defaultdict(float))
    print("str() = ", defaultdict(str))
    print("list() = ", defaultdict(list))
    print("dict() = ", defaultdict(dict))
    print("tuple() = ", defaultdict(tuple))
    print("set() = ", defaultdict(set))
    print("class Conta = ", defaultdict(Conta))


def contagem_de_dicionarios_com_counter():
    from collections import Counter

    texto_base = "Meu nome é Yan meu carro tem quatro portas tenho dois gatos e meu nome completo é Yan Victor " \
                 "Borba Araújo".lower().split()

    contador = Counter(texto_base)
    print(contador)


def usando_todo_conteudo_do_curso():

    texto1 = ''' 

        E o que há de interessante nessas funções de comparação profunda? O legal é que elas realizam
     comparações entre as propriedades e seus respectivos valores de estruturas que foram passadas para elas.

     Mas é importante ressaltar o seguinte: essas comparações são feitas a nível de valor das propriedades,
     e não em nível de endereço de memórias. São comparações profundas, isto é, se forem encontradas propriedade
     aninhadas, estas serão comparadas também.

     O resultado dessas funções é um valor booleano: true (no caso de ambas as estruturas forem idênticas, tanto
     em quantidade de propriedades e quanto em valores) e false (no caso de alguma correspondência for diferente).

     Em meu último artigo, vimos como o interpretador do JavaScript armazena dados em memória. Portanto, sabemos 
     que se compararmos com o operador Strict equal operator (===) duas estruturas distintas, mas com entradas
     iguais, teremos um resultado falsy.

    '''

    texto2 = '''

    Atualmente, muito se fala sobre computação em nuvem: “Meus dados estão subindo para o Dropbox!”, “Minha empresa
    está usando a nuvem como ferramenta de escritório para uso no dia a dia!” ou “Somos uma pequena empresa e
    utilizamos uma infraestrutura na nuvem”. Mas, afinal, o que é essa “nuvem”?

    Uma nuvem pode ser entendida como um conjunto de aplicações, armazenamento e computação que tem como base a internet
    como plataforma de funcionamento. E esse pool de serviços possui capacidade suficiente para dar suporte à maioria 
    das necessidades de grande parte dos usuários.

    '''

    def analisa_frequencia_de_letras(texto):

        from collections import Counter
        aparicoes = Counter(texto.lower())
        total_caracteres = sum(aparicoes.values())

        proporcoes = Counter(dict([(letra, frequencia / total_caracteres) for letra, frequencia in aparicoes.items()]))
        caracteres_mais_comuns = proporcoes.most_common(10)
        for caractere, frequencia in caracteres_mais_comuns:
            print(f"Caracter '{caractere}' ==> Frequência: {frequencia*100:.2f}%")
        print("\n")

    analisa_frequencia_de_letras(texto1)
    analisa_frequencia_de_letras(texto2)


aprendendo_sobre_dicionarios()









