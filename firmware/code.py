import os
import sys

for path in ["/interface"]:
    if path not in sys.path:
        sys.path.append(path)
try:
    os.listdir("/interface")
except OSError:
    print("[Error] /interface folder missing!")

apps_dir_content = os.listdir("/apps")
for item in apps_dir_content:
    path = f"/apps/{item}"
    try:
        is_dir = (os.stat(path)[0] & 0x4000) != 0
    except OSError:
        continue
        
    if is_dir:
        sub_files = os.listdir(path)
        init_file = None
        for f in ["__init__.py", "__init__.mpy", "init.py", "init.mpy"]:
            if f in sub_files:
                init_file = f
                break

        if init_file:
            try:
                target_script = f"{path}/{init_file}"
                print(f"[Apps] Launching script: {item}/{init_file}")
                if path not in sys.path:
                    sys.path.append(path)
                with open(target_script, "r") as f:
                    script_code = f.read()
                app_globals = {
                    "__name__": "__main__",
                    "__file__": target_script,
                    "__path__": path
                }
                exec(script_code, app_globals)
                sys.path.remove(path)
                print(f"[Apps] Finished: {item}")
            except Exception as e:
                print(f"[Apps] Failed to Launch {item}: {e}")
                if path in sys.path:
                    sys.path.remove(path)
        else:
            print(f"[Apps] Skipped: {item} (init file not found)")

print("Code.py Finished")
