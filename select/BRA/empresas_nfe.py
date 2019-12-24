## Selecao da Empresa NFe ##
import os, sys
from config import messages
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_nfe()

## Input e seleção de empresa ##
try:
    opt = sys.argv[3]
except IndexError:
    opt = input('Enter the letter corresponding to a company: ')
opt = opt.lower()
while opt not in ('a', 'b'):
    print('\033[91mHmm... I did not understand your answer')
    opt = input('\033[0m Reenter the letter corresponding to a company: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Invoiceware SP"
    cnpj = "24492961000129"
    xuf = "35"
if opt == "b":
    xnome = "Paperless SP"
    cnpj = "10726059000115"
    xuf = "35"

## Converter a tag 'nome' em 'xnome' e ajustar o tamanho para 115 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=60,
)
f = open('./bin/companycode.log', 'w')
f.write(cnpj)
f.close()
f = open('./bin/companyname.log', 'w')
f.write(xnome)
f.close()