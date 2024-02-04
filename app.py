from flask import Flask, send_from_directory, jsonify
import json
import os

app = Flask(__name__, static_folder='client/build')

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


# Flask API endpoint
@app.route('/api/data')
def api_data():
    return {'data': "data"}

# Flask API endpoint for getting data
@app.route('/api/getData')
def get_data():
    # Process request and return response
    with open('camps.json') as f:
        data = json.load(f)
    return jsonify({'data': data})

# Returning JSON data from a Flask endpoint
@app.route('/api/sendData')
def send_data():
    return jsonify({'message': 'Data sent successfully'})

# Flask error handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


# Serve React build files in Flask
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)