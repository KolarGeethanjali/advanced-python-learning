import requests

url = "https://pokeapi.co/api/v2/pokemon/"

response = requests.get(url)

total_records = response.json().get("count")

print(total_records)

all_data = []

for i in range(0, total_records, 20):
    paginated_url = f"{url}?offset={i}&limit=20"
    response = requests.get(paginated_url)
    data = response.json()
    all_data.append(data)

print(len(all_data))

# Query Parameters Explanation
# --------------------------------
# In a URL, query parameters are used to control what data the API returns.
# They are added after a "?" in the URL.

# Example:
# ?offset=40&limit=20

# offset → tells the API how many records to skip
# limit  → tells the API how many records to return

# So:
# offset=40 → skip first 40 records
# limit=20  → return next 20 records

# This technique is called "Pagination".
# Pagination is used when APIs return data in small batches
# instead of sending all records at once.

# offset = skip records | limit = number of records to fetch (pagination)