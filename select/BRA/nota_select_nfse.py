## Input da Serie, Folio e RPS para NFSe## -
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Input da série do documento ##
# serie = input('Digite a SÉRIE do documento: ')
# serie = serie.upper()
# while len(serie) >= 6:
#     print()
#     print ('\033[91mOpa! a Série do documento deve ter no maximo 6 dígitos!')
#     serie = input('\033[0mDigite novamente a SÉRIE do documento com o maximo de 6 DÍGITOS: ')
#     print()
serie = 7
serie = '{message:{fill}{align}{width}}'.format(
   message = (serie) ,
   fill=' ',
   align='>',
   width=5,
)

## Calcula folio + 1 ##
f = open('select/BRA/rps.txt', 'r+')
rps = f.read()
rps = int(rps) + 1
f.close()

## Salva novo folio no TXT ##
f = open('select/BRA/rps.txt', 'w')
print(rps, file=f)
f.close()

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
