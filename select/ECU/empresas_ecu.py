## Selecao da Empresa ARG ##
import os
import sys
from config import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_ecu()

## Input e seleção de empresa ##
opt = input('Enter the letter corresponding to a company: ')
opt = opt.lower()
while opt not in ('a'):
    print('\033[91mHmm... I did not understand your answer')
    opt = input('\033[0m Reenter the letter corresponding to a company: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Ecuador (Zoetis)"
    rut = "1792391091001"

## Ajustar o tamanho da tag xnome para 255 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=255,
)
## Ajustar o tamanho da tag rut para 30 caracteres ##
rut = '{message:{fill}{align}{width}}'.format(
   message = (rut) ,
   fill=' ',
   align='<',
   width=30,
)
f = open('./bin/companycode.log', 'w')
f.write(rut)
f.close()
f = open('./bin/companyname.log', 'w')
f.write(xnome)
f.close()