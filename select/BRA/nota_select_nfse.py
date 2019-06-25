## Input da Serie, Folio e RPS para NFSe## -
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Input da série do documento ##
serie = input('Digite a SÉRIE do documento: ')
serie = serie.upper()
while len(serie) >= 6:
    print()
    print ('\033[91mOpa! a Série do documento deve ter no maximo 6 dígitos!')
    serie = input('\033[0mDigite novamente a SÉRIE do documento com o maximo de 6 DÍGITOS: ')
    print()
serie = '{message:{fill}{align}{width}}'.format(
   message = (serie) ,
   fill=' ',
   align='>',
   width=5,
)

## Input do rps do documento ##
rps = input('Digite o RPS do documento: ')
rps = rps.upper()
while len(rps) >= 16:
    print()
    print ('\033[91mOpa! O RPS do documento deve ter no maximo 15 dígitos!')
    rps = input('\033[0mDigite novamente o RPS do documento com o maximo de 15 DÍGITOS: ')
    print()
rps = '{message:{fill}{align}{width}}'.format(
   message = (rps) ,
   fill=' ',
   align='>',
   width=15,
)

## Geração do Folio ##
docnum = '{message:{fill}{align}{width}}'.format(
   message = (rps) ,
   fill=' ',
   align='>',
   width=20,
)
