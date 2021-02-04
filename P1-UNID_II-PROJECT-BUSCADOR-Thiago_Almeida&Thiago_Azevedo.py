#UNIFACISA - CENTRO UNIVERSITÁRIO
#SISTEMAS DE INFORMAÇÃO
#DISCIPLINA: PROGRAMAÇÃO 1
#PROFESSOR: JEMERSON DAMÁSIO
#EQUIPE: THIAGO LEANDRO ALMEIDA & THIAGO AZEVEDO SOARES
#MATRÍCULA: 2023080006 & 2023081065 / TURNO: MANHÃ

#>>>>>>>>>>>>>>>>>>>>>>>> PROJETO DE PROGRAMAÇÃO 1 - CRAWLER <<<<<<<<<<<<<<<<<<<<<<<<<<<<#
#BUSCADOR

#Importando a biblioteca necessária para carregamento do conteúdo armazenado
#através da Persistência de Dados (arquivo):
import json

#Outros conteudos indexados:
#>>> 'data_89radiorock'
#>>> 'data_rollingstone'

with open('data_jovempan.json') as json_file:
    dicionario = json.load(json_file)
print ()
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- BUSCADOR PYTHON -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print ('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=- Seu Crawler Web -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')
print ()
print ('by Almeida, Azevedo (2020)')
print ()

pergunta = 0
while pergunta != 2:
    pesquisa = input('Buscar no PYTHON: ').lower().split()
    pos_pesq = 0
    lista_sites = []
    for site, dados in dicionario.items():
        for pavavra in pesquisa:
            if pos_pesq < len(pesquisa) and pesquisa[pos_pesq] in dados:
                lista_sites.append(site)
            pos_pesq += 1
        pos_pesq = 0
    separador = " "
    output_pesquisa = separador.join(pesquisa)
    print()
    print(f'Seu resultado de busca para: {output_pesquisa}')
    print()
    lista_final = list(set(lista_sites))
    lista_final.sort()
    print(lista_final)
    print()
    pergunta = int(input('Deseja realizar uma nova pesquisa? (Digite: 1-SIM ou 2-NÃO(sair)): '))
    print()
print('Obrigado por usar o Buscador Python, volte sempre!')
