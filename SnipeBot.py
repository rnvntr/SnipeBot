from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import smtplib
import requests
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# ---------------------- SNIPEBOT METADATA ---------------------- #
SCRIPT_NAME = "SnipeBot"
AUTHOR_NAME = "rnvntr"
VERSION = "1.0.0"

# ---------------------- CONFIGURATION ---------------------- #
# Newegg Login Credentials
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

# GPUs to Track
MONITOR_GPUS = ["5070", "5080", "5090"]  # Choose which GPUs to track

# How often to check (in seconds)
CHECK_INTERVAL = 30  

# Email Notification Settings
SMTP_SERVER = "smtp.gmail.com"  # Change for Outlook/Yahoo (e.g., "smtp.office365.com")
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"
SENDER_PASSWORD = "your_email_password"  # Use App Password if needed
RECIPIENT_EMAIL = "recipient_email@example.com"

# Discord Webhook
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/your_webhook_url"

# Newegg URLs (Replace with actual links)
GPU_URLS = {
    "5070": "https://www.newegg.com/p/N82E16814137788",
    "5080": "https://www.newegg.com/p/N82E16814137789",
    "5090": "https://www.newegg.com/p/N82E16814137790",
}

# ---------------------- SETUP SELENIUM ---------------------- #
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Run in background
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--window-size=1920,1080")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# ---------------------- FUNCTIONS ---------------------- #
def send_email_notification(gpu, url):
    """Sends an email notification when a GPU is in stock."""
    subject = f"🚨 {gpu} is IN STOCK at Newegg!"
    body = f"The {gpu} is available. Order now: {url}"

    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECIPIENT_EMAIL
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print(f"[📧] Email notification sent for {gpu}!")
    except Exception as e:
        print(f"[✘] Email notification failed: {e}")

def send_discord_notification(gpu, url):
    """Sends a Discord webhook notification when a GPU is in stock."""
    message = {
        "content": f"🚨 **{gpu} is in stock!** Order now: {url}"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=message)
        print(f"[🎮] Discord notification sent for {gpu}!")
    except Exception as e:
        print(f"[✘] Discord notification failed: {e}")

def login_newegg():
    """Logs into Newegg account"""
    driver.get("https://www.newegg.com/")
    time.sleep(3)

    try:
        sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in / Register")
        sign_in_button.click()
        time.sleep(2)

        email_field = driver.find_element(By.ID, "labeled-input-signEmail")
        email_field.send_keys(EMAIL)
        driver.find_element(By.ID, "signInSubmit").click()
        time.sleep(2)

        password_field = driver.find_element(By.ID, "labeled-input-password")
        password_field.send_keys(PASSWORD)
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        print("[✔] Successfully logged in!")

    except Exception as e:
        print(f"[✘] Login failed: {e}")
        driver.quit()

def check_stock():
    """Checks for stock availability of selected GPUs"""
    while True:
        for gpu, url in GPU_URLS.items():
            if gpu in MONITOR_GPUS:
                driver.get(url)
                time.sleep(2)

                try:
                    add_to_cart = driver.find_element(By.XPATH, "//button[contains(text(), 'Add to cart')]")
                    add_to_cart.click()
                    print(f"[✔] {gpu} in stock! Added to cart.")
                    
                    # Send notifications
                    send_email_notification(gpu, url)
                    send_discord_notification(gpu, url)

                    checkout()
                    return  # Exit loop after adding to cart
                except:
                    print(f"[✘] {gpu} is out of stock. Checking again in {CHECK_INTERVAL} seconds.")

        time.sleep(CHECK_INTERVAL)

def checkout():
    """Proceeds to checkout after adding item to cart"""
    driver.get("https://secure.newegg.com/shop/cart")
    time.sleep(2)

    try:
        checkout_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Secure Checkout')]")
        checkout_button.click()
        time.sleep(2)

        place_order = driver.find_element(By.XPATH, "//button[contains(text(), 'Place Order')]")
        place_order.click()
        print("[✔] Order placed successfully!")
        driver.quit()

    except Exception as e:
        print(f"[✘] Checkout failed: {e}")
        driver.quit()

# ---------------------- MAIN EXECUTION ---------------------- #
if __name__ == "__main__":
    login_newegg()
    check_stock()
