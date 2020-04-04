import json
from time import sleep

# Importa dados de um arquivo .json
with open('c:/Users/carlo/OneDrive/Desenvolvimento/GitHub/Diversos/covid19.json') as arquivo:
    dict_covid19 = json.load(arquivo)

# Estrutura do arquivo .json
# { records : [ {dict_1} , {dict_2} , {dict_3} , ... , {dict_n} ] }

# Menu de Opções
países = {
    1:  ['Brasil'        , 'BRA'  ],
    2:  ['China'         , 'CHN'  ],
    3:  ['Itália'        , 'ITA'  ],
    4:  ['Espanha'       , 'ESP'  ],
    5:  ['Portugal'      , 'PRT'  ],
    6:  ['Estados Unidos', 'USA'  ],
    7:  ['Reino Unido'   , 'GBR'  ],
    8:  ['Argentina'     , 'ARG'  ],
    9:  ['OUTRO'         , 'OUTRO'],
    10: ['SAIR'          , 'SAIR' ],
    }

while True:

    print('\n' + '-'*80 + '\n')
    print('ESTATÍSTICAS COVID19:\n')
    for opt, país in países.items():
        if opt > 9:
            print('[ {} ] {}'.format(opt, país[0]))
        else:
            print('[ 0{} ] {}'.format(opt, país[0]))
    print()

    while True:
        
        escolha = input('Escolha uma opção: ').strip()
        if escolha.isnumeric() == True:
            escolha = int(escolha)
            if escolha >= 1 and escolha <= len(países):
                break

    país = países[escolha][1]

    if país == 'SAIR':
        print('\nPROGRAMA FINALIZADO\n')
        break

    if país == 'OUTRO':
        países_list   = []
        codigo_list = []
        print('\nDigite o código do país desejado:\n')
        sleep(2)

        for i in range(0,len(dict_covid19['records'])):
            codigo = dict_covid19['records'][i]['countryterritoryCode']
            if codigo not in codigo_list:
                países_list.append(dict_covid19['records'][i]['countriesAndTerritories'])
                codigo_list.append(dict_covid19['records'][i]['countryterritoryCode'])

        for i in range(0,len(países_list)):
            print('{} - {}'.format(países_list[i] , codigo_list[i]))
        
        print()

        while True:
            país = input('Código --> ').upper().strip()
            if país in codigo_list:
                break

    print('\n' + '-'*40 + '\n')

    if países[escolha][0] == 'OUTRO':
        indice = codigo_list.index(país)
        print(países_list[indice].upper())
        
    else:
        print(países[escolha][0].upper())

    sleep(2)

    print('\nNúmero de casos / Número de mortes')

    dias   = []
    casos  = []
    mortes = []

#   Busca de dados no dicionário do arquivo .json
    for i in range(0,len(dict_covid19['records'])):
        if dict_covid19['records'][i]['countryterritoryCode'] == país:
            dias.append(dict_covid19['records'][i]['dateRep'])
            casos.append(dict_covid19['records'][i]['cases'])
            mortes.append(dict_covid19['records'][i]['deaths'])

    n = len(dias)
    total_casos = 0
    total_mortes = 0

    for i in range(1, n+1):

        total_casos  += int(casos[-i])
        total_mortes += int(mortes[-i])

        if int(casos[-i]) > 0:
            print('\n{} - casos: {:4} '.format(dias[-i], casos[-i]), end = '')
        if int(mortes[-i]) > 0:
            print('- mortes: {}'.format(mortes[-i]), end = '')

    print()
    print('\nTotal até o dia {}: {} casos com {} mortes'
        .format(dias[0], total_casos, total_mortes))
    
    #print('\n' + '-'*40 + '\n')

    while True:
        continuar = input('\nContinuar? [S/N] ').upper().strip()
        if continuar == 'S':
            fim = None
            break
        if continuar == 'N':
            fim = True
            break
    
    if fim == True:
        print('\nPROGRAMA FINALIZADO\n')
        break
        

print('-'*80 + '\n')





