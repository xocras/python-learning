import requests

# Response Codes:

# 1XX: Hold
# 2XX: Success
# 3XX: No Permission
# 4XX: Client Side
# 5XX: Server Side

response = requests.get("http://api.open-notify.org/iss-now.json")

response.raise_for_status()

iss_position = response.json()['iss_position']

print(f"\nISS Location:\nX ({iss_position['latitude']}) Y ({iss_position['longitude']})")
