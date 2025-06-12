# 🏏 Cricket Telegram Bot

A Telegram bot that gives live cricket match updates and information using the CricAPI. Users can view current matches, live scores, and match details via simple Telegram commands.

---

## 🚀 Features

- `/start` - Welcomes the user and shows available commands.
- `/score` - Shows current live match scores.
- `/matches` - Lists current/upcoming matches with venue and team info.

---

## 🔧 Tech Stack

- Python
- python-telegram-bot
- CricAPI
- requests

---

## 🛠 Setup Instructions

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/cricket-telegram-bot.git
   cd cricket-telegram-bot
   
Create and activate a virtual environment:
python -m venv venv
venv\Scripts\activate   # For Windows



Install dependencies:
pip install python-telegram-bot requests


Add your API keys in bot.py:
TELEGRAM_BOT_TOKEN = "your-telegram-token"
CRICAPI_KEY = "your-cricapi-key"


Run the bot:python bot.py


API Used
CricAPI: https://cricapi.com for live cricket match data and scores.


