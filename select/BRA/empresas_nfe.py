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
while opt not in ('a', 'b'):
    print('\033[91mHmm... Não entendi sua resposta')
    opt = input('\033[0mDigite novamente a letra correspondente a empresa: ')
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
