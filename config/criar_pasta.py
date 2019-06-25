## Script para criar a pasta IDOC ## -
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('\033[91mEita, Deu ruim!')
        print('\033[91mNão foi possível criar a pasta IDOC.')
        print('\033[0m')
createFolder('./idoc/')
