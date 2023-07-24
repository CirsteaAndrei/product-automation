from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/process_url', methods=['POST'])
def process_url():
    url = request.json.get('url')
    # Here you would process the URL with your Python program
    print(f'Received URL: {url}')
    return {'message': 'URL received'}

if __name__ == '__main__':
    app.run(port=5000)