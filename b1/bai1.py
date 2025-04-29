import requests
import csv

# URL của bản sao dữ liệu
url = "https://gist.githubusercontent.com/yi-jiayu/ea4f0a6c5b9734dd82920cf739b1f707/raw/79dabce87503050d4d64d0332e2076e4d5485171/pokemon.min.json"

# Tải dữ liệu JSON
response = requests.get(url)
data = response.json()

# Các trường cần trích xuất
fields = ["number", "name", "type", "height", "weight", "ThumbnailImage"]

# Ghi dữ liệu vào tệp CSV
with open("pokemon_data.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    for pokemon in data:
        row = {field: pokemon.get(field) for field in fields}
        writer.writerow(row)

print("Dữ liệu đã được lưu vào 'pokemon_data.csv'")