from flask import Flask, request, jsonify
from flask_cors import CORS 

app = Flask(__name__)
CORS(app=app)

@app.route('/create_ppt', methods=['POST'])
def create_ppt():
        # Attempt to get the JSON data from the request
        data = request.get_json()
        print(data)

        
        return jsonify({'error': 'Internal server error'}), 500  # 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)
