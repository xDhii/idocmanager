## Selecao da Empresa URY ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()

## Opçoes de empresas cadastradas para NFe ##
messages.empresas_ury()

## Input e seleção de empresa ##
opt = input('Digite a letra correspondente a empresa: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c'):
    print('\033[91mHmm... Não entendi sua resposta')
    opt = input('\033[0mDigite novamente a letra correspondente a empresa: ')
    opt = opt.lower()    
if opt == "a":
    xnome = "Sovos Uruguay (McCain) [121, 122, 123, 124]"
    rut = "080003530017"
if opt == "b":
    xnome = "DSM"
    rut = "214580250019"
if opt == "c":
    xnome = "Sovos Uruguay (SC Johnson) [101, 111]"
    rut = "213408960013"

## Ajustar o tamanho da tag xnome para 255 caracteres ##
xnome = '{message:{fill}{align}{width}}'.format(
   message = (xnome) ,
   fill=' ',
   align='<',
   width=255,
)
## Ajustar o tamanho da tag RUT para 115 caracteres ##
rut = '{message:{fill}{align}{width}}'.format(
   message = (rut) ,
   fill=' ',
   align='<',
   width=30,
)

