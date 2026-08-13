import board
import bitbangio
import digitalio
import adafruit_ssd1306

global oled

def init_screen(rotation=2):
    global oled
    scl_pin = digitalio.DigitalInOut(board.IO2)
    scl_pin.switch_to_input(pull=digitalio.Pull.UP)
    sda_pin = digitalio.DigitalInOut(board.IO1)
    sda_pin.switch_to_input(pull=digitalio.Pull.UP)
    scl_pin.deinit()
    sda_pin.deinit()
    i2c = bitbangio.I2C(scl=board.IO2, sda=board.IO1)
    WIDTH = 128
    HEIGHT = 32
    oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)
    oled.rotation = rotation
    oled.fill(0)
    oled.show()
    print("Oled Initialized")
    return True

def text(txt, x, y):
    global oled
    oled.text(txt, x, y, 1)
    oled.show()
    return True

def clear():
    global oled
    oled.fill(0)
    oled.show()
    return True

def clear_noupdate():
    global oled
    oled.fill(0)
    return True

def draw_cached_pixels_noupdate(pixel_matrix, x, y):
    global oled
    start_row = 0
    end_row = 32
    start_col = 0
    end_col = 32

    # 確保不會超出螢幕 32x128 的範圍
    if y < 0:
        start_row = -y
    if y + 32 > 32:
        end_row = 32 - y
    if x < 0:
        start_col = -x
    if x + 32 > 128:
        end_col = 128 - x

    for row in range(start_row, end_row):
        pixel_y = y + row
        row_data = pixel_matrix[row]
        for col in range(start_col, end_col):
            pixel_x = x + col
            oled.pixel(pixel_x, pixel_y, row_data[col])
    return True

def draw_bin_file(file_path, src_w, src_h, dest_x, dest_y):
    """
    讀取二進制圖標檔案並直接繪製到 OLED 螢幕上。
    基於代碼 1 的 32x32 (4位元組寬) 解析邏輯，並調用代碼 2 的繪製與 show 刷新螢幕。
    """
    # 1. 讀取並解析二進制檔案 (來自代碼 1)
    with open(file_path, "rb") as f:
        raw_bytes = f.read()
    
    w_bytes = 4  # 32 像素 / 8 位元 = 4 位元組
    pixel_list = []
    for row in range(32):
        row_pixels = []
        for col_byte in range(w_bytes):
            idx = row * w_bytes + col_byte
            current_byte = raw_bytes[idx] if idx < len(raw_bytes) else 0
            for bit in range(8):
                row_pixels.append((current_byte >> (7 - bit)) & 0x01)
        pixel_list.append(row_pixels)
    
    # 2. 呼叫現有的緩衝繪製函數 (來自代碼 2)
    draw_cached_pixels_noupdate(pixel_list, dest_x, dest_y)
    
    # 3. 根據代碼 3 的預期行為，更新螢幕以顯示圖像
    show()
    return True

def rect_noupdate(x, y, w, h, c,f = False):
    global oled
    if (f == False):
        oled.rect(x, y, w, h, c)
    else:
        oled.fill_rect(x, y, w, h, c)
    return True

def show():
    global oled
    oled.show()
    return True

def line_noupdate(x1,y1,x2,y2,c):
    global oled
    oled.line(x1, y1, x2, y2, c)
    return True

init_screen()
