import keyboard
import time
import atexit

def block_all_keys():
    """Blocks all keyboard input."""
    print("Keyboard input is disabled. Close this script to re-enable it.")

    # Generate a comprehensive list of keys
    blocked_keys = list(keyboard.all_modifiers)  # Modifier keys
    blocked_keys += [f"f{i}" for i in range(1, 13)]  # F1-F12 keys
    blocked_keys += [f"numpad {i}" for i in range(10)]  # Numpad keys 0-9
    blocked_keys += ["numpad .", "numpad /", "numpad *", "numpad -", "numpad +", "numpad enter"]
    blocked_keys += ["windows", "apps", "print screen", "scroll lock", "pause"]  # Special keys
    blocked_keys += ["insert", "home", "page up", "delete", "end", "page down"]  # Navigation keys
    blocked_keys += ["up", "down", "left", "right"]  # Arrow keys

    # Include ASCII keys (letters, numbers, and symbols)
    for i in range(256):
        try:
            if keyboard.key_to_scan_codes(chr(i)):
                blocked_keys.append(chr(i))
        except ValueError:
            pass  # Skip invalid keys

    # Block each key
    for key in blocked_keys:
        try:
            keyboard.block_key(key)
        except ValueError:
            pass  # Some keys may still not be valid

    # Ensure keys are unblocked on exit
    def cleanup():
        for key in blocked_keys:
            try:
                keyboard.unblock_key(key)
            except ValueError:
                pass  # Ignore errors for invalid keys
        print("Keyboard input re-enabled.")

    atexit.register(cleanup)

    # Keep script running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Script stopped.")

if __name__ == "__main__":
    block_all_keys()
