import sys
import board
import digitalio
import re
def run_independent_app(app_path):
    print(f"[Launcher] Preparing Line-by-Line Sandbox (With Direct _end_ Check) for: {app_path}")
    
    try:
        with open(app_path, "r") as f:
            raw_code = f.read()
    except Exception:
        print(f"[Launcher] Error: Cannot find app at {app_path}")
        return

    function_text_injection = """
import board, digitalio, sys

def _Launcher_check_():
    try:
        with digitalio.DigitalInOut(board.IO0) as btn:
            btn.direction = digitalio.Direction.INPUT
            btn.pull = digitalio.Pull.UP
            if not btn.value:
                print("\\n[Launcher Check] Escape Button detected!")
                try:
                    if '_end_' in globals() or '_end_' in locals():
                        print("[Launcher Check] Directly calling App native _end_()...")
                        globals().get('_end_', locals().get('_end_'))()
                except Exception as ce:
                    print("[Launcher Check] App _end_() execution failed:", ce)
                raise KeyboardInterrupt("App terminated after direct end() call")
    except KeyboardInterrupt:
        raise
    except Exception:
        pass
"""

    loop_pattern = re.compile(r'^([ \t]*)(while|for)\s+(.+):')

    lines = raw_code.split('\n')
    modified_lines = []

    for line in lines:
        modified_lines.append(line)
        match = loop_pattern.match(line)
        if match:
            indent = match.group(1)
            modified_lines.append(f"{indent}    _Launcher_check_()")

    modified_code = '\n'.join(modified_lines)
    final_executable_code = function_text_injection + "\n" + modified_code

    print("[Launcher] Direct end() Call Injection Result:")
    print("----------------------------------------")
    print(final_executable_code)
    print("----------------------------------------")

    app_folder = "/".join(app_path.split("/")[:-1])
    if app_folder == "":
        app_folder = "/"

    if "/interface" not in sys.path:
        sys.path.append("/interface")

    path_was_added = False
    if app_folder not in sys.path:
        sys.path.insert(0, app_folder)
        path_was_added = True

    app_globals = {
        "__name__": "__main__",
        "__file__": app_path,
        "__path__": app_folder
    }

    try:
        exec(final_executable_code, app_globals)
        print("[Launcher] App finished execution naturally.")
    except KeyboardInterrupt:
        print("[Launcher] App successfully destroyed after direct exit cleanup.")
    except Exception as e:
        print(f"[Launcher] App crashed with error: {e}")
    finally:
        if path_was_added and app_folder in sys.path:
            sys.path.remove(app_folder)
            
        for key in list(sys.modules.keys()):
            try:
                mod = sys.modules[key]
                if hasattr(mod, '__file__') and mod.__file__ and app_folder in mod.__file__:
                    del sys.modules[key]
            except Exception:
                pass
                
        app_globals.clear()
        print("[Launcher] Sandbox cleaned. Back to launch.py GUI.\n")
