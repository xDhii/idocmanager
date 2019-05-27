## Selecao da Empresa URY ##
import os, sys
sys.path.insert(0, './config')
import messages

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
<<<<<<< HEAD
    rfc = "CME940118F7A"
=======
    cuit = "CME940118F7A"
if opt == "b":
    xnome = "WeWork - MX - QA"
    cuit = "ALA151026V8A"
if opt == "c":
    xnome = "WeWork - MX - QA"
    cuit = "AMA1602043C6"
if opt == "d":
    xnome = "WeWork - MX - QA"
    cuit = "VTS160204M62"
if opt == "e":
    xnome = "INVOICEWARE - MX"
    cuit = "BTM060817960"
if opt == "f":
    xnome = "Mexico CANCELLATION - CFDI"
    cuit = "LAN8507268IA"
if opt == "g":
    xnome = "Mexico CANCELLATION - CFDI"
    cuit = "MAG041126GT8"

>>>>>>> 86aef1b628941cc5a1849c35dd1d6944335218d5

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
