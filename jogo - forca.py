from random import choice

palavras = [
# 'Acrotíri e Deceleia' ,
'Afeganistão' ,
'África do Sul' ,
# 'Akrotiri' ,
'Albânia' ,
'Alemanha' ,
'Andorra' ,
'Angola' ,
# 'Anguila' ,
'Antígua e Barbuda' ,
'Arábia Saudita' ,
'Argélia' ,
'Argentina' ,
'Armênia' ,
'Aruba' ,
'Austrália' ,
'Áustria' ,
'Azerbaijão' ,
'Bahamas' ,
'Bangladesh' ,
'Barbados' ,
'Barém' ,
'Bélgica' ,
'Belize' ,
'Benim' ,
'Bermudas' ,
'Bielorrússia' ,
'Birmânia' ,
'Bolívia' ,
'Bósnia e Herzegovina' ,
'Botsuana' ,
'Brasil' ,
'Brunei' ,
'Bulgária' ,
'Burquina Faso' ,
'Burúndi' ,
'Butão' ,
'Cabo Verde' ,
'Camarões' ,
'Camboja' ,
'Canadá' ,
'Catar' ,
'Cazaquistão' ,
'Chade' ,
'Chile' ,
'China' ,
'Chipre' ,
'Cisjordânia' ,
'Colômbia' ,
'Comores' ,
'Congo' ,
'Coreia do Norte' ,
'Coreia do Sul' ,
'Costa do Marfim' ,
'Costa Rica' ,
'Croácia' ,
'Cuba' ,
'Curaçao' ,
'Dinamarca' ,
'Djibuti' ,
'Domínica' ,
'Egito' ,
'El Salvador' ,
'Emiratos Árabes Unidos' ,
'Equador' ,
'Eritreia' ,
'Eslováquia' ,
'Eslovênia' ,
'Espanha' ,
'Estados Unidos' ,
'Estônia' ,
'Etiópia' ,
'Fiji' ,
'Filipinas' ,
'Finlândia' ,
'França' ,
'Gabão' ,
'Gâmbia' ,
'Gana' ,
'Faixa de Gaza' ,
'Geórgia' ,
'Geórgia do Sul' ,
'Gibraltar' ,
'Granada' ,
'Grécia' ,
'Groenlândia' ,
'Guam' ,
'Guatemala' ,
# 'Guernsey' ,
'Guiana' ,
'Guiné' ,
'Guiné Equatorial' ,
'Guiné Bissau' ,
'Haiti' ,
'Honduras' ,
'Hong Kong' ,
'Hungria' ,
'Iêmen' ,
# 'Ilha Bouvet' ,
# 'Ilha de Navassa' ,
# 'Ilha do Natal' ,
# 'Ilha Norfolk' ,
# 'Ilhas Ashmore e Cartier' ,
'Ilhas Caiman' ,
'Ilhas Cook' ,
# 'Ilhas de Clipperton' ,
# 'Ilhas do Mar de Coral ,
# 'Ilhas dos Cocos' ,
# 'Ilhas Falkland' ,
# 'Ilhas Faroé' ,
# 'Ilhas Heard e McDonald' ,
'Ilhas Marshall' ,
'Ilhas Maurício' ,
# 'Ilhas Paracel' ,
# 'Ilhas Pitcairn' ,
'Ilhas Salomão' ,
# 'Ilhas Spratly' ,
# 'Ilhas Turcas e Caicos' ,
'Ilhas Virgens Americanas' ,
'Ilhas Virgens Britânicas' ,
'Índia' ,
'Indonésia' ,
'Irã' ,
'Iraque' ,
'Irlanda' ,
'Islândia' ,
'Israel' ,
'Itália' ,
'Jamaica' ,
# 'Jan Mayen' ,
'Japão' ,
# 'Jersey' ,
'Jordânia' ,
'Kosovo' ,
'Kuwait' ,
'Laos' ,
'Lesoto' ,
'Letônia' ,
'Líbano' ,
'Libéria' ,
'Líbia' ,
# 'Listenstaine' ,
'Lituânia' ,
'Luxemburgo' ,
'Macau' ,
'Macedônia' ,
'Madagascar' ,
'Malásia' ,
'Malawi' ,
'Maldivas' ,
'Mali' ,
'Malta' ,
# 'Marianas do Norte' ,
'Marrocos' ,
'Mauritânia' ,
'México' ,
'Micronésia' ,
'Moçambique' ,
'Moldávia' ,
'Mônaco' ,
'Mongólia' ,
# 'Montserrat' ,
'Montenegro' ,
'Namíbia' ,
# 'Nauru' ,
'Nepal' ,
'Nicarágua' ,
'Níger' ,
'Nigéria' ,
# 'Niue' ,
'Noruega' ,
'Nova Caledónia' ,
'Nova Zelândia' ,
'Omã' ,
'Países Baixos' ,
'Palau' ,
'Panamá' ,
'Papua Nova Guiné' ,
'Paquistão' ,
'Paraguai' ,
'Peru' ,
'Polinésia Francesa' ,
'Polónia' ,
'Porto Rico' ,
'Portugal' ,
'Quênia' ,
'Quirguizistão' ,
# 'Quiribáti' ,
'Reino Unido' ,
'República Centro-Africana' ,
# 'República Democrática do Congo' ,
'República Dominicana' ,
'República Tcheca' ,
'Romênia' ,
'Ruanda' ,
'Rússia' ,
'Samoa' ,
'Samoa Americana' ,
# 'Santa Helena' ,
# 'Santa Lúcia' ,
# 'São Bartolomeu' ,
# 'São Cristóvão e Neves' ,
# 'São Marinho' ,
# 'São Martinho' ,
# 'São Pedro e Miquelon' ,
'São Tomé e Príncipe' ,
'São Vicente e Granadinas' ,
'Saara Ocidental' ,
'Seicheles' ,
'Senegal' ,
'Serra Leoa' ,
'Sérvia' ,
'Singapura' ,
'Síria' ,
'Somália' ,
'Sri Lanka' ,
'Suazilândia' ,
'Sudão' ,
'Sudão do Sul' ,
'Suécia' ,
'Suíça' ,
'Suriname' ,
# 'Svalbard e Jan Mayen' ,
'Tailândia' ,
'Taiwan' ,
'Tajiquistão' ,
'Tanzânia' ,
# 'Território Britânico do Oceano Índico' ,
# 'Territórios Austrais Franceses' ,
'Timor Leste' ,
'Togo' ,
# 'Tokelau' ,
'Tonga' ,
'Trindade e Tobago' ,
'Tunísia' ,
'Turquemenistão' ,
'Turquia' ,
'Tuvalu' ,
'Ucrânia' ,
'Uganda' ,
'Uruguai' ,
'Usbequistão' ,
# 'Vanuatu' ,
'Vaticano' ,
'Venezuela' ,
'Vietname' ,
# 'Wake Island' ,
# 'Wallis e Futuna' ,
'Zâmbia' ,
'Zimbabuê' ,
]

