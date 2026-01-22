@echo off
echo --- Iniciando Geracao do Site ---
cd /d "%~dp0"
python gerar_tudo.py
echo.
echo --- Executando Diagnostico ---
python verificar_site.py
pause