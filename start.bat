@echo off
REM ========================================
REM LiveKit Agent V3 - Inicializador
REM ========================================

echo.
echo ========================================
echo   LiveKit Agent V3
echo   Agente de Voz em Portugues
echo ========================================
echo.

REM Ativa o ambiente virtual
if exist venv\Scripts\activate.bat (
    echo [INFO] Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo [ERRO] Ambiente virtual nao encontrado!
    echo [INFO] Execute: python -m venv venv
    echo [INFO] Depois: venv\Scripts\pip install -r requirements.txt
    pause
    exit /b 1
)

REM Verifica se .env existe
if not exist .env (
    echo [AVISO] Arquivo .env nao encontrado!
    echo [INFO] Copie .env.example para .env e configure as chaves
    pause
    exit /b 1
)

REM Inicia o agente
echo [INFO] Iniciando agente v3...
echo.
python agent.py dev

pause
