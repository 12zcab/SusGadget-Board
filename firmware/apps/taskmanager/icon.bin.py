cx = x + 16
cy = y + 16

# --- 工作管理員視窗外框 ---
oled.rect_noupdate(cx - 10, cy - 9, 20, 17, 1)  # 主視窗
oled.line_noupdate(cx - 10, cy - 6, cx + 9, cy - 6, 1)  # 視窗標題列分隔線

# --- 右上角縮小/放大/關閉按鈕意象 ---
oled.line_noupdate(cx + 4, cy - 8, cx + 5, cy - 8, 1)  # 最小化
oled.rect_noupdate(cx + 7, cy - 8, 2, 2, 1)            # 關閉 X

# --- 效能折線圖 (心電圖/脈搏線) ---
oled.line_noupdate(cx - 8, cy + 2, cx - 5, cy + 2, 1)  # 起始平線
oled.line_noupdate(cx - 5, cy + 2, cx - 3, cy - 3, 1)  # 往上衝
oled.line_noupdate(cx - 3, cy - 3, cx - 1, cy + 5, 1)  # 往下掉
oled.line_noupdate(cx - 1, cy + 5, cx + 2, cy - 1, 1)  # 往上回彈
oled.line_noupdate(cx + 2, cy - 1, cx + 4, cy + 2, 1)  # 回到中線
oled.line_noupdate(cx + 4, cy + 2, cx + 7, cy + 2, 1)  # 結束平線

# --- 底部的數據裝飾線 (模擬文字/條狀圖) ---
oled.line_noupdate(cx - 7, cy + 5, cx - 4, cy + 5, 1)
oled.line_noupdate(cx - 7, cy + 7, cx - 2, cy + 7, 1)

# --- 原本的外邊框 (保持不變) ---
oled.rect_noupdate(x + 2, y + 2, 28, 28, 1)
