import requests
import yaml
import json

# Aco's ergexplorer NSFW and scam tokens endpoints
endpoints = [
    {"url": "https://api.ergexplorer.com/tokens/getNsfw", "title": "NSFW"},
    {"url": "https://api.ergexplorer.com/tokens/getScam", "title": "Scam"}
]

# Function to get token IDs from Aco's API
def fetch_token_ids(endpoint):
    response = requests.get(endpoint["url"])
    if response.status_code == 200:
        data = response.json()
        return [item["tokenId"] for item in data["items"]]
    else:
        print(f"Failed to fetch data from {endpoint['title']} endpoint")
        return []

# Function to save token IDs in a YAML file
def save_to_yaml(token_data, filename):
    with open(filename, "w") as file:
        file.write("# Blacklisted Token IDs\n\n")
        yaml.dump(token_data, file, default_flow_style=False)

# Function to save token IDs in a JSON file
def save_to_json(token_data, filename):
    formatted_data = {key.lower(): value for key, value in token_data.items()}  # Ensure JSON keys are lowercase
    with open(filename, "w") as file:
        json.dump(formatted_data, file, indent=4)

# Main function
def main():
    token_data = {}
    
    for endpoint in endpoints:
        token_ids = fetch_token_ids(endpoint)
        if token_ids:
            token_data[endpoint["title"]] = token_ids
    
    if token_data:
        save_to_yaml(token_data, "blacklist.yaml")
        save_to_json(token_data, "blacklist.json")

if __name__ == "__main__":
    main()
