@echo off
:: Set the script file and output name
SET SCRIPT_FILE=filecreationdilogue.py
SET OUTPUT_NAME=FileCreationDialogue

:: Check if PyInstaller is installed
pyinstaller --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo PyInstaller is not installed. Installing it now...
    pip install pyinstaller
)

:: Compile the Python script into an EXE (no console window)
pyinstaller --noconfirm --noconsole --onefile --name %OUTPUT_NAME% %SCRIPT_FILE%

:: Move the EXE to System32
IF EXIST dist\%OUTPUT_NAME%.exe (
    echo Moving the executable to System32...
    move /Y dist\%OUTPUT_NAME%.exe C:\Windows\System32\%OUTPUT_NAME%.exe
) ELSE (
    echo Compilation failed. Exiting...
    exit /b 1
)

:: Add to context menu using the registry file
IF EXIST Add to right click.reg (
    echo Adding to context menu...
    reg import "Add to right click.reg"
) ELSE (
    echo Registry file not found. Skipping context menu addition...
)

:: Clean up unnecessary files and folders
IF EXIST build (
    rmdir /s /q build
)
IF EXIST %OUTPUT_NAME%.spec (
    del %OUTPUT_NAME%.spec
)

:: Notify the user
echo Setup completed successfully!
pause
