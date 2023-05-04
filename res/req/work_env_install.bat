@echo off
if not defined in_subprocess (cmd /k set in_subprocess=y ^& %0 %*) & exit )
conda env create -f work_env_list_05_2023.yml	
pause