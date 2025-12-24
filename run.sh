#!/bin/bash
# 🎨 PPT 重新設計工具 - 快速啟動腳本 (macOS/Linux)

echo ""
echo "============================================================"
echo "🎨 PPT AI 重新設計工具 - Streamlit Demo"
echo "============================================================"
echo ""

# 檢查 Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 未安裝，請先安裝 Python 3.8+"
    exit 1
fi

# 檢查虛擬環境
if [ ! -d ".venv" ]; then
    echo "⚙️  創建虛擬環境..."
    python3 -m venv .venv
fi

# 激活虛擬環境
source .venv/bin/activate

# 安裝依賴
echo "📦 安裝依賴套件..."
pip install -q -r requirements.txt

echo ""
echo "============================================================"
echo "✅ 準備就緒！"
echo ""
echo "🚀 啟動 Streamlit 應用..."
echo "📌 應用地址: http://localhost:8501"
echo ""
echo "💡 提示: 按 Ctrl+C 停止應用"
echo "============================================================"
echo ""

# 啟動應用
streamlit run Q3_streamlit_app.py
