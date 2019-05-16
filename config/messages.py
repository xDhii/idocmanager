## Mensagem de todas as telas ##
import os, sys, shutil

def atencao():
    print('\033[91m Atenção: Todas as empresas devem estar configuradas como SAPKFQ!')
    print()
    print('\033[91m Caso contrário, o programa não irá funcionar!')
    print()
    print()
    continuar = input('\033[1m Digite S para continuar ou N para encerrar o programa:\033[0m ')
    continuar = continuar.lower()
    while continuar not in ('s', 'n'):
        print(' Não entendi sua resposta.')
        atencao()
    if continuar == "s":
            print()
    if continuar == "n":
        sys.exit
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def mensageminicial():
    print()
    print("\033[1;30;47m        Criador de IDOC v0.2.191 (beta)        ")
    print()
    print('\33[1;37;40mEstá faltando alguma empresa ou tipo de documento?')
    print('\33[1;37;40mMe avise: adriano.valumin@sovos.com')
    print('\033[0m')
    print()
    print()

def paises_disponiveis():
    print('\033[1mPaíses Disponíveis para criação de IDOC\033[0m')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mA -  Brasil     \033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mA -  México     \033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mB -  Uruguay    \033[0m')

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
    print('\033[0m')
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_nfe():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mInvoiceware          SP  - 24492961000129\033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mInvoiceware          SP  - 24493109000176\033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mInvoiceware          RS  - 15373395001036\033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mInvoiceware          SP  - 10726059000115\033[0m')
    print('\033[1;30;47m E \033[0m - \033[4mBrow Forman          SC  - 00305765000210\033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mPhilips              MG  - 22555787000352\033[0m')
    print('\033[1;30;47m G \033[0m - \033[4mInfoglobo            RJ  - 04067191000755\033[0m')
    print('\033[1;30;47m H \033[0m - \033[4mEMS GERMED           SP  - 57507378000365\033[0m')
    print('\033[1;30;47m I \033[0m - \033[4mEdwards BR NFM       SP  - 05944604000533\033[0m')
    print('\033[1;30;47m J \033[0m - \033[4mOrica BR             PA  - 31056708001917\033[0m')
    print('\033[1;30;47m K \033[0m - \033[4mComp. de Dist.       MS  - 11517841003455\033[0m')
    print('\033[1;30;47m L \033[0m - \033[4mPhilips Medical      SP  - 58295213000178\033[0m')
    print('\033[1;30;47m M \033[0m - \033[4mPhilips Medical      MG  - 58295213002111\033[0m')
    print('\033[1;30;47m N \033[0m - \033[4mBiomerieux           RJ  - 33040635000171\033[0m')
    print('\033[1;30;47m O \033[0m - \033[4mSabo Autopeças       SP  - 60860681001323\033[0m')
    print('\033[0m')
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_ury():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mSovos Uruguay (McCain)      - 080003530017\033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mDSM                         - 214580250019\033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mSovos Uruguay (SC Johnson)  - 213408960013\033[0m')
    print('\033[0m')
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')

def empresas_mex():
    print()
    print('Lista de empresas cadastradas:')
    print()
    print('\033[1;30;47m A \033[0m - \033[4mSovos Mexico Inbound (CHEP)     - CME940118F7A\033[0m')
    print('\033[1;30;47m B \033[0m - \033[4mWeWork - MX - QA                - ALA151026V8A\033[0m')
    print('\033[1;30;47m C \033[0m - \033[4mWeWork - MX - QA                - AMA1602043C6\033[0m')
    print('\033[1;30;47m D \033[0m - \033[4mWeWork - MX - QA                - VTS160204M62\033[0m')    
    print('\033[1;30;47m E \033[0m - \033[4mINVOICEWARE - MX                - BTM060817960\033[0m')
    print('\033[1;30;47m F \033[0m - \033[4mMexico CANCELLATION - CFDI      - LAN8507268IA\033[0m')
    print('\033[1;30;47m G \033[0m - \033[4mMexico CANCELLATION - CFDI      - MAG041126GT8\033[0m')
    print('\033[0m')
    print('Certo, e qual das empresas acima deseja utilizar no IDOC?')


def tryagain():
    print('Certo, vamos enviar o IDOC para a VM')
    vmdestino = input ('Digite para qual VM você deseja enviar o IDOC: ')
    while len(vmdestino) != 2:
        print ('\033[91mOpa! Você deve inserir 2 dígitos!')
        vmdestino = input('\033[0mDigite novamente o número da VM: ')
    print('\033[93mTentando enviar o IDOC para INVQASRV'+ str(vmdestino))
    print('\033[0m')
    print()
    try:
        print('\033[93mEste processo pode levar até 30 segundos...')
        print('\033[0m')        
        shutil.move('idoc/outbound.idoc', '//invqasrv'+ str(vmdestino) +'.corp.sovos.local/c$/TF/Queues/IDOCReceiver')  
        limpar_tela()
        mensageminicial()
        print('\033[92mTudo certo! IDOC Enviado!')
        print('Acompanhe o processamento do documento no portal.')
        print('\033[0m')
    except (shutil.Error, OSError, IOError):
        limpar_tela()
        mensageminicial()
        print('\033[91mOpa! Não foi possível enviar o IDOC para a VM selecionada.')
        print('\033[0m')
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
                print('\033[92mTudo certo! IDOC Enviado!')
                print('Acompanhe o processamento do documento no portal.')
                print('\033[0m')
            except (shutil.Error, OSError, IOError):
                tryagain()
        if tentarnovamente in ("n", "nao", "não", "no", "not"):
            print()
            print('\033[92mOk! O documento gerado está dentro da pasta IDOC ;)')