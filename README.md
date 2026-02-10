# 🕵️‍♂️ Python Cloud Keylogger (Educational)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Discord](https://img.shields.io/badge/Discord-Webhook-5865F2?style=for-the-badge&logo=discord)
![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)

A stealthy, Python-based system monitoring tool designed for educational purposes and security research.  
This agent captures keystrokes in real-time, batches the data using threaded timers, and securely synchronizes logs to a private Discord server via Webhooks.

> **⚠️ DISCLAIMER:**  
> This software is developed strictly for **educational purposes** to demonstrate system monitoring techniques, background process handling, and cloud API integration.  
> The author allows usage only on authorized systems. **Malicious use is prohibited.**

---

## ✨ Features

- **☁️ Cloud Synchronization:** Uploads log files directly to a private Discord channel using Webhooks (serverless).
- **⏱️ Smart Batching:** Uses a threaded timer to collect data in memory and upload every **60 seconds** to prevent network spam.
- **⌨️ Clean Logging:** Automatically processes `Backspace` and special keys to ensure output logs are readable.
- **🚀 Zero-Config Auth:** No complex OAuth, client secrets, or local credentials required.
- **👻 Stealth Mode:** Can be compiled into a single-file executable (`.exe`) that runs silently in the background.

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Libraries:**  
  - `pynput` – input monitoring  
  - `requests` – HTTP transmissions  
  - `threading` – asynchronous operations  
  - `os` – file handling  
- **Infrastructure:** Discord Webhooks (data storage)

---

## ⚙️ Installation & Setup

### 1. Prerequisites

Ensure you have Python installed. Then install the required dependencies:

```bash
pip install pynput requests
```

### 2. Configuration

Open `logger.py` and update the settings at the top of the file:

```python
# --- SETTINGS ---
WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL_HERE"  # Paste your webhook URL
INTERVAL = 60  # Time in seconds between uploads
```

### 3. Creating the Webhook

1. Create a private Discord server.
2. Go to **Server Settings → Integrations → Webhooks**.
3. Click **New Webhook**, copy the **Webhook URL**, and paste it into the script.

---

## 🚀 Usage

### Running via Python

Simply run the script in your terminal:

```bash
python logger.py
```

- Type anywhere on your computer.
- After 60 seconds (or upon pressing Enter), a `.txt` file will appear in your Discord channel.

### Building the Executable (Windows)

To compile this into a standalone `.exe` that runs without a console window:

1. Install PyInstaller:

```bash
pip install pyinstaller
```

2. Run the build command:

```bash
pyinstaller --noconsole --onefile --icon=app_icon.ico logger.py
```

The final application will be available in the `dist` folder.

---

## 📝 License

This project is open-source and available under the GNU General Public License v3.0 (GPL-3.0).
See the [LICENSE](LICENSE) file for full license details.

---

<div align="center">
<b>Developed by <a href="https://www.mohamedshiras.dev">Mohamed Shiras</a></b><br/>
<i>Student @ NIBM | Undergraduate</i>
</div>
