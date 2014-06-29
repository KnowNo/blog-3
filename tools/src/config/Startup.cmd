@echo off

REM Setup PATH
set PATH=%PATH%;D:\Tools\gradle-1.8-all\gradle-1.8\bin
set PATH=%PATH%;D:\Tools\groovy-binary-2.1.8\groovy-2.1.8\bin
set PATH=%PATH%;D:\Tools\lua-5.2.1_Win32_bin
set PATH=%PATH%;D:\Tools\premake-4.4-beta4-windows
set PATH=%PATH%;D:\Tools\eclipse-standard-kepler-SR1-win32\eclipse
set PATH=%PATH%;C:\Program Files\Java\jdk1.7.0_45\bin
set PATH=%PATH%;D:\Tools\GnuWin32\GetGnuWin32\gnuwin32\bin
set PATH=%PATH%;C:\Python27
set PATH=%PATH%;C:\Python27\Scripts
set PATH=%PATH%;D:\Tools\sqlite-shell-win32-x86-3080301
set PATH=%PATH%;D:\Tools\apache-ant-1.8.2\bin
set PATH=%PATH%;C:\Program Files\Apache Software Foundation\Apache2.2\bin
set PATH=%PATH%;C:\Program Files\MySQL\MySQL Server 5.6\bin
set PATH=%PATH%;C:\Program Files\Graphviz2.38\bin
set PATH=%PATh%;D:\Tools\ProcessExplorer

REM Configure doskey (alias in linux)
doskey sublime="C:\Program Files\Sublime Text 2\sublime_text.exe" $*
doskey groovyConsole=start groovyConsole.bat $*
doskey MySQLWorkBench="C:\Program Files\MySQL\MySQL Workbench CE 6.0.9\MySQLWorkbench.exe" $*
doskey errlook="C:\Program Files\Microsoft Visual Studio 10.0\Common7\Tools\errlook.exe"
doskey premake="D:\Tools\premake-4.4-beta5-windows\premake4.exe" $*
doskey msbuild="C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild" $*

REM Setup python startup scripts
set PYTHONSTARTUP=D:\Source\GitHub\tools\src\startup.py

REM Start in D: directory
D:
cd D:\Source
cls