acentos_minusculas = [
['a' , 'á' , 'â' , 'à' , 'å' , 'ã' , 'ä'] ,
['e' , 'é' , 'ê' , 'è' , 'ë'] ,
['i' , 'í' , 'î' , 'ì' , 'ï'] ,
['o' , 'ó' , 'ô' , 'ò' , 'ø' , 'õ' , 'ö'] ,
['u' , 'ú' , 'û' , 'ù' , 'ü'] ,
['c' , 'ç'] ,
['n' , 'ñ'] ,
['y' , 'ý'] ]

acentos_maiusculas = [
['A' , 'Á' , 'Â' , 'À' , 'Å' , 'Ã' , 'Ä'] ,
['E' , 'É' , 'Ê' , 'È' , 'Ë'] ,
['I' , 'Í' , 'Î' , 'Ì' , 'Ï'] ,
['O' , 'Ó' , 'Ô' , 'Ò' , 'Ø' , 'Õ' , 'Ö'] ,
['U' , 'Ú' , 'Û' , 'Ù' , 'Ü'] ,
['C' , 'Ç'] ,
['N' , 'Ñ'] ,
['Y' , 'Ý'] ]


palavra = choice(palavras).upper()
palavra_list = []

for i in range(0 , len(palavra)):
    letra = palavra[i]
    num = len(acentos_maiusculas)    
    for j in range (0 , num):
        if letra in acentos_maiusculas[j][1:num]:
            letra = letra.replace(letra, acentos_maiusculas[j][0])
        else:
            letra = letra
    palavra_list.append(letra)

palavra_oculta = []
for i in range(0,len(palavra_list)):
    palavra_oculta.append('__')

erros = 0
tentativa = 0
palavra = list(palavra)

while erros < 6:
    print('\n\n{}\n'.format('  '.join(palavra_oculta)))
    tentativa += 1
    palpite = input('Digite uma letra: ').upper()
    if palpite in palavra_list:
        for j in range(0, len(palavra_list)):
            if palpite == palavra_list[j]:
                palavra_oculta[j] = palavra[j]
    else:
        erros += 1
    if palavra_oculta == palavra:
        break
    if erros > 0:
        print(f'Erros: {erros}\n')


print('\n\n{}\n'.format('  '.join(list(palavra))))

