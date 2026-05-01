# Simplified Binance Futures Trading Bot (Testnet)

## 📌 Overview
This project is a Python-based CLI trading bot that interacts with the Binance Futures Testnet API.  
It supports placing MARKET and LIMIT orders for USDT-M futures.

The goal of this project is to demonstrate:
- REST API integration
- CLI application design
- Input validation
- Logging system
- Error handling

---

## ⚙️ Features

- Place MARKET orders (BUY / SELL)
- Place LIMIT orders (BUY / SELL)
- CLI-based input using argparse
- Input validation (symbol, side, quantity, price)
- Structured logging to file
- Error handling for API and runtime failures
- Binance Futures Testnet integration

---

## 🧱 Project Structure

    trading_bot/
    ├── bot/
    │   ├── client.py
    │   ├── validators.py
    │   ├── logger.py
    │
    ├── cli.py
    ├── .env
    ├── logs.txt
    ├── requirements.txt
    └── README.md

---

## 🚀 Setup Instructions

### 1. Clone repository
```
git clone https://github.com/algoWithSachin/binance-futures-trading-bot.git
```
```
cd trading_bot
```
### Create Virtual Env
```
uv venv
```
### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Create .env file
```
API_KEY=your_testnet_api_key  
API_SECRET=your_testnet_secret  
BASE_URL=https://demo-fapi.binance.com  
```
## ▶️ How to Run

```
### MARKET Order
uv run python cli.py --symbol BTCUSDT --side BUY --type MARKET --qty 0.01

---

### LIMIT Order
uv run python cli.py --symbol BTCUSDT --side SELL --type LIMIT --qty 0.01 --price 70000

```


## 📊 Example Output
```

ORDER RESPONSE
----------------------------------------
Order ID     : 123456789
Symbol       : BTCUSDT
Side         : BUY
Type         : MARKET
Status       : NEW
Qty          : 0.01
Executed Qty : 0.01
----------------------------------------

```

## 📁 Logging
```

logs.txt stores all events:

ORDER PLACED | BTCUSDT | BUY | MARKET | qty=0.01 | orderId=123456

ERROR | BTCUSDT | SELL | error=Invalid price range

```

## ⚠️ Important Notes

- Uses Binance Futures Testnet only
- No real money is used
- API keys must be kept private
- LIMIT orders must follow exchange price rules

---

## 🧠 Tech Stack

- Python 3.x
- requests
- python-dotenv
- argparse
- Binance Futures Testnet API

---

## 📌 Disclaimer

This project is for educational and evaluation purposes only.  
It is not intended for live trading or production use.

---

## 👨‍💻 Author

Built as part of a technical assignment demonstrating backend/API integration skills.