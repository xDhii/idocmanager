## Tipos de documento do Brasil ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents/ARG")
## Opçoes de documentos disponiveis ##
print('Documentos disponíveis: ')
print()
print('\033[1;30;47m A \033[0m - \033[4mARG - Exportation Invoice (With CUIT Destino)\033[0m')
print('\033[1;30;47m B \033[0m - \033[4mARG - Exportation Invoice (Without CUIT Destino)\033[0m')
print('\033[1;30;47m C \033[0m - \033[4mARG - Local Invoice MTX CAEA\033[0m')
print('\033[1;30;47m D \033[0m - \033[4mARG - Local Invoice MTX\033[0m')
print('\033[1;30;47m E \033[0m - \033[4mAARG - Local Invoice MTX CAE & CAEA\033[0m')
print('\033[1;30;47m F \033[0m - \033[4mARG - Local Invoice\033[0m')

print()
print('Entendido. Qual tipo de documento você deseja criar?')
opt = input('Digite a letra correspondente ao tipo de documento: ')
opt = opt.lower()
while opt not in ('a', 'b'):
    print('\033[91mHmm... Não entendi qual o documento voce quer gerar')
    opt = input('\033[0mVamos tentar novamente. Digite a letra correspondente ao tipo de documento: ')
    opt = opt.lower()

if opt == "a":
    import ARG_Exportation_Invoice_WithCUITDestino
if opt == "b":
    import ARG_Exportation_Invoice_WithoutCUITDestino
if opt == "c":
    import ARG_Local_Invoice_MTX_CAEA
if opt == "d":
    import ARG_Local_Invoice_MTX
if opt == "e":
    import ARG_Local_Invoice_MTXCAECAEA
if opt == "f":
    import ARG_Local_Invoice
