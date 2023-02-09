import time
import random
from flask import Flask, request
import requests

app = Flask(__name__)

# Registracija workera i dodjela ID-a
response = requests.post("http://127.0.0.1:5000/register")
worker_id = response.json()["worker_id"]

@app.route("/work", methods=["POST"])
def work():
    task = request.get_json()
    # Simulacija  - delay mreže
    time.sleep(random.uniform(0.1, 0.3))

    # Brojanje riječi
    word_count = len(task["code_chunk"].split())
    print(f"Worker {worker_id} counted {word_count} words for code of client {task['client_id']}")

    return {"word_count": word_count}

if __name__ == "__main__":
    app.run(host= "127.0.0.1", port=5005)