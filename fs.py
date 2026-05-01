import time
from FunPayAPI.account import Account
from FunPayAPI.updater.runner import Runner
import telebot


GOLDEN_KEY = "2r5uxkr7l5sb8zog5eu6ow1vclqu5sqt"  
TELEGRAM_TOKEN = "8779737904:AAFYY1ONJz86lfrZWbeoVYP2HwvxpLIqBos"
TELEGRAM_CHAT_ID = "5549863719"

account = Account(GOLDEN_KEY)

account.headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ascii",
    "Accept-Language": "en-US,en;q=0.9"
}
account.get()

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def send_telegram_message(text):
    try:
        bot.send_message(TELEGRAM_CHAT_ID, text)
    except:
        pass

runner = Runner(account)

def run_funpay_listener():
    while True:
        try:
            for event in runner.listen(requests_delay=4):
                send_telegram_message("New event detected!")
        except KeyboardInterrupt:
            break
        except:
            time.sleep(2)

if name == "main":
    run_funpay_listener()