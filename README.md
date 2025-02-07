# 🖥️ Newegg SnipeBot 🎯
### 🚀 Auto-Buy RTX 5070, 5080, 5090 from Newegg Before They Sell Out!

Newegg SnipeBot is a **Python automation tool** that:
- Logs into **Newegg**
- Monitors stock for **RTX 5070, 5080, and 5090**
- Sends **instant notifications** via **Email & Discord**
- **Auto-adds the GPU to cart** and attempts checkout  
💥 **Never miss a drop again!**

---

## 📦 Features
✅ **Automated Stock Checking** – Checks availability every 30 seconds (configurable)  
✅ **Instant Alerts** – Sends **Discord & Email notifications** when a GPU is found  
✅ **Auto-Buy** – Adds to cart & proceeds to checkout  
✅ **Customizable** – Modify GPU selection, notification settings, and frequency  

---

## 🛠️ Setup & Installation

### 1️⃣ Install Dependencies
You'll need **Python 3.8+** and the required libraries. Run:
```
pip install selenium webdriver-manager smtplib requests
```

### 2️⃣ Install ChromeDriver
Newegg SnipeBot uses Selenium for automation.
Let webdriver-manager install the driver automatically:
```
python -c "from webdriver_manager.chrome import ChromeDriverManager; ChromeDriverManager().install()"
```
### 3️⃣ Configure Your Credentials
Edit snipebot.py and update:
```
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_email_password"
RECIPIENT_EMAIL = "recipient_email@example.com"
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"
```

### ⚠️ Important:

- Gmail Users: Use an App Password.
- Discord Webhook: Create one under Server Settings → Integrations.

### 🎯 Usage
## 🔹 Run the bot:
```
python snipebot.py
```
🔄 The script will loop until stock is found.

### 📝 Configuration Options
You can customize:
```
MONITOR_GPUS = ["5070", "5080", "5090"]  # Select which GPUs to track
CHECK_INTERVAL = 30  # Time between checks (in seconds)
```

### 🛑 Troubleshooting
## 🛠️ Selenium Errors?
- Ensure Chrome is installed.
- Try updating WebDriver:
```
pip install --upgrade webdriver-manager
```

## 📧 Email Issues?
- Check SMTP settings.
- Use an App Password for Gmail.

### 🏆 Future Features (Planned)
- 🚀 Support for Other Retailers (Amazon, Best Buy)
- ⚡ Telegram Notifications
🔄 Auto-Restart if Newegg Crashes

### 💙 Contributing
Want to improve Newegg SnipeBot? Feel free to submit a pull request or suggest features.

### ⚠️ Disclaimer
🛑 This script is for personal use only. Use responsibly and follow Newegg’s policies.

🔥 Happy Sniping!
