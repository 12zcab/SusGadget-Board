cx = x + 16
cy = y + 16

# --- 按鍵立體外框 (Keycap Outer Base) ---
oled.rect_noupdate(cx - 10, cy - 10, 20, 18, 1)  # 鍵帽底部外輪廓

# --- 按鍵內凹/表面框 (Keycap Top Surface) ---
# 繪製稍微往內縮且偏上的內框，營造鍵帽斜面的立體視覺
oled.rect_noupdate(cx - 8, cy - 8, 16, 13, 1)   # 鍵帽頂部表面

# --- 連接內外框的斜角線 (3D Edges) ---
oled.line_noupdate(cx - 10, cy - 10, cx - 8, cy - 8, 1)  # 左上斜角
oled.line_noupdate(cx + 9, cy - 10, cx + 7, cy - 8, 1)   # 右上斜角
oled.line_noupdate(cx - 10, cy + 7, cx - 8, cy + 4, 1)   # 左下斜角
oled.line_noupdate(cx + 9, cy + 7, cx + 7, cy + 4, 1)    # 右下斜角

# --- "Esc" 字母圖案 (手繪微型字體，置中偏上) ---
# 字母 'E'
oled.line_noupdate(cx - 6, cy - 5, cx - 4, cy - 5, 1)    # 頂橫
oled.line_noupdate(cx - 6, cy - 3, cx - 5, cy - 3, 1)    # 中橫
oled.line_noupdate(cx - 6, cy - 1, cx - 4, cy - 1, 1)    # 底橫
oled.line_noupdate(cx - 6, cy - 5, cx - 6, cy - 1, 1)    # 左豎

# 字母 's'
oled.line_noupdate(cx - 2, cy - 5, cx, cy - 5, 1)        # 頂橫
oled.line_noupdate(cx - 2, cy - 3, cx, cy - 3, 1)        # 中橫
oled.line_noupdate(cx - 2, cy - 1, cx, cy - 1, 1)        # 底橫
oled.line_noupdate(cx - 2, cy - 5, cx - 2, cy - 3, 1)    # 左上豎
oled.line_noupdate(cx, cy - 3, cx, cy - 1, 1)            # 右下豎

# 字母 'c'
oled.line_noupdate(cx + 2, cy - 5, cx + 4, cy - 5, 1)    # 頂橫
oled.line_noupdate(cx + 2, cy - 1, cx + 4, cy - 1, 1)    # 底橫
oled.line_noupdate(cx + 2, cy - 5, cx + 2, cy - 1, 1)    # 左豎

# --- 原本的外邊框 (Outer Border - 保持不變) ---
oled.rect_noupdate(x + 2, y + 2, 28, 28, 1)
