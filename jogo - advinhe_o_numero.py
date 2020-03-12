from random import randint

print('\n' + '-'*80)

niveis = 3          # Quantidades de níveis do jogo
rodadas = 20        # Total de rodadas permitidas

# Variáveis incrementais
nivel = 0           # Nível atual
tentativa = None    # Tentativa atual (valor zerada no início de cada nível)
rodada = 0          # Rodada atual (valor é acumulado)

fim = False
vitoria = False

print('\nADVINHE O NÚMERO:\n')
print("- Tente advinhar o número escolido pelo computador.")
print(f"- Complete todos os {niveis} níveis em {rodadas} tentativas.")
print("- Digite 'sair' a qualquer momento para sair do jogo.")

# Laço de repetição para controlar os diferentes níveis do jogo
while fim == False:
    nivel += 1          # nível 1, 2, 3, 4...
    limite = 10**nivel  # 10, 100, 1000, 10000...
    numero = randint(0 , limite)    # Número sorteado pelo computador 
    tentativa = 0 
    print('\n\n' + '-'*40)
    print(f'\n|||||||||| NÍVEL {nivel} ||||||||||\n')

    # Laço de repetição para controlar as tentativas de cada nível
    while True:
        tentativa += 1
        rodada += 1
        restantes = rodadas - rodada
        validacao = False

        if rodada == rodadas:           # Última rodada    --> ''
            print(f'\nNÍVEL {nivel} - Rodada {rodada}')

        elif rodada == rodadas - 1:     # Penúltima rodada --> '1 restante'
            print(f'\nNÍVEL {nivel} - Rodada {rodada} [{restantes} restante]')

        else:                           # Demais rodadas   --> 'x restanteS'
            print(f'\nNÍVEL {nivel} - Rodada {rodada} [{restantes} restantes]')

        # Laço de repetição para validação do valor digitado pelo usuário
        while validacao == False:

            if rodada == rodadas:
                tentativa_str = 'ÚLTIMA TENTATIVA'
            else:
                tentativa_str = f'Tentativa {tentativa}'

            palpite = input(f'{tentativa_str}: ' +
                f'Digite um número inteiro entre 0 e {limite}: ')

            # Verificando se o usuário deseja sair do jogo
            if palpite.lower().strip() == 'sair':
                fim = True
                break
            
            # Verificando se o valor digitado é numérico
            if palpite.isnumeric() == True:
                palpite = int(palpite)

                # Verificando se o valor digitado está dentro dos limites
                if palpite in range(0 , limite + 1):
                    validacao = True
        
        print('\n' + '-'*40)

        # Saída do jogo por opção do usuário
        if fim == True:
            break
        
        # Acerto do número
        if palpite == numero:
            print('\nACERTOU! O número escolhido foi o {}.'
                .format(numero))

            # Condição para acerto + término de todos os níveis        
            if nivel == niveis:
                vitoria = True
            else:
                print('\nVocê avançou para o próximo nível.')

            break
                
        # Término do jogo
        if rodada == rodadas:
            fim = True
            break

        # Erro do número + Dica
        if palpite < numero:
            print('\nDigite um número MAIOR')
        else:
            print('\nDigite um número MENOR')

    # Término do jogo

    if palpite == '0':      # por opção do usuário
        print('\nJogo interrompido pelo usuáro.\n')

    elif vitoria == True:   # pelo usuário ter avançado todos os níveis
        print(f'\nParabéns! Você completou todos os {niveis} níveis ' +
            f'em {rodada} tentativas.\n')
        fim = True

    elif fim == True:       # por término das rodadas

        print(f'\nFIM DE JOGO! O número sorteado foi o {numero}!\n')

    print('-'*80 + '\n')


