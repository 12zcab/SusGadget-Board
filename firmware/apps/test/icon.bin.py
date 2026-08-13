cx = x + 16
cy = y + 16
oled.line_noupdate(cx - 6, cy - 6, cx - 6, cy - 2, 1)
oled.line_noupdate(cx + 6, cy - 6, cx + 6, cy - 2, 1)
oled.line_noupdate(cx - 8, cy + 3, cx - 4, cy + 7, 1)
oled.line_noupdate(cx - 4, cy + 7, cx + 4, cy + 7, 1)
oled.line_noupdate(cx + 4, cy + 7, cx + 8, cy + 3, 1)
oled.line_noupdate(cx - 10, cy, cx - 8, cy, 1)
oled.line_noupdate(cx + 8, cy, cx + 10, cy, 1)
oled.rect_noupdate(x + 2, y + 2, 28, 28, 1)