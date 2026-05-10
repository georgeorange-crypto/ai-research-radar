@echo off
REM AI Research Radar - Windows 启动脚本
REM 先复制 .env.example 为 .env 并填入配置

REM 如果 .env 不存在，提示用户
if not exist .env (
    echo [提示] 未找到 .env 文件
    echo [提示] 请先复制 .env.example 为 .env 并填入配置
    echo.
    echo 或者按任意键继续（将使用本地摘要模式）
    pause > nul
) else (
    echo [OK] 找到 .env 文件，加载配置...
)

echo.
echo ========================================
echo AI Research Radar 启动中...
echo ========================================
echo.

python run.py

echo.
echo ========================================
echo 运行完成！
echo ========================================
pause
