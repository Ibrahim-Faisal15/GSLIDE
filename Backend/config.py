from flask import Flask, request, send_file,jsonify, make_response
from flask_cors import CORS 
from render_ppt import get_presentation

app = Flask(__name__)
CORS(app)

@app.route('/create_ppt', methods=['POST'])
def create_ppt():
        # Attempt to get the JSON data from the request
        data = request.get_json()
        ppt_bytes = get_presentation(data)
        
        
        return ppt_bytes
if __name__ == '__main__':
    app.run(debug=True)
