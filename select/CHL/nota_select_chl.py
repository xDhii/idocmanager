## Selecao da Empresa ARG ##
import os
import sys
from config import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()


## Calcula folio + 1 ##
f = open('./select/CHL/folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1
f.close()

## Salva novo folio no TXT ##
f = open('./select/CHL/folio.txt', 'w')
f.write(str(folio))
f.close()

folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=15,
)

## Saves the generated folio to LOG ##
f = open('./bin/folio.log', 'w')
f.write(folio)
f.close()