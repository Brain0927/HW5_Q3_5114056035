#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Streamlit 應用檔案清單和部署檢查
"""

import os
import sys

required_files = [
    "streamlit_app.py",
    "redesign_ppt.py",
    "requirements.txt",
    ".streamlit/config.toml",
]

print("📋 檢查必要檔案...")
all_exist = True

for file in required_files:
    exists = os.path.exists(file)
    status = "✅" if exists else "❌"
    print(f"{status} {file}")
    if not exists:
        all_exist = False

if all_exist:
    print("\n✅ 所有必要檔案都存在，可以部署！")
    sys.exit(0)
else:
    print("\n❌ 缺少必要檔案，無法部署")
    sys.exit(1)
