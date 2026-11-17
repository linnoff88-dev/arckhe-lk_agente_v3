@echo off
REM ========================================
REM LiveKit Agent V3 - Setup Inicial
REM ========================================
REM Este script recria o ambiente virtual
REM e instala todas as dependencias
REM ========================================

echo.
echo ========================================
echo   LiveKit Agent V3 - Setup
echo   Configuracao Inicial do Ambiente
echo ========================================
echo.

REM Remove venv antigo se existir
if exist venv (
    echo [INFO] Removendo ambiente virtual antigo...
    rmdir /s /q venv
    echo [OK] Ambiente antigo removido.
    echo.
)

REM Cria novo ambiente virtual
echo [INFO] Criando novo ambiente virtual...
python -m venv venv
if %errorlevel% neq 0 (
    echo [ERRO] Falha ao criar ambiente virtual!
    echo [INFO] Verifique se Python 3.10+ esta instalado
    pause
    exit /b 1
)
echo [OK] Ambiente virtual criado.
echo.

REM Ativa o ambiente
echo [INFO] Ativando ambiente virtual...
call venv\Scripts\activate.bat

REM Atualiza pip
echo [INFO] Atualizando pip...
python -m pip install --upgrade pip --quiet
echo [OK] pip atualizado.
echo.

REM Instala dependencias
echo [INFO] Instalando dependencias...
echo [INFO] Isso pode levar alguns minutos...
echo.
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo [ERRO] Falha ao instalar dependencias!
    pause
    exit /b 1
)
echo.
echo [OK] Dependencias instaladas com sucesso!
echo.

REM Verifica se .env existe
if not exist .env (
    echo ========================================
    echo   ATENCAO: Configuracao Necessaria
    echo ========================================
    echo.
    echo [AVISO] Arquivo .env nao encontrado!
    echo.
    echo Proximo passo:
    echo 1. Copie .env.example para .env
    echo 2. Edite .env com suas API keys
    echo.
    echo Comando: copy .env.example .env
    echo.
    pause
) else (
    echo [OK] Arquivo .env encontrado.
    echo.
)

REM Testa as importacoes
echo [INFO] Testando instalacao...
python -c "from livekit import agents; from livekit.plugins import openai, deepgram; print('[OK] Todos os modulos importados com sucesso!')"
if %errorlevel% neq 0 (
    echo [ERRO] Falha ao importar modulos!
    pause
    exit /b 1
)
echo.

echo ========================================
echo   Setup Concluido com Sucesso!
echo ========================================
echo.
echo Proximo passo: Execute start.bat
echo.
pause
