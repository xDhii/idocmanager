## Input da Serie e Folio para NFe ## -
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Input da série do documento ##
serie = input('Digite a SÉRIE do documento: ')
serie = serie.upper()
while len(serie) >= 4:
    print()
    print ('\033[91mOpa! a Série do documento deve ter no maximo 3 dígitos!')
    serie = input('\033[0mDigite novamente a SÉRIE do documento com o maximo de 3 DÍGITOS: ')
    print()
serie = '{message:{fill}{align}{width}}'.format(
   message = (serie) ,
   fill=' ',
   align='>',
   width=3,
)

## Input do folio ##
folio = input('Digite o FOLIO do documento: ')
folio = folio.upper()
while len(folio) >= 10:
    print()
    print ('\033[91mOops! O número do documento deve conter no maximo 9 dígitos!')
    folio = input('\033[0mDigite novamente o FOLIO do documento com o maximo de 9 DÍGITOS: ')
    print()
folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=9,
)