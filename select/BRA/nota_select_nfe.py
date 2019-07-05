## Input da Serie e Folio para NFe ## -
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
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

## Calcula folio + 1 ##
f = open('folio.txt', 'r+')
folio = f.read()
folio = int(folio) + 1
f.close()

## Salva novo folio no TXT ##
f = open('folio.txt', 'w')
print(folio, file=f)
f.close()

folio = '{message:{fill}{align}{width}}'.format(
   message = (folio) ,
   fill='0',
   align='>',
   width=9,
)
