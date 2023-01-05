import asyncio
import urllib
import aiohttp
import sys
import mysql.connector
import json
import aiofiles
from flask import Flask, request, jsonify, Response
import requests

app = Flask(__name__)

@app.route('/wt_w', methods=['POST'])
def wt_w():
    usernames = request.get_json()

    # Filter the rows where the username starts with 'd'
    filtered_usernames = [username for username in usernames if username.lower().startswith('w')]
    print(filtered_usernames)

    # Pass the filtered data to the 4th microservice
    async def post_data():
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:5003/gather_data", json=filtered_usernames) as resp:
                pass

    # Run the asynchronous code using asyncio.run()
    asyncio.run(post_data())

    return "Data filtered and passed to 4th microservice!", 200

@app.route('/wt_d', methods=['POST'])
def wt_d():
    usernames = request.get_json()

    # Filter the rows where the username starts with 'd'
    filtered_usernames = [username for username in usernames if username.lower().startswith('d')]
    print(filtered_usernames)

    # Pass the filtered data to the 4th microservice
    async def post_data():
        async with aiohttp.ClientSession() as session:
            async with session.post("http://127.0.0.1:5003/gather_data", json=filtered_usernames) as resp:
                pass

    # Run the asynchronous code using asyncio.run()
    asyncio.run(post_data())

    return "Data filtered and passed to 4th microservice!", 200

if __name__ == '__main__':
    app.run(port=5002)