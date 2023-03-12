import asyncio
from flask import Flask, jsonify
import goodwe
import os

app = Flask(__name__)

@app.route('/inverters')
async def get_inverters():
    result = asyncio.run(goodwe.search_inverters()).decode("utf-8").split(",")
    print(result)
    return jsonify('')

@app.route('/inverter/<ip_address>', methods=['GET'])
async def get_inverter_data(ip_address):
    inverter = await goodwe.connect(ip_address)
    runtime_data = await inverter.read_runtime_data()

    data = []
    for sensor in inverter.sensors():
        if sensor.id_ in runtime_data:
            data.append({
                "id": sensor.id_,
                "name": sensor.name,
                "value": runtime_data[sensor.id_],
                "unit": sensor.unit,
            })
            
    return jsonify(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
