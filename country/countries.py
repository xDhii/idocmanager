## Tipos de documento do Brasil ##
import os
import sys
from config import messages

def Argentina():
    ## Mensagem inicial ##
    from country.documents import Argentina
    messages.limpar_tela()
    messages.mensageminicial()

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
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Argentina Exportation Invoice"
        # empresas_arg.select_company()
        Argentina.ARG_Exportation_Invoice_WithCUITDestino()
    if opt == "b":
        document = "Argentina Exportation Invoice"
        Argentina.ARG_Exportation_Invoice_WithoutCUITDestino()
    if opt == "c":
        document = "Argentina Local Invoice MTX CAEA"
        Argentina.ARG_Local_Invoice_MTX_CAEA()
    if opt == "d":
        document = "Argentina Local Invoice MTX"
        Argentina.ARG_Local_Invoice_MTX()
    if opt == "e":
        document = "Argentina Local Invoice MTX CAE & CAEA"
        Argentina.ARG_Local_Invoice_MTXCAECAEA()
    if opt == "f":
        document = "Argentina Local Invoice"
        Argentina.ARG_Local_Invoice()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('Argentina')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()

def Brasil():
    ## Mensagem inicial ##
    from country.documents import Brasil
    messages.limpar_tela()
    messages.mensageminicial()

    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mBRA - NFe       \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mBRA - NFSe      \033[0m')
    print()
    print('Got it. What kind of document do you want to create?')
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Brazil NFe"
        Brasil.BRA_NFE()
    if opt == "b":
        document = "Brazil NFSe"
        Brasil.BRA_NFSE()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('Brasil')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()

def Chile():
    ## Mensagem inicial ##
    from country.documents import Chile
    messages.limpar_tela()
    messages.mensageminicial()

    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mCHL - DTE                            \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mCHL - DTE DSCCItem 1000+             \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mCHL - DTE Cesion             \033[0m')
    print()
    print('Got it. What kind of document do you want to create?')
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')    opt = opt.lower()
    while opt not in ('a', 'b', 'c'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Chile DTE"
        Chile.CHL_dte()
    if opt == "b":
        document = "Chile DTE DSCCItem 1000+"
        Chile.CHL_dtedescitem1000()
    if opt == "c":
        document = "Chile DTE Cesion"
        Chile.CHL_cesion()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('Chile')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()

def Ecuador():
    ## Mensagem inicial ##
    from country.documents import Ecuador
    messages.limpar_tela()
    messages.mensageminicial()

    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mECU - Factura 01              \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mECU - Remision 06             \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mECU - Retencion 07            \033[0m')
    print()
    print('Got it. What kind of document do you want to create?')
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "ECU Factura 01"
        Ecuador.ECU_factura01()
    if opt == "b":
        document = "ECU Remision 06"
        Ecuador.ECU_remision06()
    if opt == "c":
        document = "ECU Remision 06"
        Ecuador.ECU_retencion07()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('Ecuador')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()

def Mexico():
    ## Mensagem inicial ##
    from country.documents import Mexico
    messages.limpar_tela()
    messages.mensageminicial()

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
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "México CFDI (Detallista and Addenda)"
        Mexico.MEX_cfdi_detallista_and_addenda()
    if opt == "b":
        document = "México CFDI (Comex)"
        Mexico.MEX_cfdi33_comex()
    if opt == "c":
        document = "México CFDI (Comex without Addenda)"
        Mexico.MEX_cfdi33_comex_noaddenda()
    if opt == "d":
        document = "México CFDI Standard"
        Mexico.MEX_cfdi33_standard()
    if opt == "e":
        document = "México CFDI Standard (Type E)"
        Mexico.MEX_Standard_Type_E()
    if opt == "f":
        document = "México CFDI Standard )Type P)"
        Mexico.MEX_Standard_Type_P()
    if opt == "g":
        document = "México CFDI Standard (Type T)"
        Mexico.MEX_Standard_Type_T()
    if opt == "h":
        document = "México CFDI (Standart without Addenda)"
        Mexico.MEX_cfdi33_standard_addendastep1_without_addenda()
    if opt == "i":
        document = "México CFDI (Standard with Addenda)"
        Mexico.MEX_cfdi33_standard_addendastep2addenda()
    if opt == "j":
        document = "México CFDI (Standard with Serie)"
        Mexico.MEX_cfdi33_standard_serie()
    if opt == "k":
        document = "México CFDI (Pagos)"
        Mexico.MEX_cfdi33_pagos()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('México')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()

def Peru():
    ## Mensagem inicial ##
    from country.documents import Peru
    messages.limpar_tela()
    messages.mensageminicial()

    ## Opçoes de documentos disponiveis ##
    print('Available documents: ')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mPER - 2.0 Type 1                            \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mPER - 2.0 Type 3                            \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mPER - 2.0 Type 7                            \033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mPER - 2.0 Type 8                            \033[0m')
    print('\033[1;30;47m E \033[0m - \033[4mPER - 2.0 Type 9                            \033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mPER - 2.0 Type 20                           \033[0m')
    print('\033[1;30;47m G \033[0m - \033[4mPER - 2.1 Boleta                            \033[0m')
    print('\033[1;30;47m H \033[0m - \033[4mPER - 2.1 Factura                           \033[0m')
    print('\033[1;30;47m I \033[0m - \033[4mPER - 2.1 Nota Credito                      \033[0m')
    print('\033[1;30;47m J \033[0m - \033[4mPER - 2.1 Nota Debito                       \033[0m')
    print()
    print('Got it. What kind of document do you want to create?')
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Peru 2.0 Type 1"
        Peru.PER_20type1()
    if opt == "b":
        document = "Peru 2.0 Type 3"
        Peru.PER_20type3()
    if opt == "c":
        document = "Peru 2.0 Type 7"
        Peru.PER_20type7()
    if opt == "d":
        document = "Peru 2.0 Type 8"
        Peru.PER_20type8()
    if opt == "e":
        document = "Peru 2.0 Type 9"
        Peru.PER_20type9()
    if opt == "f":
        document = "Peru 2.0 Type 20"
        Peru.PER_20type20()
    if opt == "g":
        document = "Peru 2.1 Boleta"
        Peru.PER_21boleta()
    if opt == "h":
        document = "Peru 2.1 Factura"
        Peru.PER_21factura()
    if opt == "i":
        document = "Peru 2.1 Nota Credito"
        Peru.PER_21notacredito()
    if opt == "j":
        document = "Peru 2.1 Nota Debito"
        Peru.PER_21notadebito()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('Peru')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()

def Uruguay():
    ## Mensagem inicial ##
    from country.documents import Uruguay
    messages.limpar_tela()
    messages.mensageminicial()

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
    try:
        opt = sys.argv[2]
    except IndexError:
        opt = input('Enter the letter corresponding to the document type: ')
    opt = opt.lower()
    while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
        print('\033[91m Hmm... I did not understand which document you want to generate. \033[0m')
        opt = input("Let's try again. Enter the corresponding letter: ")
        opt = opt.lower()

    if opt == "a":
        document = "Uruguay Ticket (101)"
        Uruguay.URY_101ticket()
    if opt == "b":
        document = "Uruguay Factura (111)"
        Uruguay.URY_111factura()
    if opt == "c":
        document = "Uruguay Factura Exportacion (121)"
        Uruguay.URY_121facturaexportacion()
    if opt == "d":
        document = "Uruguay Factura Nota Credito(122)"
        Uruguay.URY_122facturanotacredito()
    if opt == "e":
        document = "Uruguay Factura Nota Debito (123)"
        Uruguay.URY_123facturanotadebito()
    if opt == "f":
        document = "Uruguay Eremito Exportacion (124)"
        Uruguay.URY_124eremitoexportacion()
    if opt == "g":
        document = "Uruguay Factura (for Failure)"
        Uruguay.URY_211errorce()
    if opt == "h":
        document = "Uruguay Factura (211)"
        Uruguay.URY_211factura()

    ## Write logs for being used in the future step ##
    f = open('./bin/country.log', 'w')
    f.write('Uruguay')
    f.close()
    f = open('./bin/document.log', 'w')
    f.write(document)
    f.close()
