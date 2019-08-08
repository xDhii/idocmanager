## Script para criar a pasta IDOC ## -
import os
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('\033[91mOops, something wrong!')
        print('\033[91mCould not create the IDOC folder.')
        print('\033[0m')
createFolder('./idoc/')
createFolder('./logs/')
createFolder('./bin/')