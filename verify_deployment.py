#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🎨 PPT 應用驗證腳本
檢查應用是否可以正常部署到 Streamlit Cloud
"""

import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

def check_files():
    """檢查必要檔案"""
    print("\n📋 檢查必要檔案...")
    print("=" * 60)
    
    required_files = {
        'streamlit_app.py': '主應用程式',
        'requirements.txt': 'Python 依賴清單',
        '.streamlit/config.toml': 'Streamlit 配置',
        'README.md': '專案說明',
        '風格1_現代科技風.pptx': '設計範例 1',
        '風格2_商務沉穩風.pptx': '設計範例 2',
    }
    
    passed = 0
    for file, description in required_files.items():
        exists = os.path.exists(file)
        status = "✅" if exists else "❌"
        print(f"{status} {file:40} ({description})")
        if exists:
            passed += 1
    
    return passed == len(required_files)

def check_dependencies():
    """檢查依賴"""
    print("\n📦 檢查 Python 依賴...")
    print("=" * 60)
    
    try:
        import streamlit as st
        print(f"✅ streamlit {st.__version__}")
    except ImportError:
        print("❌ streamlit (未安裝)")
        return False
    
    try:
        import pptx
        print(f"✅ python-pptx {pptx.__version__}")
    except ImportError:
        print("❌ python-pptx (未安裝)")
        return False
    
    try:
        import PIL
        print(f"✅ pillow {PIL.__version__}")
    except ImportError:
        print("❌ pillow (未安裝)")
        return False
    
    return True

def check_python_version():
    """檢查 Python 版本"""
    print("\n🐍 檢查 Python 版本...")
    print("=" * 60)
    
    version = sys.version_info
    print(f"Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 8:
        print("✅ 版本符合要求 (需要 3.8+)")
        return True
    else:
        print("❌ 版本過舊，請升級到 3.8+")
        return False

def check_git():
    """檢查 Git 設置"""
    print("\n🔗 檢查 Git 設置...")
    print("=" * 60)
    
    if os.path.exists('.git'):
        print("✅ Git 倉庫已初始化")
        return True
    else:
        print("⚠️  Git 倉庫未初始化")
        print("   執行: git init")
        return False

def main():
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + "  🎨 PPT 應用部署前檢查  ".center(58) + "║")
    print("╚" + "=" * 58 + "╝")
    
    results = {
        "檔案檢查": check_files(),
        "Python 版本": check_python_version(),
        "依賴檢查": check_dependencies(),
        "Git 設置": check_git(),
    }
    
    # 總結
    print("\n" + "=" * 60)
    print("📊 檢查總結")
    print("=" * 60)
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for check, result in results.items():
        status = "✅" if result else "⚠️ "
        print(f"{status} {check}")
    
    print(f"\n結果: {passed}/{total} 檢查通過")
    
    if passed == total:
        print("\n" + "=" * 60)
        print("🎉 所有檢查通過！應用可以部署")
        print("=" * 60)
        print("\n🚀 後續步驟:")
        print("  1. 本地測試: streamlit run streamlit_app.py")
        print("  2. 推送到 GitHub: git push origin main")
        print("  3. 在 Streamlit Cloud 部署")
        print("  4. 分享應用連結")
        return 0
    else:
        print("\n" + "=" * 60)
        print("⚠️  部分檢查未通過，請修復後重試")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
