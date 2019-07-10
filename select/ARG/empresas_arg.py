## Selecao da Empresa URY ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_arg()

## Input e seleção de empresa ##
opt = input('Digite a letra correspondente a empresa: ')
opt = opt.lower()
while opt not in ('a', 'b'):
    print('\033[91mHmm... Não entendi sua resposta')
    opt = input('\033[0mDigite novamente a letra correspondente a empresa: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Sovos Argentina (Rockwell)"
    cuit = "30681463999"
if opt == "b":
    xnome = "Sovos Argentina (Philips) - Local MTX"
    cuit = "30503747533"


## Ajustar o tamanho da tag xnome para 255 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=200,
)
## Ajustar o tamanho da tag cuit para 115 caracteres ##
cuit = '{message:{fill}{align}{width}}'.format(
   message = (cuit) ,
   fill=' ',
   align='<',
   width=11,
)

