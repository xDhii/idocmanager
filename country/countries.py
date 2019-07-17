## Tipos de documento do Brasil ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
def Argentina():
    ## Mensagem inicial ##
    messages.limpar_tela()
    messages.mensageminicial()
    ## Voltar para a pasta de documentos do Brasil ##
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents")
    import documents
    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mARG - Exportation Invoice (With CUIT Destino)\033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mARG - Exportation Invoice (Without CUIT Destino)\033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mARG - Local Invoice MTX CAEA\033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mARG - Local Invoice MTX\033[0m')
    print('\033[1;30;47m E \033[0m - \033[4mARG - Local Invoice MTX CAE & CAEA\033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mARG - Local Invoice\033[0m')

    print()
    print("Got it. What kind of document do you want to create?")
    opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Argentina Exportation Invoice"
        documents.ARG_Exportation_Invoice_WithCUITDestino()
    if opt == "b":
        document = "Argentina Exportation Invoice"
        documents.ARG_Exportation_Invoice_WithoutCUITDestino()
    if opt == "c":
        document = "Argentina Local Invoice MTX CAEA"
        documents.ARG_Local_Invoice_MTX_CAEA()
    if opt == "d":
        document = "Argentina Local Invoice MTX"
        documents.ARG_Local_Invoice_MTX()
    if opt == "e":
        document = "Argentina Local Invoice MTX CAE & CAEA"
        documents.ARG_Local_Invoice_MTXCAECAEA()
    if opt == "f":
        document = "Argentina Local Invoice"
        documents.ARG_Local_Invoice()
    ## Write logs for being used in the future stepd ##
    f = open('bin/country.log', 'w')
    f.write('Argentina')
    f.close()
    f = open('bin/document.log', 'w')
    f.write(document)
    f.close()
def Brasil():
    ## Mensagem inicial ##
    messages.limpar_tela()
    messages.mensageminicial()
    ## Voltar para a pasta de documentos do Brasil ##
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents")
    import documents
    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mBRA - NFe       \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mBRA - NFSe      \033[0m')

    print()
    print('Got it. What kind of document do you want to create?')
    opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Brazil NFe"
        documents.BRA_NFE()
    if opt == "b":
        document = "Brazil NFSe"
        documents.BRA_NFSE()
    f = open('bin/country.log', 'w')
    f.write('Brasil')
    f.close()
    f = open('bin/document.log', 'w')
    f.write(document)
    f.close()
def Mexico():
    ## Mensagem inicial ##
    messages.limpar_tela()
    messages.mensageminicial()
    ## Voltar para a pasta de documentos ##
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents")
    import documents
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
        documents.MEX_cfdi_detallista_and_addenda()
    if opt == "b":
        document = "México CFDI (Comex)"
        documents.MEX_cfdi33_comex()
    if opt == "c":
        document = "México CFDI (Comex without Addenda)"
        documents.MEX_cfdi33_comex_noaddenda()
    if opt == "d":
        document = "México CFDI Standard"
        documents.MEX_cfdi33_standard()
    if opt == "e":
        document = "México CFDI Standard (Type E)"
        documents.MEX_Standard_Type_E()
    if opt == "f":
        document = "México CFDI Standard )Type P)"
        documents.MEX_Standard_Type_P()
    if opt == "g":
        document = "México CFDI Standard (Type T)"
        documents.MEX_Standard_Type_T()
    if opt == "h":
        document = "México CFDI (Standart without Addenda)"
        documents.MEX_cfdi33_standard_addendastep1_without_addenda()
    if opt == "i":
        document = "México CFDI (Standard with Addenda)"
        documents.MEX_cfdi33_standard_addendastep2addenda()
    if opt == "j":
        document = "México CFDI (Standard with Serie)"
        documents.MEX_cfdi33_standard_serie()
    if opt == "k":
        document = "México CFDI (Pagos)"
        documents.MEX_cfdi33_pagos()
    f = open('bin/country.log', 'w')
    f.write('México')
    f.close()
    f = open('bin/document.log', 'w')
    f.write(document)
    f.close()
def Uruguay():
    ## Mensagem inicial ##
    messages.limpar_tela()
    messages.mensageminicial()
    ## Voltar para a pasta de documentos do Brasil ##
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents")
    import documents
    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mURY - 101 Ticket                            \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mURY - 111 Factura                           \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mURY - 121 Factura Exportación               \033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mURY - 122 Factura Nota Crédito Exportación  \033[0m')
    print('\033[1;30;47m E \033[0m - \033[4mURY - 123 Factura Nota Débito Exportación   \033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mURY - 124 eRemito Exportación               \033[0m')
    print('\033[1;30;47m G \033[0m - \033[4mURY - 211 Factura (for failure)              \033[0m')
    print('\033[1;30;47m H \033[0m - \033[4mURY - 211 Factura                            \033[0m')

    print()
    print('Got it. What kind of document do you want to create?')
    opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Uruguay Ticket (101)"
        documents.URY_101ticket()
    if opt == "b":
        document = "Uruguay Factura (111)"
        documents.URY_111factura()
    if opt == "c":
        document = "Uruguay Factura Exportacion (121)"
        documents.URY_121facturaexportacion()
    if opt == "d":
        document = "Uruguay Factura Nota Credito(122)"
        documents.URY_122facturanotacredito()
    if opt == "e":
        document = "Uruguay Factura Nota Debito (123)"
        documents.URY_123facturanotadebito()
    if opt == "f":
        document = "Uruguay Eremito Exportacion (124)"
        documents.URY_124eremitoexportacion()
    if opt == "g":
        document = "Uruguay Factura (for Failure)"
        documents.URY_211errorce()
    if opt == "h":
        document = "Uruguay Factura (211)"
        documents.URY_211factura()
    f = open('bin/country.log', 'w')
    f.write('Uruguay')
    f.close()
    f = open('bin/document.log', 'w')
    f.write(document)
    f.close()