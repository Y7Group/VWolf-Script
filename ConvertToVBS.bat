@echo off
title VWolf script compiler

set /p vw_file=Enter the path to the VWolfScript file: 
set /p output_file=Enter the output file name: 

python3 converter.py "%vw_file%" "%output_file%"
