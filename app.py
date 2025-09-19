from flask import Flask, request, jsonify
from instance_grp.createInstanceGrp import create_instance_group
from instance_grp.deleteInstanceGrp import delete_instance_group

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_json():
    # Save the incoming JSON to a variable
    received_data = request.get_json()
    
    if received_data is None:
        return jsonify({'error': 'Invalid or missing JSON'}), 400

    # You can now use 'received_data' as needed
    # For example, print it or process it
    print("Received JSON:", received_data)
    # Respond with the received data
    try:
        if(received_data['node-count'] > 0):
            create_instance_group(
                project_id=received_data['project-id'],
                zone=received_data['zone'],
                group_name=received_data['cluster-id'],
                instance_template=received_data['instance-template'],
                size=int(received_data['node-count'])
            )
            return jsonify({'status': 'success', 'message': f"Instance group '{received_data['cluster-id']}' creation initiated."})
        elif(received_data['node-count'] == 0):
            delete_instance_group(
                project_id=received_data['project-id'],
                zone=received_data['zone'],
                group_name=received_data['cluster-id']
            )
    except KeyError as e:
        return jsonify({'error': f'Missing key in JSON: {e}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/data', methods=['GET'])
def send_json():
    return jsonify({'message': 'Hello from CloudOrchestre!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
