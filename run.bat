@echo off
REM 🎨 PPT 重新設計工具 - 快速啟動腳本 (Windows)

echo.
echo ============================================================
echo 🎨 PPT AI 重新設計工具 - Streamlit Demo
echo ============================================================
echo.

REM 檢查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python 未安裝，請先安裝 Python 3.8+
    pause
    exit /b 1
)

REM 檢查虛擬環境
if not exist ".venv" (
    echo ⚙️ 創建虛擬環境...
    python -m venv .venv
)

REM 激活虛擬環境
call .venv\Scripts\activate.bat

REM 安裝依賴
echo 📦 安裝依賴套件...
pip install -q -r requirements.txt

echo.
echo ============================================================
echo ✅ 準備就緒！
echo.
echo 🚀 啟動 Streamlit 應用...
echo 📌 應用地址: http://localhost:8501
echo.
echo 💡 提示: 按 Ctrl+C 停止應用
echo ============================================================
echo.

REM 啟動應用
streamlit run Q3_streamlit_app.py

pause
