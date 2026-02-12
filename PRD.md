# 遊戲中心 PRD

## 基本資訊
- 網站名稱：BillyWa's Center
- 設計風格：深色科技感 + 簡約現代
- 主色調：深藍 #05070a + 霓虹藍 #00f2ff + 霓虹紫 #7000ff + 霓虹粉 #ff00c8
- 語言：繁體中文 (zh-TW)
- 目標：提供單一 HTML 文件的瀏覽器遊戲集合，無需外部依賴

## 功能需求
1. **黑暗/明亮模式切換**：用戶可切換深色與明亮主題
2. **響應式設計**：支援桌面、平板、手機
3. **遊戲卡片瀏覽**：分類展示所有遊戲
4. **快速載入**：每個遊戲為獨立 HTML 文件，點擊即玩
5. **無障礙設計**：符合 WAI-ARIA 標準

## 遊戲列表

### SOLO 單人挑戰
1. **經典貪食蛇** (snack.html) - 最純粹的挑戰，在方寸之間考驗反應，讓你的蛇成為王者。
2. **Block Blast** (block_blast.html) - 極簡風格的積木消除遊戲，放鬆心情，釋放壓力。
3. **水果忍者** (fruit_ninja.html) - 刀光劍影，切碎迎面而來的水果，享受切割的快感。
4. **意念控制** (telekinesis.html) - 獨特的超能力體驗，用你的「心靈感應」來掌控一切。
5. **恐龍獵人 3D** (dino_hunter.html) - 重返遠古時代，面對兇猛的史前巨獸，你能生存下來嗎？

### VERSUS 雙人對戰
6. **極速乒乓** (touch_pong.html) - 同屏競技，指尖對決。最快、最直接的乒乓球體驗。
7. **雙人冰球** (air_hockey.html) - 實體物理碰撞感，與朋友一起享受快節奏的對壘。
8. **井字對弈** (tic_tac_toe.html) - 經典中的經典，簡單卻百玩不厭的智力較量。

### MIND 棋類智慧
9. **五子棋** (gomoku.html) - 五星連珠，步步驚心。提供強大的 AI 與雙人模式。
10. **中國象棋** (chinese_chess.html) - 將相之爭，楚河漢界。傳統棋藝的現代數位重現。

### 3D 實驗遊戲 (位於 3D-test/)
11. **3D 手勢控制粒子系統** (3D-test/deepseek-v3.2.html) - 使用手勢控制 3D 粒子系統的沉浸式體驗
12. **其他 3D 實驗** (3D-test/gemini-3-pro.html, glm-4.7.html, minimax-m2.1.html, qwen-3-max.html) - 各種 3D 互動演示

## 頁面結構
- **Header**：網站標題 "BillyWa's Center" + slogan "Fun&releax"
- **遊戲卡片區**：每張卡片包含 [遊戲圖示 / 遊戲名 / 簡介 / 標籤 / 開始按鈕]
- **分類區**：SOLO、VERSUS、MIND 三大分類
- **Footer**：版權資訊 "© 2026 BillyWa. Built with Neon Energy."

## 設計規範

### 色彩系統
- **深色模式**：
  - 背景：var(--bg-dark) = #05070a
  - 主要文字：var(--text-main) = #e2e8f0
  - 次要文字：var(--text-dim) = #94a3b8
  - 強調色：var(--accent-primary) = #00f2ff (藍)
  - 輔助色：var(--accent-secondary) = #7000ff (紫)
  - 輔助色：var(--accent-tertiary) = #ff00c8 (粉)

- **明亮模式**：(待定義)
  - 背景：淺灰或白色
  - 文字：深灰色
  - 強調色：保持相同色系但調整飽和度

### 排版
- 標題字體：Orbitron (科技感)
- 正文字體：Noto Sans TC (繁體中文支援)
- 字體大小：使用 clamp() 實現響應式

### 動畫與過渡
- 卡片懸浮效果：translateY(-10px) + scale(1.02)
- 載入動畫：旋轉 spinner
- 背景動畫：網格透視 + 漸變光暈

## 技術規格

### 文件結構
```
.
├── index.html          # 主入口頁面
├── snack.html          # 貪食蛇
├── block_blast.html    # 方塊消除
├── fruit_ninja.html    # 水果忍者
├── telekinesis.html    # 意念控制
├── dino_hunter.html    # 恐龍獵人 3D
├── touch_pong.html     # 極速乒乓
├── air_hockey.html     # 雙人冰球
├── tic_tac_toe.html    # 井字棋
├── gomoku.html         # 五子棋
├── chinese_chess.html  # 中國象棋
├── 3D-test/            # 3D 實驗遊戲目錄
│   ├── deepseek-v3.2.html
│   ├── gemini-3-pro.html
│   ├── glm-4.7.html
│   ├── minimax-m2.1.html
│   ├── qwen-3-max.html
│   └── lib/            # 3D 庫
├── AGENTS.md           # 開發指南
├── README.md           # 項目說明
└── PRD.md              # 本文件
```

### 技術棧
- **HTML5**：語義化標籤
- **CSS3**：CSS 變數、Flexbox、Grid、媒體查詢
- **JavaScript**：原生 ES6+，無框架
- **遊戲技術**：Canvas 2D、WebGL (Three.js)、MediaPipe (手勢識別)

### 瀏覽器兼容性
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- iOS Safari
- Chrome for Android

## 待辦事項

### 高優先級
1. [ ] 實現黑暗/明亮模式切換功能
2. [ ] 優化現有 index.html 的響應式設計
3. [ ] 為 3D 遊戲添加導航連結到主頁

### 中優先級
4. [ ] 為每個遊戲添加統一的返回按鈕
5. [ ] 實現 localStorage 保存高分功能
6. [ ] 添加遊戲搜索或過濾功能

### 低優先級
7. [ ] 添加遊戲統計（遊玩次數、總分）
8. [ ] 實現用戶自定義主題
9. [ ] 添加遊戲成就系統

## 成功指標
1. 所有遊戲在主流瀏覽器正常運行
2. 頁面載入時間 < 3 秒
3. 移動端觸控體驗流暢
4. 無障礙評分 ≥ 90/100
5. 用戶可無縫切換黑暗/明亮模式

## 附錄

### 遊戲分類顏色標籤
- SOLO (單人挑戰)：藍色 (#00f2ff)
- VERSUS (雙人對戰)：粉色 (#ff00c8)
- MIND (棋類智慧)：紫色 (#7000ff)
- ACTION (動作遊戲)：橙色 (#ffaa00)

### 現有功能檢查
- [x] 載入動畫
- [x] 響應式網格布局
- [x] 卡片懸浮效果
- [x] 繁體中文界面
- [ ] 黑暗/明亮模式切換
- [ ] 遊戲進度保存
- [ ] 無障礙鍵盤導航

---

*最後更新：2026-02-05*
*版本：1.0*