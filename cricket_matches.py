import requests

# Step 1: Set your API key and URL
API_KEY = "00953195-0f03-4d7a-8619-991179e97810"
URL = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"

# Step 2: Send a GET request to the CricAPI
try:
    response = requests.get(URL)
    data = response.json()

    # Check if data was returned successfully
    if data.get("status") == "success":
        matches = data.get("data", [])

        if not matches:
            print("No live matches found.")
        else:
            # Step 3: Loop through each match and print details
            for match in matches:
                name = match.get("name", "N/A")
                status = match.get("status", "N/A")
                venue = match.get("venue", "N/A")
                date = match.get("date", "N/A")
                teams = match.get("teams", ["Team 1", "Team 2"])
                score_info = match.get("score", [])

                print(f"🏏 Match: {name}")
                print(f"📍 Venue: {venue}")
                print(f"📅 Date: {date}")
                print(f"🧢 Teams: {teams[0]} vs {teams[1]}")
                print(f"🕹 Status: {status}")

                if score_info:
                    for score in score_info:
                        print(f"🏏 {score['inning']}: {score['r']} runs / {score['w']} wickets in {score['o']} overs")
                else:
                    print("🔄 Score not available yet.")

                print("-" * 50)

    else:
        print("❌ Failed to fetch match data:", data.get("message", "Unknown error"))

except Exception as e:
    print("⚠️ Error occurred:", str(e))
