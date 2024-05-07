from flask import Flask, send_file, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def app_route():
    return send_file(os.path.join(os.path.dirname(__file__), 'index.html')), 200

# Define a dictionary to store dynamic variables
variables = {}

@app.route('/endpointName', methods=['POST'])
def endpointName():
    variables['request_data'] = request.get_json()
    variables['var1'] = variables['request_data']
    print(variables['var1'])



@app.errorhandler(404)
def not_found(e):
    return "Page not found", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
