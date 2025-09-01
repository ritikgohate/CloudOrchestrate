from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_json():
    data = request.get_json()
    return jsonify({'received': data})

@app.route('/data', methods=['GET'])
def send_json():
    return jsonify({'message': 'Hello from Cloud Run!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
