cx = x + 16
cy = y + 16

# LED Bulb Dome & Sides
oled.line_noupdate(cx - 3, cy - 8, cx + 3, cy - 8, 1)  # Top curve
oled.line_noupdate(cx - 5, cy - 5, cx - 3, cy - 8, 1)  # Top-left slope
oled.line_noupdate(cx + 5, cy - 5, cx + 3, cy - 8, 1)  # Top-right slope
oled.line_noupdate(cx - 5, cy - 5, cx - 5, cy - 1, 1)  # Left side
oled.line_noupdate(cx + 5, cy - 5, cx + 5, cy - 1, 1)  # Right side

# LED Collar / Rim
oled.line_noupdate(cx - 7, cy - 1, cx + 7, cy - 1, 1)  # Top rim line
oled.line_noupdate(cx - 7, cy - 1, cx - 7, cy + 1, 1)  # Left rim edge
oled.line_noupdate(cx + 7, cy - 1, cx + 7, cy + 1, 1)  # Right rim edge
oled.line_noupdate(cx - 7, cy + 1, cx + 7, cy + 1, 1)  # Bottom rim line

# LED Pins / Leads (Anode longer on left, Cathode shorter on right)
oled.line_noupdate(cx - 3, cy + 1, cx - 3, cy + 9, 1)  # Left lead (longer)
oled.line_noupdate(cx + 3, cy + 1, cx + 3, cy + 7, 1)  # Right lead (shorter)

# Emitted Light Rays
oled.line_noupdate(cx - 7, cy - 7, cx - 10, cy - 10, 1)  # Top-left ray
oled.line_noupdate(cx + 7, cy - 7, cx + 10, cy - 10, 1)  # Top-right ray
oled.line_noupdate(cx - 8, cy - 4, cx - 11, cy - 4, 1)   # Left ray
oled.line_noupdate(cx + 8, cy - 4, cx + 11, cy - 4, 1)   # Right ray

# Outer Border
oled.rect_noupdate(x + 2, y + 2, 28, 28, 1)