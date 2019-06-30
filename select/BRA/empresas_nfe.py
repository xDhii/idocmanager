## Selecao da Empresa NFe ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_nfe()

## Input e seleção de empresa ##
opt = input('Digite a letra correspondente a empresa: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'):
    print('\033[91mHmm... Não entendi sua resposta')
    opt = input('\033[0mDigite novamente a letra correspondente a empresa: ')
    opt = opt.lower()
if opt == "a":
    xnome = "Invoiceware SP"
    cnpj = "24492961000129"
    xuf = "35"
if opt == "b":
    xnome = "Axalta Coating Systems RS"
    cnpj = "15373395001036"
    xuf = "43"
if opt == "c":
    xnome = "Paperless SP"
    cnpj = "10726059000115"
    xuf = "35"
if opt == "d":
    xnome = "Brow Forman SC"
    cnpj = "00305765000210"
    xuf = "42"
if opt == "e":
    xnome = "Signify Iluminação MG"
    cnpj = "22555787000352"
    xuf = "31"
if opt == "f":
    xnome = "Infoglobo RJ"
    cnpj = "04067191000755"
    xuf = "33"
if opt == "g":
    xnome = "EMS GERMED SP"
    cnpj = "57507378000365"
    xuf = "35"
if opt == "h":
    xnome = "Edwards BR NFM SP"
    cnpj = "05944604000533"
    xuf = "35"
if opt == "i":
    xnome = "Orica BR PA"
    cnpj = "31056708001917"
    xuf = "15"
if opt == "j":
    xnome = "Comp. de Dist. MS"
    cnpj = "11517841003455"
    xuf = "50"
if opt == "k":
    xnome = "Philips Medical SP"
    cnpj = "58295213000178"
    xuf = "35"
if opt == "l":
    xnome = "Philips Medical MG"
    cnpj = "58295213002111"
    xuf = "31"
if opt == "m":
    xnome = "Biomerieux RJ"
    cnpj = "33040635000171"
    xuf = "33"
if opt == "n":
    xnome = "Sabo Autopeças SP"
    cnpj = "60860681001323"
    xuf = "35"

## Converter a tag 'nome' em 'xnome' e ajustar o tamanho para 115 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=60,
)
