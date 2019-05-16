## Tipos de documento do Uruguay ##
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents/MEX")
## Opçoes de documentos disponiveis ##
print('Documentos disponíveis: ')
print()
print('\033[1;30;47m A \033[0m - \033[4mMEX - CDFI Detallist e Addenda              \033[0m')
print('\033[1;30;47m B \033[0m - \033[4mMEX - CFDI 33 Comex                         \033[0m')
print('\033[1;30;47m C \033[0m - \033[4mMEX - CFDI 33 Comex no Addenda              \033[0m')
print('\033[1;30;47m D \033[0m - \033[4mMEX - CFDI 33 Standard                      \033[0m')
print('\033[1;30;47m E \033[0m - \033[4mMEX - CFDI 33 Standard Type E               \033[0m')
print('\033[1;30;47m F \033[0m - \033[4mMEX - CFDI 33 Standard Type P               \033[0m')
print('\033[1;30;47m G \033[0m - \033[4mMEX - CFDI 33 Standard Type T               \033[0m')
print('\033[1;30;47m H \033[0m - \033[4mMEX - CFDI 33 Standard Addenda Only Step 1  \033[0m')
print('\033[1;30;47m I \033[0m - \033[4mMEX - CFDI 33 Standard Addenda Only Step 2  \033[0m')
print('\033[1;30;47m J \033[0m - \033[4mMEX - CFDI 33 Standard com Série            \033[0m')
print('\033[1;30;47m K \033[0m - \033[4mMEX - CFDI Pagos                            \033[0m')

print()
print('Entendido. Qual tipo de documento você deseja criar?')
opt = input('Digite a letra correspondente ao tipo de documento: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'):
    print('\033[91mHmm... Não entendi qual o documento voce quer gerar')
    opt = input('\033[0mVamos tentar novamente. Digite a letra correspondente ao tipo de documento: ')
    opt = opt.lower()

if opt == "a":
    import MEX_cfdi_detallista_and_addenda
if opt == "b":
    import MEX_cfdi33_comex
if opt == "c":
    import MEX_cfdi33_comex_noaddenda
if opt == "d":
    import MEX_cfdi33_standard
if opt == "e":
    import MEX_Standard_Type_E
if opt == "f":
    import MEX_Standard_Type_P
if opt == "g":
    import MEX_Standard_Type_T
if opt == "h":
    import MEX_cfdi33_standard_addendastep1_without_addenda
if opt == "i":
    import MEX_cfdi33_standard_addendastep2addenda
if opt == "j":
    import MEX_cfdi33_standard_serie
if opt == "k":
    import MEX_cfdi33_pagos