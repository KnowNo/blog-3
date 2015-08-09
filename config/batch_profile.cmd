@echo off

REM TODO: bash
REM TODO: windows system tools


REM alias
doskey sublime="C:\Program Files\Sublime Text 2\sublime_text.exe" $*
doskey python3=C:\Python34\python.exe $*

REM path
set PATH=C:\Program Files\Java\jdk1.8.0_31\bin;%PATH%