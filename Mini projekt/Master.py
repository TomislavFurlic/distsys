import requests
import time
from flask import Flask, request
import random

# Lista adresa za workere
workers = ["http://127.0.0.1:5001", "http://127.0.0.1:5002", "http://127.0.0.1:5003", "http://127.0.0.1:5004", "http://127.0.0.1:5005"]
worker_counter = 0

app = Flask(__name__)

@app.route("/register", methods=["POST"])
def register_worker():
    global worker_counter
    worker_counter += 1
    worker_id = worker_counter
    workers.append(f"http://127.0.0.1:{5000 + worker_id}")
    print(f"Worker {worker_id} from http://127.0.0.1:{5000 + worker_id} is sucesfully connected!")
    return {"worker_id": worker_id}

@app.route("/process", methods=["POST"])
def process():
    task = request.get_json()
    client_id = task["client_id"]
    code = task["code"]
    # Podjela koda na chunkove
    code_chunks = [code[i:i+100] for i in range(0, len(code), 100)]
    # Slanje zahtjeva workeru za obradu
    word_count = 0
    for chunk in code_chunks:
        worker = random.choice(workers)
        response = requests.post(f"{worker}/work", json={"client_id": client_id, "code_chunk": chunk})
        word_count += response.json()["word_count"]
    # Ukupan zbroj
    return {"word_count": word_count} 

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)