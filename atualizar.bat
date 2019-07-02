@echo off
@break off
cls
echo Atualizador

echo Este processo ira atualizar o projeto de automacao do TF.
echo Este processo leva ate 2 minutos
echo .
echo .
echo .
sleep 5


git init
git pull https://github.com/xDhii/idocmanager.git
CD .git
del /F/Q/S *.* > NUL
cd ..
RMDIR /Q/S .git