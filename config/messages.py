## Mensagem de todas as telas ##
import os, sys, shutil

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mensageminicial():
    print('\033[91m Atenção: Todas as empresas devem estar configuradas como SAPKFQ! \033[0m')
    print()
    print("\033[1;30;47m        Criador de IDOC v0.4.00 (beta)              \033[0m")
    print()
    print('\33[1;37;40m Está faltando alguma empresa ou tipo de documento?  \033[0m')
    print('\33[1;37;40m Me avise: adriano.valumin@sovos.com                 \033[0m')
    print()
    print()

def paises_disponiveis():
    print('\033[1m Países Disponíveis para criação de IDOC \033[0m')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mArgentina       \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mBrasil          \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mMéxico          \033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mUruguay         \033[0m')
    print('\033[1;30;47m Z \033[0m - \033[4mZerar Folios    \033[0m')

def empresas_nfse():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mMicrosoft MST   RJ - CNPJ:60316817000286  I.M:01819925 \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mMicrosoft MST   RJ - CNPJ:60316817000286  I.M:30677173 \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mClariant Suzano SP - CNPJ:31452113002871  I.M:18981    \033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mRockwell Aut.   SP - CNPJ:46323754000183  I.M:102660   \033[0m')
    print('\033[1;30;47m E \033[0m - \033[4mRockwell Aut.   SP - CNPJ:46323754000183  I.M:6013110  \033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mSovos NFSe      SP - CNPJ:24492961000129  I.M:3505708  \033[0m')
    print('\033[1;30;47m G \033[0m - \033[4mCepheid EQA     SP - CNPJ:18628083000204  I.M:26914    \033[0m')
    print('\033[1;30;47m H \033[0m - \033[4mMecanotecnica   PR - CNPJ:03715819000123  I.M:23814    \033[0m')
    print('\033[1;30;47m I \033[0m - \033[4mKerry I.Aro.    AM - CNPJ:12796590000190  I.M:1302603  \033[0m')
    print('\033[1;30;47m J \033[0m - \033[4mKerry do Brasil SP - CNPJ:02332686001204  I.M:3513009  \033[0m')
    print('\033[1;30;47m K \033[0m - \033[4mLanxess         RJ - CNPJ:29667227000509  I.M:3301702  \033[0m')
    print('\033[1;30;47m L \033[0m - \033[4mLanxess         RS - CNPJ:29667227000681  I.M:4322004  \033[0m')
    print('\033[1;30;47m M \033[0m - \033[4mLanxess         PE - CNPJ:29667227001068  I.M:2602902  \033[0m')
    print('\033[1;30;47m N \033[0m - \033[4mLanxess         RS - CNPJ:29667227001220  I.M:4322004  \033[0m')
    print('\033[1;30;47m O \033[0m - \033[4mCodesp          SP - CNPJ:44837524000107  I.M:575315   \033[0m')
    print()
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_nfe():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mInvoiceware             SP  - 24492961000129 \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mPaperless               SP  - 10726059000115 \033[0m')
    print()
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_ury():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mSovos Uruguay (McCain)      - 080003530017 \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mDSM                         - 214580250019 \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mSovos Uruguay (SC Johnson)  - 213408960013 \033[0m')
    print()
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_mex():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mSovos Mexico Inbound (CHEP)     - CME940118F7A \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mWeWork - MX - QA                - ALA151026V8A \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mWeWork - MX - QA                - AMA1602043C6 \033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mWeWork - MX - QA                - VTS160204M62 \033[0m')
    print('\033[1;30;47m E \033[0m - \033[4mINVOICEWARE - MX                - BTM060817960 \033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mMexico CANCELLATION - CFDI      - LAN8507268IA \033[0m')
    print('\033[1;30;47m G \033[0m - \033[4mMexico CANCELLATION - CFDI      - MAG041126GT8 \033[0m')
    print()
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_arg():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mSovos Argentina (Rockwell)              - 30681463999 \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mSovos Argentina (Philips) - Local MTX   - 30503747533 \033[0m')
    print()
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')


def tryagain():
    print('Certo, vamos enviar o IDOC para a VM')
    vmdestino = input ('Digite para qual VM você deseja enviar o IDOC: ')
    while len(vmdestino) != 2:
        print ('\033[91m Opa! Você deve inserir 2 dígitos! \033[0m')
        vmdestino = input('Digite novamente o número da VM: ')
    print('\033[93m Tentando enviar o IDOC para INVQASRV'+ str(vmdestino) +'\033[0m')
    print()
    print()
    try:
        print('\033[93m Este processo pode levar até 30 segundos... \033[0m')
        print()
        shutil.move('idoc/outbound.idoc', '//invqasrv'+ str(vmdestino) +'.corp.sovos.local/c$/TF/Queues/IDOCReceiver')
        limpar_tela()
        mensageminicial()
        print('\033[92m Tudo certo! IDOC Enviado! \033[0m')
        print('\033[92m Acompanhe o processamento do documento no portal. \033[0m')
        print()
    except (shutil.Error, OSError, IOError):
        limpar_tela()
        mensageminicial()
        print('\033[91m Opa! Não foi possível enviar o IDOC para a VM selecionada. \033[0m')
        print('\033[91m Você digitou o número da VM correta? \033[0m')
        print()
        tentarnovamente = input('Deseja tentar novamente? Digite S ou N: ')
        tentarnovamente = tentarnovamente.lower()
        while tentarnovamente not in ('n', 's'):
            tentarnovamente = tentarnovamente.lower()
            print('Não entendi sua resposta')
            tentarnovamente = input('Deseja tentar novamente? Digite S ou N: ')
            tentarnovamente = tentarnovamente.lower()
        if tentarnovamente in ('s', 'sim', 'yes'):
            try:
                shutil.move('idoc/outbound.idoc', '//invqasrv'+ str(vmdestino) +'.corp.sovos.local/c$/TF/Queues/IDOCReceiver')
                limpar_tela()
                mensageminicial()
                print('\033[92m Tudo certo! IDOC Enviado! \033[0m')
                print('\033[92m Acompanhe o processamento do documento no portal. \033[0m')
                print()
            except (shutil.Error, OSError, IOError):
                tryagain()
        if tentarnovamente in ("n", "nao", "não", "no", "not"):
            print()
            print('\033[92m Ok! O documento gerado está dentro da pasta IDOC ;) \033[0m')