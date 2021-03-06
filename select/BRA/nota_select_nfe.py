## Input da Serie e Folio para NFe ## -
import os, sys
sys.path.append('../idocmanager/config')
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

serie = 7
serie = '{message:{fill}{align}{width}}'.format(
   message = (serie) ,
   fill=' ',
   align='>',
   width=3,
)

## Calcula folio + 1 ##
f = open('./select/BRA/folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1
f.close()

## Salva novo folio no TXT ##
f = open('./select/BRA/folio.txt', 'w')
f.write(str(folio))
f.close()

folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=9,
)

## Saves the generated folio to LOG ##
f = open('./bin/folio.log', 'w')
f.write(str(folio))
f.close()