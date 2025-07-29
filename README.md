# 💸 Crypto Price Telegram Alert

A simple Python script that fetches the latest crypto prices (BTC/USDT, etc.) and sends automated price alerts to your Telegram via bot.

## 🚀 Features
- Fetches live crypto prices from Binance
- Sends real-time alerts directly to Telegram
- Easy setup with `.env` file (API keys, bot token, chat ID)
- Modular and ready for further customization

## 📦 Requirements

- Python 3.8+
- Binance Python API (`python-binance`)
- `python-dotenv`
- `python-telegram-bot`
- Telegram Bot (via @BotFather)

Install requirements:
```bash
pip install -r requirements.txt

⚙️ Setup
Clone the repo

bash
Copy
Edit
git clone https://github.com/jimmynio/crypto-price-telegram-alert.git
cd crypto-price-telegram-alert

Create a .env file in the project directory with:

ini
Copy
Edit
BINANCE_API_KEY=your_binance_key
BINANCE_API_SECRET=your_binance_secret
TELEGRAM_TOKEN=your_telegram_bot_token
TELEGRAM_CHAT_ID=your_chat_id

Run the script

bash
Copy
Edit
python price_logger.py

Notes
Never share your .env file or API keys publicly.

Edit the script to add more coins or customize alerts.

🧑‍💻 Author
Dimitris Seriatos (jimmynio)

📝 License
MIT
