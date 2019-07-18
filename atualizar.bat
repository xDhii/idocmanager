@echo off
@break off
cls

echo Updating...
echo This process can take up to 2 minutes
echo .
echo .
echo .


rmdir bin, config, country, process, select, idocmanager, .git, git /Q/S > NUL
del __init__.py /Q/F/S > NULdel idocmanager.py /Q/F/S > NUL
del Iniciar.bat /Q/F/S > NUL
del README.md /Q/F/S > NUL
git clone https://github.com/xDhii/idocmanager.git

cd idocmanager
attrib -s -h .git
echo
ren .git git
move git ..
move bin ..
move config ..
move country ..
move process ..
move select ..
move idocmanager.py ..
move Iniciar.bat ..
move README.md ..
move __init__.py
cd ..
ren git .git
attrib +h .git
rmdir idocmanager /Q/S > NUL


echo Okay, finished ;)
pause