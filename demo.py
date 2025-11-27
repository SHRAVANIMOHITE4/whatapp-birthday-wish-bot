import pywhatkit as kit
import pyautogui
import json
import time
from datetime import datetime

def send_whatsapp_message_now(phone_number, message):
    try:
        # Optional delay to avoid any race conditions
        time.sleep(2)

        # Increase wait_time to give enough time for WhatsApp Web to load
        kit.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)

        time.sleep(3)  # Wait until message box is fully ready
        pyautogui.press("enter")

        print(f"✅ Message sent to {phone_number}")
    except Exception as e:
        print("❌ Error occurred:", e)


def send_birthday_wishes(birthday_file):
    with open(birthday_file, 'r') as file:
        data = json.load(file)

    today = datetime.now()
    today_month_day = today.strftime("%m-%d")

    for contact in data['contacts']:
        birthday_month_day = contact['date'][5:]
        if birthday_month_day == today_month_day:
            name = contact['name']
            phone = contact['phone']
            message = f"Happy Birthday, {name}! 🎉 Wishing you a wonderful day filled with joy!"
            send_whatsapp_message_now(phone, message)

# Call the function with your file
send_birthday_wishes(r'C:\Users\SHRAVANI\Desktop\whatsapp bot\birthdays.json')
