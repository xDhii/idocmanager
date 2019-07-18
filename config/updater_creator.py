def create_updater():
    f = open('Updater.bat', 'w')
    f.write('@echo off\n')
    f.write('@break off\n')
    f.write('cls\n')
    f.write(' \n')
    f.write('echo Updating...\n')
    f.write('echo This process can take up to 2 minutes\n')
    f.write('echo .\n')
    f.write('echo .\n')
    f.write('echo .\n')
    f.write(' \n')
    f.write('rmdir bin, config, country, process, select, idocmanager, .git, git /Q/S > NUL\n')
    f.write('del __init__.py /Q/F/S > NULdel idocmanager.py /Q/F/S > NUL\n')
    f.write('del Iniciar.bat /Q/F/S > NUL\n')
    f.write('del README.md /Q/F/S > NUL\n')
    f.write('git clone https://github.com/xDhii/idocmanager.git\n')
    f.write(' \n')
    f.write('cd idocmanager\n')
    f.write('attrib -s -h .git\n')
    f.write('echo\n')
    f.write('ren .git git\n')
    f.write('move git ..\n')
    f.write('move bin ..\n')
    f.write('move config ..\n')
    f.write('move country ..\n')
    f.write('move process ..\n')
    f.write('move select ..\n')
    f.write('move idocmanager.py ..\n')
    f.write('move Iniciar.bat ..\n')
    f.write('move README.md ..\n')
    f.write('move __init__.py\n')
    f.write('cd ..\n')
    f.write('ren git .git\n')
    f.write('attrib +h .git\n')
    f.write('rmdir idocmanager /Q/S > NUL\n')
    f.write(' \n')
    f.write(' \n')
    f.write('echo Okay, finished ;)\n')
    f.write('pause\n')
    f.write('del Updater.bat /Q/F/S > NUL\n')
    f.close