@echo off
chcp 65001 >nul
echo 程序会自动检测所有 txt 文件，逐个生成 srt。 
set /p input=请输入 Y 开始执行，输入 N 退出：（Y/N）

if /i "%input%"=="Y" (
    echo 开始执行...
    python.exe ./tosrt.py
    echo 结束
    pause
    exit
) else if /i "%input%"=="N" (
    exit
) else (
    echo 无效的输入。
    pause
    exit /b 1
)
