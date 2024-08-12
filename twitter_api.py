import http.client
import pandas as pd
import json

# Create a connection to the API
conn = http.client.HTTPSConnection("news-api14.p.rapidapi.com")

# Define headers with your API key
headers = {
    'x-rapidapi-key': "16d4fda647mshcf07fb0add19e4dp180a82jsna76b3a1969f1",
    'x-rapidapi-host': "news-api14.p.rapidapi.com"
}

# Define the query parameter
query = "trump"  # Replace with your desired search term

# Make the request with query parameter
conn.request("GET", f"/v2/search/publishers?query={query}", headers=headers)

# Get the response
res = conn.getresponse()
data = res.read()

# Decode the response
response_json = json.loads(data.decode("utf-8"))

# Extract the relevant data
if 'data' in response_json:
    publishers_data = response_json['data']
else:
    publishers_data = []

# Convert to DataFrame
df = pd.DataFrame(publishers_data)

# Display the DataFrame
print(df)

