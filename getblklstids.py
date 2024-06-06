import requests

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

# Function to save token IDs in a markdown file
def save_to_markdown(token_ids, filename, title):
    with open(filename, "a") as file:  # Use "a" for append mode
        file.write(f"## {title} Token IDs\n\n")
        file.write("| Token ID |\n")
        file.write("|----------|\n")
        for token_id in token_ids:
            file.write(f"| {token_id} |\n")
        file.write("\n")

# Main function
def main():
    with open("blacklist.md", "w") as file:
        file.write("# Blacklisted Token IDs\n\n")
    for endpoint in endpoints:
        token_ids = fetch_token_ids(endpoint)
        if token_ids:
            save_to_markdown(token_ids, "blacklist.md", endpoint["title"])

if __name__ == "__main__":
    main()
