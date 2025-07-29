# Crypto Price Logger & Telegram Alert 🚀

A simple Python script that fetches real-time cryptocurrency prices (BTC/ETH), logs data to CSV, and sends Telegram alerts if prices hit custom thresholds.

- 📈 Real-time price tracking via public API (CoinGecko)
- 📊 Automatic logging to CSV (for data analysis)
- 💬 Instant Telegram alerts (Bot API integration)
- 🕒 Runs periodically via cronjob or Task Scheduler

## Setup

1. Clone this repo
2. Install dependencies:
    pip install -r requirements.txt
3. Add your Telegram Bot Token & Chat ID to `.env` or script
4. Run:
    python price_logger.py

## Example use cases:
- Track price trends and spikes
- Automate trading alerts
- Build personal crypto dashboards

*Author: Dimitris Seriatos*
