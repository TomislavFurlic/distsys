import asyncio
import urllib
import aiohttp
import sys
import mysql.connector
import json
import aiofiles
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Database
conn = mysql.connector.connect(
    user="tfurlic",
    password="tomislavfurlic",
    host="db4free.net",
    database="unipu2023"
)

cursor = conn.cursor()

def populate_database():
    print('Populating database with test data...')
    # Open the JSON file
    with open('file-000000000040.json', 'r') as f:
        line_count = 0
        rows = []
        # Iterate over the lines in the file
        for line in f:
            line_count += 1
            # Parse the JSON object on each line
            data = json.loads(line)
            # Store the data in a list of tuples
            username, filename = data['repo_name'].split('/')
            github_link = "https://github.com/{}/{}".format(username, filename)
            print(username, filename)
            rows.append((username, github_link, filename))
            if line_count == 10000: break
        cursor.executemany('INSERT INTO repos (username, ghlink, filename) VALUES (%s, %s, %s)', rows)
        conn.commit()

@app.route('/')
def home():
    return "Welcome to the home page!"

# Route that returns the first 100 rows of the database
@app.route('/get_links')
def get_links():
    cursor.execute('SELECT * FROM repos LIMIT 100')
    rows = cursor.fetchall()
    
    usernames = []
    githubLinks = []
    filename = []
    
    for row in rows:
        usernames.append(row[1])
        githubLinks.append(row[2])
        filename.append(row[3])
    
    data = {
        "usernames": usernames,
        "githubLinks": githubLinks,
        "filename": filename
    }
    
    return jsonify(data)

async def call_elearning_api():
    # Call the e-learning API and get the response
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:5000/get_links") as resp:
            data = await resp.json()
    # Pass the data to the WT microservice as a dictionary
    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:5001/wt_w", json=data) as resp:
            pass
        async with session.post("http://127.0.0.1:5001/wt_d", json=data) as resp:
            pass

if __name__ == '__main__':
    # Check if the database is empty
    cursor.execute('SELECT COUNT(*) FROM repos')
    count = cursor.fetchone()[0]
    if count == 0:
        print('Database is empty, populating with test data...')
        populate_database()

    app.run()
    asyncio.run(call_elearning_api())