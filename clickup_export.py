import requests
import pandas as pd

# Set your ClickUp API token and team ID
API_TOKEN = "your_clickup_api_token_here"  # Replace with your API Token
TEAM_ID = "your_team_id_here"  # Replace with your Team ID
API_URL = f"https://api.clickup.com/api/v2/team/{TEAM_ID}/audit"

# Set the headers for the API request
headers = {"Authorization": API_TOKEN}

# Send the request to fetch activity data
response = requests.get(API_URL, headers=headers)

if response.status_code == 200:
    # Extract and process JSON data
    data = response.json().get("data", [])
    if data:
        df = pd.json_normalize(data)  # Flatten JSON data
        df.to_csv("clickup_activity_logs.csv", index=False)
        print("✅ Activity logs exported to 'clickup_activity_logs.csv'")
    else:
        print("⚠️ No activity logs found.")
else:
    print(f"❌ Error {response.status_code}: {response.text}")
