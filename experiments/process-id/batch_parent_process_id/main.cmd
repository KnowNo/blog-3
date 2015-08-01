@echo off

echo 1. main.cmd launch python directly:
python %~dp0\show_parent_process_id.py

echo 2 main.cmd launch cmd by call
call %~dp0\show_parent_process_id.cmd

echo 3 main.cmd launch cmd by default:
%~dp0\show_parent_process_id.cmd

