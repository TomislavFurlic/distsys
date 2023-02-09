import pandas as pd
import random
import requests

# Lista od 10000 klijenata
client_ids = [i for i in range(10000)]

# Ucitavanje
chunks = pd.read_json("file-000000000040.json", lines=True, chunksize=1000)

# Podjednaka podjela koda među klijentima
client_data = {}
for chunk in chunks:
    for index, row in chunk.iterrows():
        client_id = client_ids[index % len(client_ids)]
        if client_id not in client_data:
            client_data[client_id] = ""
        client_data[client_id] += row["content"]

# Prosječan broj slova svih kodova
total_characters = 0
for code in client_data.values():
    total_characters += len(code)
avg_characters = total_characters / len(client_data)
print("Average number of characters:", avg_characters)

# Slanje zahtjeva master servisu za procesuiranje
for client_id, code in client_data.items():
    requests.post("http://127.0.0.1:5000/process", json={"client_id": client_id, "code": code})