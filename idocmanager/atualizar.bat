@echo off
@break off
cls

echo Updating...
echo This process can take up to 2 minutes
echo .
echo .
echo .


rmdir bin, config, country, process, select, idocmanager /Q/S > NUL
rm __init__.py, idocmanager.py, Iniciar.bat, README.ba /Q/F/S > NUL
git clone https://github.com/xDhii/idocmanager.git

cd idocmanager
move bin ..
move config ..
move country ..
move process ..
move select ..
move *.* ..
cd ..



echo Okay, finished ;)
pause