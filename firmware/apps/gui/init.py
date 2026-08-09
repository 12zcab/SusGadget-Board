import oled
import board, digitalio, sys
import launcher
import json, joystick, time, os

cached_apps = []

def load_config():
    with open("config.json", "r") as file:
        return json.load(file)

def save_config(config):
    with open("config.json", "w") as file:
        json.dump(config, file, indent=4)

def return_app_paths():
    paths = []
    apps_dir_content = os.listdir("/apps")
    for item in apps_dir_content:
        path = f"/apps/{item}"
        try:
            is_dir = (os.stat(path)[0] & 0x4000) != 0
        except OSError:
            continue
        if is_dir:
            sub_files = os.listdir(path)
            app_file = None
            for f in ["__app__.py", "__app__.mpy", "app.py", "app.mpy"]:
                if f in sub_files:
                    app_file = f
                    break
            if app_file:
                paths.append([path, app_file])
    return paths

def cache_apps_and_icons():
    global cached_apps
    cached_apps = []
    raw_paths = return_app_paths()
    for path, init_file in raw_paths:
        icon_bin_path = f"{path}/icon.bin"
        icon_py_path = f"{path}/icon.bin.py"
        
        icon_type = "none"
        icon_data = None
        
        try:
            with open(icon_bin_path, "rb") as f:
                raw_bytes = f.read()
            w_bytes = 4
            pixel_list = []
            for row in range(32):
                row_pixels = []
                for col_byte in range(w_bytes):
                    idx = row * w_bytes + col_byte
                    current_byte = raw_bytes[idx] if idx < len(raw_bytes) else 0
                    for bit in range(8):
                        row_pixels.append((current_byte >> (7 - bit)) & 0x01)
                pixel_list.append(row_pixels)
            icon_type = "bin"
            icon_data = pixel_list
        except OSError:
            try:
                with open(icon_py_path, "r") as f:
                    py_code = f.read()
                icon_type = "py"
                icon_data = compile(py_code, icon_py_path, "exec")
            except OSError:
                icon_type = "none"
                icon_data = [0 * 32 for _ in range(32)]
                
        cached_apps.append({
            "path": path,
            "init_file": init_file,
            "icon_type": icon_type,
            "icon_data": icon_data
        })

def init():
    oled.clear()
    cache_apps_and_icons()
    loop()

def loop():
    input_enabled = 1
    cursor_pos_x, cursor_pos_y = 16, 16
    cursor_mapped_x, cursor_mapped_y = 2, 1
    move_cursor_pos_x, move_cursor_pos_y = 16, 16
    while True:
        oled.clear_noupdate()
        if input_enabled == 1:
            joy_in = joystick.read()
            if joy_in[0] == False:
                print("Up")
                move_cursor_pos_y -= 32
                input_enabled = 0
            if joy_in[2] == False:
                print("Left")
                move_cursor_pos_x -= 32
                input_enabled = 0
            if joy_in[1] == False:
                print("Down")
                move_cursor_pos_y += 32
                input_enabled = 0
            if joy_in[3] == False:
                print("Right")
                move_cursor_pos_x += 32
                input_enabled = 0
        if move_cursor_pos_x < 16:
            move_cursor_pos_x = 16
        if move_cursor_pos_y < 16:
            move_cursor_pos_y = 16
        if move_cursor_pos_x > cursor_pos_x:
            cursor_pos_x += 8
            print(cursor_pos_x)
        if move_cursor_pos_x < cursor_pos_x:
            cursor_pos_x -= 8
            print(cursor_pos_x)
        if move_cursor_pos_y > cursor_pos_y:
            cursor_pos_y += 8
            print(cursor_pos_y)
        if move_cursor_pos_y < cursor_pos_y:
            cursor_pos_y -= 8
            print(cursor_pos_y)
        if move_cursor_pos_y == cursor_pos_y:
            if move_cursor_pos_x == cursor_pos_x:
                input_enabled = 1
        cursor_mapped_x = cursor_pos_x // 32
        cursor_mapped_y = cursor_pos_y // 32
        drawx = 0
        drawy = 0
        for app in cached_apps:
            icon_x = drawx * 32 - cursor_pos_x + 64
            icon_y = drawy * 32 - cursor_pos_y + 16
            if icon_x > -32 and icon_x < 128 and icon_y > -32 and icon_y < 32:
                if app["icon_type"] == "bin":
                    oled.draw_cached_pixels_noupdate(app["icon_data"], icon_x, icon_y)
                elif app["icon_type"] == "py":
                    context = {"oled": oled, "x": icon_x, "y": icon_y}
                    try:
                        exec(app["icon_data"], context)
                    except Exception as e:
                        print("Icon script error:", e)
                else:
                    oled.rect_noupdate(icon_x + 2, icon_y + 2, 28, 28, 1)
                
                if drawx == cursor_mapped_x:
                    if drawy == cursor_mapped_y:
                        oled.rect_noupdate(icon_x, icon_y, 32, 32, 1)
                        if input_enabled == 1:
                            if joystick.read()[4] == False:
                                launcher.run_independent_app(f"{app['path']}/{app['init_file']}")
            drawx += 1
            if drawx == 7:
                drawx = 0
                drawy += 1
        oled.show()

init()
