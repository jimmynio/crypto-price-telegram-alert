import os
from binance.client import Client
from dotenv import load_dotenv
from pycoingecko import CoinGeckoAPI
from telegram import Bot

load_dotenv()

# API κλειδιά από το .env
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)
bot = Bot(token=TELEGRAM_TOKEN)

def get_btc_price_binance():
    ticker = client.get_symbol_ticker(symbol="BTCUSDT")
    return float(ticker['price'])

def get_kaspa_price_coingecko():
    cg = CoinGeckoAPI()
    price = cg.get_price(ids='kaspa', vs_currencies='usd')
    return float(price['kaspa']['usd'])

def send_telegram_alert(message):
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

if __name__ == "__main__":
    btc_price = get_btc_price_binance()
    kas_price = get_kaspa_price_coingecko()
    print(f"Τρέχουσα τιμή BTC/USDT: {btc_price}")
    print(f"Τρέχουσα τιμή KAS/USDT: {kas_price}")

    # Παράδειγμα: στέλνεις alert στο Telegram
    alert_msg = f"Τρέχουσες τιμές:\nBTC/USDT: {btc_price}\nKAS/USDT: {kas_price}"
    send_telegram_alert(alert_msg)
    print("Alert στάλθηκε στο Telegram!")
