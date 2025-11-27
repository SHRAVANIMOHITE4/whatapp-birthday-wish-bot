import pyautogui
import time
import json
from datetime import datetime
import webbrowser

def send_birthday_message(name, message):
    try:
        print(f"\n📝 Typing message for {name} in 5 seconds...")
        print("➡️ Move your mouse into the Instagram message box NOW!")
        time.sleep(5)

        # Type and send
        pyautogui.write(message, interval=0.05)
        pyautogui.press("enter")
        print(f"✅ Message sent to {name}")
        time.sleep(2)

    except Exception as e:
        print(f"❌ Failed to send to {name}: {e}")

def open_instagram():
    webbrowser.open("https://www.instagram.com/direct/inbox/")
    print("🌐 Opening Instagram Direct Messages...")
    time.sleep(10)  # Wait for browser to fully open

def send_all_birthday_wishes(birthday_file):
    # Load the birthday list
    with open(birthday_file, 'r') as file:
        data = json.load(file)

    # Get today's date
    today = datetime.now().strftime("%m-%d")

    open_instagram()
    input("📌 After Instagram opens, click the FIRST contact's message box, then press Enter here...")

    # Loop through contacts
    for contact in data["contacts"]:
        if contact["date"][5:] == today:
            name = contact["name"]
            message = f"🎉 Happy Birthday, {name}! Wishing you a fantastic year ahead! 🥳"
            send_birthday_message(name, message)
            input("👉 Now click the NEXT contact manually, then press Enter to continue...")

    print("🎉 All birthday messages sent!")

# 🚀 Run the bot
send_all_birthday_wishes(
    birthday_file=r"C:\Users\SHRAVANI\Desktop\instagram bot\birth_day.json"
)
