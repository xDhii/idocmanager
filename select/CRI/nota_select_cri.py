## Selecao da Empresa ARG ##
import os
import sys
from config import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()


## Calcula folio + 1 ##
f = open('./select/CRI/folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1
f.close()

## Salva novo folio no TXT ##
f = open('./select/CRI/folio.txt', 'w')
print(folio, file=f)
f.close()

folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=15,
)

## Saves the generated folio to LOG ##
f = open('./bin/folio.log', 'w')
print(folio, file=f)
f.close()