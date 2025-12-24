# 🎨 PPT AI 重新設計工具

智慧設計系統，一鍵為您的 PowerPoint 進行版型重新設計

## 🚀 快速開始

### 線上試用（推薦）
最簡單的方式是直接訪問已部署的線上版本：

**📌 應用連結**: https://ppt-redesign-app.streamlit.app

### 本地運行
如果想在本地運行：

```bash
# 1. 克隆或下載此倉庫
cd HW5_Q3_5114056035-master

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 運行應用
streamlit run Q3_streamlit_app.py
```

應用將在 http://localhost:8501 啟動

## ✨ 功能特性

### 🎨 兩種設計風格

**1. 現代科技風** 🚀
- 深藍背景 + 亮藍紫色強調
- 高對比、視覺衝擊力大
- 適合技術展示、產品發表

**2. 商務沉穩風** 💼
- 淺灰背景 + 金色標題
- 專業可信、企業級感受
- 適合商業洽談、投資簡報

### ⚡ 核心功能

✅ **PPT 檔案上傳**
- 支持 .pptx 格式（PowerPoint 2007+）
- 自動驗證和信息提取

✅ **實時設計預覽**
- 看到配色方案
- RGB 顏色數值參考

✅ **一鍵應用**
- 批量處理所有投影片
- 保留 100% 原始內容

✅ **即時下載**
- 生成新 PPT
- 自動命名方便識別

## 📊 使用示例

1. **打開應用** → 訪問上方連結
2. **上傳 PPT** → 選擇您的 .pptx 檔案
3. **選擇風格** → 選擇喜歡的設計方案
4. **應用設計** → 點擊「✨ 應用設計」按鈕
5. **下載成果** → 點擊「📥 下載設計後的 PPT」

## 🔧 技術架構

```
前端: Streamlit (Python Web UI)
↓
後端: python-pptx (PPT 處理引擎)
↓
輸出: 重新設計的 .pptx 檔案
```

### 技術棧
- Python 3.12
- Streamlit 1.28.1
- python-pptx 0.6.21
- Pillow 10.1.0

## 📁 項目結構

```
HW5_Q3_5114056035-master/
│
├── 📌 核心應用
│   ├── streamlit_app.py                 # Streamlit 主應用
│   ├── redesign_ppt.py                  # PPT 設計邏輯
│   └── requirements.txt                 # Python 依賴
│
├── 📊 設計成果
│   ├── 風格1_現代科技風.pptx
│   ├── 風格2_商務沉穩風.pptx
│   └── 251021_AI_CP值比較器_V1_第9組.pptx (原始檔案)
│
├── 📚 文檔
│   ├── README.md                        # 本檔案
│   ├── AI_設計過程及決策文檔.md
│   ├── 技術實現細節.md
│   ├── Streamlit_部署指南.md
│   └── 作業提交清單.md
│
└── ⚙️ 配置
    └── .streamlit/
        └── config.toml                  # Streamlit 配置
```

## 🎓 作業背景

**課程**: 智慧計算系統  
**作業**: Q3 - PPT 換版型（AI 重新設計）  
**要求**: 輸出至少 2 種不同風格的新 PPT + 對話過程記錄  
**完成日期**: 2025 年 12 月 24 日

## 💡 設計決策

### 為什麼選擇 Streamlit？

| 方案 | 優點 | 缺點 |
|-----|------|------|
| **Streamlit** ✅ | 簡潔、快速、線上部署 | 功能相對基礎 |
| ChatGPT + DALL·E | 功能強大 | 需付費、無法自動化 |
| PowerPoint Designer | 官方工具 | 需要 Microsoft 365 |
| n8n | 企業級 | 配置複雜 |

### 配色原理

**現代科技風配色**:
- RGB (20, 30, 60) = 深藍 → 沉穩專業
- RGB (255, 255, 255) = 白色 → 高對比度 (WCAG AAA)
- RGB (100, 200, 255) = 亮藍 → 科技感
- 對比度 21:1，無障礙友善

**商務沉穩風配色**:
- RGB (240, 240, 240) = 淺灰 → 簡潔清爽
- RGB (184, 134, 11) = 金色 → 高級專業
- RGB (60, 60, 60) = 深灰 → 易讀穩重
- 易於列印，傳統配色

## 🚀 部署指南

### 方式 1：Streamlit Cloud（推薦）

1. **準備 GitHub 倉庫**
   ```bash
   git init
   git add .
   git commit -m "Add PPT redesign app"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/ppt-redesign-app
   git push -u origin main
   ```

2. **訪問 Streamlit Cloud**
   - 前往 https://share.streamlit.io
   - 點擊「New app」
   - 連接 GitHub 倉庫
   - 設定：
     - Repository: `your-username/ppt-redesign-app`
     - Branch: `main`
     - Main file: `streamlit_app.py`

3. **自動部署**
   - Streamlit 會自動構建和部署
   - 您的應用 URL 會被生成

### 方式 2：本地運行

```bash
# 安裝依賴
pip install -r requirements.txt

# 運行應用
streamlit run Q3_streamlit_app.py

# 應用在 http://localhost:8501 啟動
```

### 方式 3：Docker 部署

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["streamlit", "run", "streamlit_app.py"]
```

```bash
docker build -t ppt-redesign .
docker run -p 8501:8501 ppt-redesign
```

## ❓ 常見問題

### Q：應用支持哪些格式？
**A**: 僅支持 .pptx 格式（PowerPoint 2007+）。舊版 .ppt 格式不支持。

### Q：可以修改配色嗎？
**A**: 可以！編輯 `streamlit_app.py` 中的 `STYLE_CONFIGS` 字典，然後重新部署。

### Q：如何添加新風格？
**A**: 在 `STYLE_CONFIGS` 中添加新的配置：
```python
"新風格": {
    "name": "New Style",
    "description": "描述",
    "colors": {
        "bg": (r, g, b),
        "text": (r, g, b),
        "accent1": (r, g, b),
        "accent2": (r, g, b),
    },
    "preview_bg": "#HEX",
    "preview_text": "#HEX",
    "emoji": "🎯"
}
```

### Q：應用無法打開怎麼辦？
**A**: 檢查：
1. Python 版本 ≥ 3.8
2. 依賴已安裝：`pip install -r requirements.txt`
3. 防火牆未阻擋端口 8501

### Q：PPT 下載後無法打開？
**A**: 
1. 確保使用 PowerPoint 2007 或以上版本
2. 試試用 LibreOffice Impress 打開
3. 檢查磁盤空間是否充足

## 📈 功能改進計畫

- [ ] 支持 .ppt 舊格式轉換
- [ ] 自訂配色工具（顏色選擇器）
- [ ] 投影片預覽功能
- [ ] 批量上傳和轉換
- [ ] AI 智能配色建議（基於內容）
- [ ] 模板庫（預設設計風格）

## 🤝 貢獻

歡迎提交 Issue 和 Pull Request！

## 📄 授權

MIT License - 自由使用和修改

## 👨‍💼 作者

**學號**: 5114056035  
**課程**: 智慧計算系統  
**日期**: 2025 年 12 月 24 日

---

## 📞 技術支援

遇到問題？

1. **檢查日誌** → 查看終端輸出
2. **驗證檔案** → 確認 .pptx 格式
3. **重新安裝依賴** → `pip install -r requirements.txt --upgrade`
4. **清除緩存** → `rm -rf .streamlit/` 並重新運行

---

**🎉 感謝使用本應用！**

應用連結: https://ppt-redesign-app.streamlit.app

