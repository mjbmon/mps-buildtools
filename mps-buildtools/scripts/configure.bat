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

echo "Getting MPS_BUILDTOOLS..."
set blist= %MPS_BUILDTOOLS% %PROJECT_TOP_DIR% %PROJECT_TOP_DIR%\.. %HOMEPATH%\.local\.lib
for %%b in (%blist%) do (
  set bt=%%b%\mps-buildtools
  echo "Look for %bt%"
  if exist %bt% (
    if exist %bt%\configure.py (
      echo "Found %bt%"
      goto :found_buildtools
    )
  )
)
echo "Cannot find mps-buildtools"
exit /B

:found_buildtools
MPS_BUILDTOOLS=%bt%

echo "Running configure.py..."
%PYTHON%  %MPS_BUILDTOOLS%\configure.py %*

echo "Configure done."
