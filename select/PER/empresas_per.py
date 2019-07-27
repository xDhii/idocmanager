## Selecao da Empresa URY ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_per()

## Input e seleção de empresa ##
opt = input('Enter the letter corresponding to a company: ')
opt = opt.lower()
while opt not in ('a'):
    print('\033[91mHmm... I did not understand your answer')
    opt = input('\033[0m Reenter the letter corresponding to a company: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Coca-Cola Peru"
    rut = "20415932376"

rut11 = rut
## Ajustar o tamanho da tag xnome para 255 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=128,
)
## Ajustar o tamanho da tag rut para 30 caracteres ##
rut = '{message:{fill}{align}{width}}'.format(
   message = (rut) ,
   fill=' ',
   align='<',
   width=30,
)
f = open('bin/companycode.log', 'w')
f.write(rut)
f.close()
f = open('bin/companyname.log', 'w')
f.write(xnome)
f.close()