# 📸 Telegram to Google Drive Bot

This bot allows you to send photos via Telegram and automatically uploads them to your Google Drive, organized by date (`YYYY-MM-DD` format). **No temporary local disk storage is used.**

---

## ✅ Key Features

- Automatically receives photos from Telegram.
- Creates a daily folder in Google Drive.
- Directly uploads images without saving them on disk.
- Sends back a shareable link to the uploaded image.

---

## 🛠️ System Requirements

- Python 3.8 or higher  
- Google Drive account  
- Telegram Bot + Access Token  
- `credentials.json` file from Google API Console  

---

## 📦 Installation Guide

### 1. Create Project Directory and Virtual Environment
```bash
mkdir telegram-drive-bot
cd telegram-drive-bot
python -m venv venv

# Activate the environment:
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🤖 Create a Telegram Bot

1. Open Telegram and go to [@BotFather](https://t.me/BotFather)  
2. Type `/newbot` and follow the instructions to create a new bot  
3. BotFather will return an **Access Token**—save this to configure in `bot.py`

---

## 🔐 Create Google OAuth Credentials

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)  
2. Create a new Project → Go to **API & Services → Enable APIs & Services**  
3. Search for and enable **Google Drive API**  
4. Go to **Credentials → Create Credentials → OAuth Client ID**
   - **Application type**: Select "Desktop App"
5. Download the **`credentials.json`** file  
6. Place this file in your project root directory

---

## 🚀 First Run

```bash
python bot.py
```

- On first run, a browser window will open for Google account authentication.
- After authentication, a `token.json` file will be auto-generated to store access tokens.

👉 **Note:**  
If you are **running locally** (not deploying the bot), edit the following line in `drive_uploader.py`:
```python
creds = flow.run_console()
```
Change it to:
```python
creds = flow.run_local_server(port=0)
```
This makes authentication easier via your browser.

---

## 📁 Project Directory Structure

```
telegram-drive-bot/
├── bot.py              # Telegram Bot logic
├── drive_uploader.py   # Handles uploading images to Google Drive
├── credentials.json    # OAuth credentials from Google (downloaded)
├── token.json          # Google authentication token (generated after first run)
├── requirements.txt    # List of required Python libraries
└── README.md           # User guide
```

---

## ⚠️ Security Warning

- **Do not** commit `credentials.json` or `token.json` to GitHub or any public repository.
- If you see **WinError 32**, it may be because the image is open in another application—close it before sending.
- Ensure your bot has access to your Google Drive via the authenticated Google account.

---

## 🧩 Roadmap

- ✅ Add support for **videos**, **PDFs**
- ✅ Restrict photo upload permissions (admin-only)
- ✅ Build a **web dashboard** to manage images/videos

---

## 🖼️ Example UI

| Save Photo           | Save Video            |
|----------------------|----------------------|
| ![Photo saved to Drive](assets/anh.jpg) | ![Video saved to Drive](assets/video.jpg) |

---

## 📬 Contact

For support, please open an issue on the project's GitHub repository.
