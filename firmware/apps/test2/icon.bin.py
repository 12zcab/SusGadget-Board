cx = x + 16
cy = y + 16
oled.line_noupdate(cx, cy - 15, cx + 9, cy + 12, 1)
oled.line_noupdate(cx + 9, cy + 12, cx - 14, cy - 5, 1)
oled.line_noupdate(cx - 14, cy - 5, cx + 14, cy - 5, 1)
oled.line_noupdate(cx + 14, cy - 5, cx - 9, cy +12, 1)
oled.line_noupdate(cx - 9, cy +12, cx, cy - 15, 1)
oled.rect_noupdate(x + 2, y + 2, 28, 28, 1)