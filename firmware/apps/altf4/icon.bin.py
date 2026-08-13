cx = x + 16
cy = y + 16

# ==================== 左鍵帽：Alt ====================
# 外框與內框
oled.rect_noupdate(cx - 11, cy - 7, 10, 14, 1)  # 外框
oled.rect_noupdate(cx - 10, cy - 6, 8, 11, 1)   # 內框面

# 手繪文字 "Alt" (稍微簡化以放入 6 像素寬度)
oled.line_noupdate(cx - 9, cy - 3, cx - 9, cy + 1, 1)   # A 左豎
oled.line_noupdate(cx - 7, cy - 3, cx - 7, cy + 1, 1)   # A 右豎
oled.line_noupdate(cx - 9, cy - 3, cx - 7, cy - 3, 1)   # A 頂橫
oled.line_noupdate(cx - 9, cy - 1, cx - 7, cy - 1, 1)   # A 中橫

oled.line_noupdate(cx - 5, cy - 3, cx - 5, cy + 2, 1)   # l 豎線

oled.line_noupdate(cx - 4, cy - 3, cx - 2, cy - 3, 1)   # t 頂橫
oled.line_noupdate(cx - 3, cy - 3, cx - 3, cy + 2, 1)   # t 豎線

# ==================== 右鍵帽：F4 ====================
# 外框與內框
oled.rect_noupdate(cx + 1, cy - 7, 10, 14, 1)   # 外框
oled.rect_noupdate(cx + 2, cy - 6, 8, 11, 1)    # 內框面

# 手繪文字 "F4"
oled.line_noupdate(cx + 3, cy - 3, cx + 3, cy + 2, 1)   # F 左豎
oled.line_noupdate(cx + 3, cy - 3, cx + 5, cy - 3, 1)   # F 頂橫
oled.line_noupdate(cx + 3, cy - 1, cx + 4, cy - 1, 1)   # F 中橫

oled.line_noupdate(cx + 7, cy - 3, cx + 7, cy, 1)       # 4 左半豎
oled.line_noupdate(cx + 7, cy, cx + 9, cy, 1)           # 4 中橫
oled.line_noupdate(cx + 9, cy - 3, cx + 9, cy + 2, 1)   # 4 右長豎

# ==================== 連接兩鍵的加號 ====================
oled.line_noupdate(cx - 1, cy - 1, cx + 1, cy - 1, 1)   # + 橫
oled.line_noupdate(cx, cy - 2, cx, cy, 1)               # + 豎

# --- 原本的外邊框 (保持不變) ---
oled.rect_noupdate(x + 2, y + 2, 28, 28, 1)
