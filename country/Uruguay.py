## Tipos de documento do Uruguay ##
import os, sys
sys.path.insert(0, './config')
import messages

## Mensagem inicial ##
messages.limpar_tela()
messages.mensageminicial()
## Voltar para a pasta de documentos do Brasil ##
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/country/documents/URY")
## Opçoes de documentos disponiveis ##
print('Documentos disponíveis: ')
print()
print('\033[1;30;47m A \033[0m - \033[4mURY - 101 Ticket                            \033[0m')
print('\033[1;30;47m B \033[0m - \033[4mURY - 111 Factura                           \033[0m')
print('\033[1;30;47m C \033[0m - \033[4mURY - 121 Factura Exportación               \033[0m')
print('\033[1;30;47m D \033[0m - \033[4mURY - 122 Factura Nota Crédito Exportación  \033[0m')
print('\033[1;30;47m E \033[0m - \033[4mURY - 123 Factura Nota Débito Exportación   \033[0m')
print('\033[1;30;47m F \033[0m - \033[4mURY - 124 eRemito Exportación               \033[0m')
print('\033[1;30;47m G \033[0m - \033[4mURY - 211 ErrorCE                           \033[0m')
print('\033[1;30;47m H \033[0m - \033[4mURY - 211 Factura                           \033[0m')

print()
print('Entendido. Qual tipo de documento você deseja criar?')
opt = input('Digite a letra correspondente ao tipo de documento: ')
opt = opt.lower()
while opt not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'):
    print('\033[91mHmm... Não entendi qual o documento voce quer gerar')
    opt = input('\033[0mVamos tentar novamente. Digite a letra correspondente ao tipo de documento: ')
    opt = opt.lower()

if opt == "a":
    import URY_101ticket
if opt == "b":
    import URY_111factura
if opt == "c":
    import URY_121facturaexportacion
if opt == "d":
    import URY_122facturanotacredito
if opt == "e":
    import URY_123facturanotadebito
if opt == "f":
    import URY_124eremitoexportacion
if opt == "g":
    import URY_211errorce
if opt == "h":
    import URY_211factura
