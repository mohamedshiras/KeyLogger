import os
from pynput import keyboard

# File setup
folder_path = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(folder_path, "my_keystrokes.txt")

def write_to_file(content):
    with open(log_file, "a") as f:
        f.write(content)

def on_press(key):
    try:
        # Record regular characters
        write_to_file(key.char)
    except AttributeError:
        # Handle special keys
        special_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
            keyboard.Key.tab: "\t"
        }
        write_to_file(special_keys.get(key, f" [{key}] "))

def on_activate_hkey():
    print("\n[STOP SIGNAL] Ctrl + Alt + C detected. Stopping...")
    # This will stop the listener
    main_listener.stop()

# Define the hotkey combination
hkey_combination = '<ctrl>+<alt>+c'

print(f"Recording... Saving to: {log_file}")
print(f"Press {hkey_combination} to stop recording.")

# We use two listeners: 
# 1. The Global Hotkey for the stop command
# 2. The standard Listener to record everything
with keyboard.GlobalHotKeys({hkey_combination: on_activate_hkey}) as hkey_listener:
    with keyboard.Listener(on_press=on_press) as main_listener:
        main_listener.join()