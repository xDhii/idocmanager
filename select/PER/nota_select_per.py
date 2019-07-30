## Input da Serie e Folio para PER ## -
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()


## Calcula folio + 1 ##
f = open('./select/PER/folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1
f.close()

## Salva novo folio no TXT ##
f = open('./select/PER/folio.txt', 'w')
f.write(folio)
f.close()

folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=8,
)

## Saves the generated folio to LOG ##
f = open('./bin/folio.log', 'w')
f.write(folio)
f.close()