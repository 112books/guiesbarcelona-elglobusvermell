@echo off
REM El Globus Vermell — Publicar canvis (Windows)
REM Fes doble clic aqui despres d'editar els fitxers .md

where bash >nul 2>nul
if %errorlevel% neq 0 (
    echo.
    echo No s'ha trobat Git Bash al sistema.
    echo Instal-la "Git for Windows" des de https://git-scm.com/download/win
    echo ^(inclou Git Bash, nomes cal fer-ho un cop^)
    echo.
    pause
    exit /b 1
)

bash "%~dp0publica-canvis"
echo.
pause
