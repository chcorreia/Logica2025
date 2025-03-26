echo Configura o python
@echo off
python -m venv %~dp0venv
%~dp0venv\Scripts\activate
pip install -r %~dp0requirements.txt