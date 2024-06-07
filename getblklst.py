import requests
import yaml

# Aco's ergexplorer nsfw and scam tokens endpoints
endpoints = [
    {"url": "https://api.ergexplorer.com/tokens/getNsfw", "title": "NSFW"},
    {"url": "https://api.ergexplorer.com/tokens/getScam", "title": "Scam"}
]

# Function to get token IDs from Aco's api
def fetch_token_ids(endpoint):
    response = requests.get(endpoint["url"])
    if response.status_code == 200:
        data = response.json()
        return [item["tokenId"] for item in data["items"]]
    else:
        print(f"Failed to fetch data from {endpoint['title']} endpoint")
        return []

# Function to save token IDs in a YAML file
def save_to_yaml(token_ids, filename, title):
    with open(filename, "a") as file:  # Use "a" for append mode
        yaml.dump({title: token_ids}, file, default_flow_style=False)

# Main function
def main():
    with open("blacklist.yaml", "w") as file:
        file.write("# Blacklisted Token IDs\n\n")
    for endpoint in endpoints:
        token_ids = fetch_token_ids(endpoint)
        if token_ids:
            save_to_yaml(token_ids, "blacklist.yaml", endpoint["title"])

if __name__ == "__main__":
    main()
