## Selecao da Empresa ARG ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_arg()

## Input e seleção de empresa ##
opt = input('Enter the letter corresponding to a company: ')
opt = opt.lower()
while opt not in ('a', 'b'):
    print('\033[91mHmm... I did not understand your answer')
    opt = input('\033[0m Reenter the letter corresponding to a company: ')
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
f = open('./bin/companycode.log', 'w')
f.write(cuit)
f.close()
f = open('./bin/companyname.log', 'w')
f.write(xnome)
f.close()