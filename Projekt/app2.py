import aiohttp
import asyncio
from flask import Flask, request

app = Flask(__name__)

async def call_elearning_api():
    # Call the e-learning API and get the response
    async with aiohttp.ClientSession() as session:
        async with session.get("http://127.0.0.1:5000/get_links") as resp:
            data = await resp.json()
    
    async with aiohttp.ClientSession() as session:
        print("- POSLAO WT_W")
        async with session.post("http://127.0.0.1:5002/wt_w", json=data['usernames']) as resp:
            pass
    
    async with aiohttp.ClientSession() as session:
        print("- POSLAO WT_D")
        async with session.post("http://127.0.0.1:5002/wt_d", json=data['usernames']) as resp:
            pass

@app.route('/call_elearning_api', methods=['POST', 'GET'])
def call_elearning_api_route():
    asyncio.run(call_elearning_api())
    return "E-learning API called and data passed to the 2nd microservice!"

if __name__ == '__main__':
    app.run(port=5001)