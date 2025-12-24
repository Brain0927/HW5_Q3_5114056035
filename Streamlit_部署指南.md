# 📋 Streamlit 部署指南

## 本地運行

### 方式 1：直接運行

```bash
cd d:\00_student\02_AIOT\Homework5\HW5_Q3_5114056035-master

# 啟動 Streamlit 應用
streamlit run streamlit_app.py
```

應用會在 `http://localhost:8501` 啟動

### 方式 2：使用虛擬環境

```bash
# 激活虛擬環境
.venv\Scripts\Activate.ps1

# 安裝依賴
pip install -r requirements.txt

# 運行應用
streamlit run streamlit_app.py
```

---

## 部署到 Streamlit Cloud

### 前提條件：
1. GitHub 帳號
2. Streamlit 帳號（可用 GitHub 登入）

### 部署步驟：

#### 第 1 步：上傳到 GitHub

```bash
# 初始化 Git 倉庫
git init
git add .
git commit -m "Add PPT redesign Streamlit app"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/ppt-redesign-app.git
git push -u origin main
```

#### 第 2 步：連接到 Streamlit Cloud

1. 訪問 https://share.streamlit.io
2. 點擊「New app」
3. 連接 GitHub 倉庫
4. 選擇：
   - Repository: `YOUR_USERNAME/ppt-redesign-app`
   - Branch: `main`
   - Main file path: `streamlit_app.py`

#### 第 3 步：部署

- Streamlit 會自動部署
- 您的應用 URL: `https://share.streamlit.io/YOUR_USERNAME/ppt-redesign-app`

---

## 檔案結構

```
HW5_Q3_5114056035-master/
├── streamlit_app.py              # Streamlit 應用主程式
├── requirements.txt              # Python 依賴
├── .streamlit/
│   └── config.toml              # Streamlit 配置
├── redesign_ppt.py              # 核心設計邏輯
├── 風格1_現代科技風.pptx         # 設計範例 1
├── 風格2_商務沉穩風.pptx         # 設計範例 2
└── README.md                    # 本說明檔
```

---

## 功能特點

✅ **上傳 PPT 檔案**
- 支持 .pptx 格式
- 顯示檔案信息（投影片數、大小、尺寸）

✅ **選擇設計風格**
- 現代科技風：深藍 + 亮藍 + 紫色
- 商務沉穩風：淺灰 + 金色

✅ **實時預覽**
- 配色方案視覺展示
- RGB 顏色數值

✅ **即時下載**
- 點擊後生成新 PPT
- 自動命名

---

## 技術棧

- **後端**: Python 3.12
- **前端**: Streamlit 1.28.1
- **PPT 處理**: python-pptx 0.6.21
- **部署平台**: Streamlit Cloud

---

## 常見問題

### Q：為什麼上傳後沒有反應？
A：檢查檔案格式是否為 .pptx，不是 .ppt

### Q：下載的 PPT 無法打開？
A：確保使用 PowerPoint 2007 或以上版本

### Q：可以修改配色嗎？
A：可以，編輯 `STYLE_CONFIGS` 字典中的顏色值

---

## 支援與反饋

如有問題，請檢查：
1. Python 版本 ≥ 3.8
2. 所有依賴已安裝：`pip install -r requirements.txt`
3. 檔案路徑正確

---

