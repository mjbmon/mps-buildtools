@echo off

echo "Windows configure script"

echo "Getting PROJECT_TOP_DIR..."
set PROJECT_TOP_DIR=%~dp0
echo "PROJECT_TOP_DIR is %PROJECT_TOP_DIR%"


echo "Checking python..."
set PYTHON=python
set P="%PYTHON% --version"
FOR /F "delims=" %%i IN ('%P%') DO set PYTHON_VERSION=%%i
echo "PYTHON VERSION is %PYTHON_VERSION%"

echo "Getting MPS_BUILDTOOLS"
if exist .\mps-buildtools (
  echo set MPS_BUILDTOOLS=.\mps-buildtools
  set MPS_BUILDTOOLS=.\mps-buildtools
) else (
    if exist ..\mps-buildtools (
       echo set  MPS_BUILDTOOLS=..\mps-buildtools
       set  MPS_BUILDTOOLS=..\mps-buildtools
        ) else (
             if "%MPS_BUILDTOOLS%"=="" (
                echo "Cannot find mps-buildtools"
                exit /B
           )
     )
)

echo "MPS_BUILDTOOLS %MPS_BUILDTOOLS%"

echo "Running configure.py ..."
%PYTHON%  %MPS_BUILDTOOLS%\configure.py %*

echo "Configure done."
