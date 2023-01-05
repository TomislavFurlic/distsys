import asyncio
import aiofiles
from flask import Flask, request, jsonify
import aiohttp

app = Flask(__name__)

@app.route('/gather_data', methods=['POST'])
def gather_data():
    data = request.get_json()
    #print(data)
    if len(data) > 10:
        # Asynchronously create a file for each element in the list
        tasks = []
        for i, element in enumerate(data):
            tasks.append(create_file(i, element))
        # Reference to the current event loop
        loop = asyncio.get_event_loop()
        # Run the asynchronous tasks and get the response
        response = loop.run_until_complete(asyncio.gather(*tasks))
    else:
        response = "No files created"
    # Return the response as a JSON object
    return jsonify(response)

async def create_file(i, element):
    async with aiofiles.open(f"file{i}.txt", "w") as f:
        await f.write(element)

if __name__ == '__main__':
    app.run(port=5003)