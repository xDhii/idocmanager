## Selecao da Empresa URY ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
f = open('bin/companycode.log', 'w')
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_mex()

## Input e seleção de empresa ##
opt = input('Digite a letra correspondente a empresa: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g'):
    print('\033[91mHmm... Não entendi sua resposta')
    opt = input('\033[0mDigite novamente a letra correspondente a empresa: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Sovos Mexico Inbound (CHEP)"
    rfc = "CME940118F7A"
if opt == "b":
    xnome = "WeWork - MX - QA"
    rfc = "ALA151026V8A"
if opt == "c":
    xnome = "WeWork - MX - QA"
    rfc = "AMA1602043C6"
if opt == "d":
    xnome = "WeWork - MX - QA"
    rfc = "VTS160204M62"
if opt == "e":
    xnome = "INVOICEWARE - MX"
    rfc = "BTM060817960"
if opt == "f":
    xnome = "Mexico CANCELLATION - CFDI"
    rfc = "LAN8507268IA"
if opt == "g":
    xnome = "Mexico CANCELLATION - CFDI"
    rfc = "MAG041126GT8"


## Ajustar o tamanho da tag xnome para 255 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=128,
)
## Ajustar o tamanho da tag rfc para 115 caracteres ##
rfc = '{message:{fill}{align}{width}}'.format(
   message = (rfc) ,
   fill=' ',
   align='<',
   width=20,
)

f.write(rfc + xnome)
f.close()