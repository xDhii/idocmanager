## Tipos de documento do Uruguay ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
f = open('bin/country.log', 'w')
f.write('México')
f.close()
f = open('bin/document.log', 'w')
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents/MEX")
## Opçoes de documentos disponiveis ##
print('Available documents: ')
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
    print('Got it. What kind of document do you want to create?')
    opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

if opt == "a":
    document = "México CFDI (Detallista and Addenda)"
    import MEX_cfdi_detallista_and_addenda
if opt == "b":
    document = "México CFDI (Comex)"
    import MEX_cfdi33_comex
if opt == "c":
    document = "México CFDI (Comex without Addenda)"
    import MEX_cfdi33_comex_noaddenda
if opt == "d":
    document = "México CFDI Standard"
    import MEX_cfdi33_standard
if opt == "e":
    document = "México CFDI Standard (Type E)"
    import MEX_Standard_Type_E
if opt == "f":
    document = "México CFDI Standard )Type P)"
    import MEX_Standard_Type_P
if opt == "g":
    document = "México CFDI Standard (Type T)"
    import MEX_Standard_Type_T
if opt == "h":
    document = "México CFDI (Standart without Addenda)"
    import MEX_cfdi33_standard_addendastep1_without_addenda
if opt == "i":
    document = "México CFDI (Standard with Addenda)"
    import MEX_cfdi33_standard_addendastep2addenda
if opt == "j":
    document = "México CFDI (Standard with Serie)"
    import MEX_cfdi33_standard_serie
if opt == "k":
    document = "México CFDI (Pagos)"
    import MEX_cfdi33_pagos

f.write(document)
f.close()