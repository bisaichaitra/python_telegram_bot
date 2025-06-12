import requests

API_KEY = "00953195-0f03-4d7a-8619-991179e97810"
URL = f"https://api.cricapi.com/v1/cricScore?apikey={API_KEY}"

response = requests.get(URL)
data = response.json()

if data.get("status") == "success":
    matches = data.get("data", [])
    for match in matches:
        team1 = match.get("t1", "Team 1")
        team2 = match.get("t2", "Team 2")
        team1_score = match.get("t1s", "No score")
        team2_score = match.get("t2s", "No score")
        status = match.get("status", "Status unknown")
        series = match.get("series", "Series unknown")
        date = match.get("dateTimeGMT", "Date unknown")

        print(f"🏏 {team1} vs {team2}")
        print(f"📅 Date: {date}")
        print(f"🎯 Series: {series}")
        print(f"🕹 Status: {status}")
        print(f"🔹 {team1}: {team1_score}")
        print(f"🔸 {team2}: {team2_score}")
        print("--------------------------------------------------")
else:
    print("❌ Failed to fetch cricScore data.")
