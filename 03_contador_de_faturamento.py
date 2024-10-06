import json

def ler_json(arquivo_jason):
    '''
    Abre para leitura um arquivo Json e retorna uma lista com dicionários.

    :param arquivo_jason: Local do arquivo Json
    :return: Uma lista com com dicionarios.
    '''
    arquivo = open(arquivo_jason, 'r')
    dados = json.load(arquivo)
    arquivo.close()
    return dados


def maior_valor_dicionario_na_lista(lista, key):
    '''
    Retorna o dicionário com o maior valor de acordo com a chave
    que utilizar.

    :param lista: Uma lista com dicionários
    :param key: A chave que tem os valores a serem medidos
    :return: O dicionário com o maior valor
    '''

    maior_valor = lista[0]

    for item in lista:
        if item[key] > maior_valor[key]:
            maior_valor = item

    return maior_valor


def menor_valor_dicionario_na_lista(lista, key):
    '''
    Retorna o dicionário com o menor valor de acordo com a chave
    que utilizar e o valor for maior que zero.

    :param lista: Uma lista com dicionários
    :param key: A chave que tem os valores a serem medidos
    :return: O dicionário com o menor valor
    '''

    menor_valor = lista[0]

    for item in lista:
        if item[key] < menor_valor[key] and item[key] > 0:
            menor_valor = item

    return menor_valor


def media_dicionario_na_lista(lista, key, valor_desconsiderado):
    '''
    Retorna a média dos valores de um dicionario dentro de uma lista
    considerando apenas os valores maiores que os definidos.

    :param lista: Uma lista com dicionarios
    :param key: A chave que está os valores a serem calculados
    :param valor_desconsiderado: Valores menores e iguais a esse não serão considerados
    :return: Uma média sem considerar os valores predefinidos.
    '''

    itens_validos = 0
    valor_total = 0

    for item in lista:
        if item[key] > valor_desconsiderado:
            itens_validos += 1
            valor_total += item[key]

    media = valor_total / itens_validos
    return media


#Programa Principal
dados = ler_json('dados.json') #Lê os dados do arquivo Json e cria a lista dados

menor_valor = menor_valor_dicionario_na_lista(dados, 'valor') #Pega o dicionário com menor valor
maior_valor = maior_valor_dicionario_na_lista(dados,'valor') #Pega o dicionário com maior valor
media = media_dicionario_na_lista(dados, 'valor', 0) #Media dos valores de todos os dicionários maiores que 0

dias_superior_a_media = [] #Lista que irá armazenar os dicionarios que tenham faturamento maior que a média

#Inseri os dicionarios em 'dias_superior_a_media'
for dia in dados:
    if dia['valor'] > media:
        dias_superior_a_media.append(dia)

#Formata a saída em tabelas
print('Menor fatura do mês: \n')
print(f'{"Dia":<3} {"Valor":>36}')
print(f'{maior_valor["dia"]:<3} {"R$":>25} {maior_valor["valor"]:>10.2f}')
print(40 * '-')

print('\nMenor fatura do mês: \n')
print(f'{"Dia":<3} {"Valor":>36}')
print(f'{menor_valor["dia"]:<3} {"R$":>25} {menor_valor["valor"]:>10.2f}')
print(40 * '-')

print('\nFatura maior que a média: \n')
print(f'{"Dia":<3} {"Valor":>36}')
for linha in dias_superior_a_media:
    print(f'{linha["dia"]:<3} {"R$":>25} {linha["valor"]:>10.2f}')

print(40 * "-")
