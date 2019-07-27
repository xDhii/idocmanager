## Input da Serie, Folio e RPS para NFSe## -
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

serie = 7
serie = '{message:{fill}{align}{width}}'.format(
   message = (serie) ,
   fill=' ',
   align='>',
   width=5,
)

## Calcula folio + 1 ##
f = open('./select/BRA/rps.txt', 'r+')
rps = f.read()
rps = int(rps) + 1
f.close()

## Salva novo folio no TXT ##
f = open('./select/BRA/rps.txt', 'w')
f.write(rps)
f.close()

rps = '{message:{fill}{align}{width}}'.format(
   message = (rps) ,
   fill='0',
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

## Saves the generated folio to LOG ##
f = open('./bin/folio.log', 'w')
f.write(rps)
f.close()