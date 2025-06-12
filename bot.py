from telegram.ext import Updater, CommandHandler
import requests

# Your tokens
TELEGRAM_BOT_TOKEN = "6966190822:AAFwkWLpcRnNHbVcv8s3eJm4VF0ylzT7Rbs"
CRICAPI_KEY = "00953195-0f03-4d7a-8619-991179e97810"

# 🏏 Fetch current live scores
def get_live_scores():
    url = f"https://api.cricapi.com/v1/cricScore?apikey={CRICAPI_KEY}"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "success":
        return "❌ Couldn't fetch live scores."

    matches = data.get("data", [])
    if not matches:
        return "😔 No live matches found."

    message = "🏏 *Live Scores*\n\n"
    for match in matches:
        t1 = match.get("t1", "Team 1")
        t2 = match.get("t2", "Team 2")
        t1s = match.get("t1s", "N/A")
        t2s = match.get("t2s", "N/A")
        status = match.get("status", "Unknown")
        series = match.get("series", "Unknown")
        date = match.get("dateTimeGMT", "N/A")

        message += f"*{t1}* vs *{t2}*\n"
        message += f"📅 {date}\n"
        message += f"🏆 Series: {series}\n"
        message += f"🎯 Status: {status}\n"
        message += f"🔹 {t1}: {t1s}\n"
        message += f"🔸 {t2}: {t2s}\n"
        message += "--------------------------------------------------\n\n"
    
    return message

# 🗓 Fetch upcoming and live match details
def get_match_details():
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={CRICAPI_KEY}&offset=0"
    response = requests.get(url)
    data = response.json()

    if data.get("status") != "success":
        return "❌ Couldn't fetch match info."

    matches = data.get("data", [])
    if not matches:
        return "😔 No match data found."

    message = "📅 *Current/Upcoming Matches*\n\n"
    for match in matches[:5]:  # Show top 5
        name = match.get("name", "Match")
        venue = match.get("venue", "N/A")
        date = match.get("date", "Unknown")
        teams = match.get("teams", ["Team 1", "Team 2"])
        status = match.get("status", "Unknown")
        score = match.get("score", [])

        message += f"🏏 *{name}*\n"
        message += f"📍 Venue: {venue}\n"
        message += f"📅 Date: {date}\n"
        message += f"🧢 Teams: {teams[0]} vs {teams[1]}\n"
        message += f"🕹 Status: {status}\n"

        if score:
            for entry in score:
                message += f"🏏 {entry.get('inning')}: {entry.get('r')} runs / {entry.get('w')} wickets in {entry.get('o')} overs\n"
        else:
            message += "🔄 Score not available yet.\n"

        message += "--------------------------------------------------\n\n"

    return message

# Handlers
def start(update, context):
    update.message.reply_text("🏏 Welcome! Use /matches for match info and /score for live scores.")

def matches(update, context):
    update.message.reply_text("📡 Fetching match details...")
    info = get_match_details()
    send_long_message(info, update, parse_mode='Markdown')

def score(update, context):
    update.message.reply_text("📡 Fetching live scores...")
    info = get_live_scores()
    send_long_message(info, update, parse_mode='Markdown')


def send_long_message(text, update, parse_mode='Markdown'):
    for i in range(0, len(text), 4096):
        update.message.reply_text(text[i:i+4096], parse_mode=parse_mode)

# Run the bot
def main():
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("matches", matches))
    dp.add_handler(CommandHandler("score", score))

    print("✅ Bot is running...")
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
