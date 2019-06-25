## Input da Serie e Folio para URY ## -
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Input do folio ##
folio = input('Digite o FOLIO do documento: ')
folio = folio.upper()
while len(folio) >= 16:
    print()
    print ('\033[91mOops! O número do documento deve conter no maximo 15 dígitos!')
    folio = input('\033[0mDigite novamente o FOLIO do documento com o maximo de 15 DÍGITOS: ')
    print()
folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=15,
)