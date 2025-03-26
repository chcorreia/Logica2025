echo Verificando por atualizacoes
@echo off
set DIR_ATUAL=%CD%
cd %~dp0
git remote add upstream https://github.com/chcorreia/Logica2025.git
git pull --ff-only upstream main
cd %DIR_ATUAL%