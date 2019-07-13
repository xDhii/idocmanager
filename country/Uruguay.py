## Tipos de documento do Uruguay ##
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/config")
import messages
f = open('bin/country.log', 'w')
f.write('Uruguay')
f.close()
f = open('bin/document.log', 'w')
## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents/URY")
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
    import URY_101ticket
if opt == "b":
    document = "Uruguay Factura (111)"
    import URY_111factura
if opt == "c":
    document = "Uruguay Factura Exportacion (121)"
    import URY_121facturaexportacion
if opt == "d":
    document = "Uruguay Factura Nota Credito(122)"
    import URY_122facturanotacredito
if opt == "e":
    document = "Uruguay Factura Nota Debito (123)"
    import URY_123facturanotadebito
if opt == "f":
    document = "Uruguay Eremito Exportacion (124)"
    import URY_124eremitoexportacion
if opt == "g":
    document = "Uruguay Factura (for Failure)"
    import URY_211errorce
if opt == "h":
    document = "Uruguay Factura (211)"
    import URY_211factura

f.write(document)
f.close()