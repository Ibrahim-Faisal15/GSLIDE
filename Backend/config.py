from flask import Flask, request, jsonify
from flask_cors import CORS 
from render_ppt import get_presentation



app = Flask(__name__)
CORS(app=app)

@app.route('/create_ppt', methods=['POST'])
def create_ppt():
        data = request.get_json()
        print(data)

        


        
        return  jsonify(data) # 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True, port=3000)
