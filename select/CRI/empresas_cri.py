## Selecao da Empresa ARG ##
import os
import sys
from config import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para ##
messages.empresas_cri()

## Input e seleção de empresa ##
opt = input('Enter the letter corresponding to a company: ')
opt = opt.lower()
while opt not in ('a'):
    print('\033[91mHmm... I did not understand your answer')
    opt = input('\033[0m Reenter the letter corresponding to a company: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Costa Rica (SC Johnson)"
    rut = "3101013242"
if opt == "b":
    xnome = "Costa Rica  (Kerry)"
    rut = "3101016535"


## Ajustar o tamanho da tag xnome para 25 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=25,
)
## Ajustar o tamanho da tag rut para 10 caracteres ##
rut = '{message:{fill}{align}{width}}'.format(
   message = (rut) ,
   fill=' ',
   align='>',
   width=10,
)
f = open('./bin/companycode.log', 'w')
f.write(rut)
f.close()
f = open('./bin/companyname.log', 'w')
f.write(xnome)
f.close()