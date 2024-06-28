from flask_cors import CORS
from flask import Flask, redirect
from text_gen import get_response


app = Flask(__name__)
CORS(app)


#ROUTES
@app.route("/create_ppt")
def index():
  get_response("Make a presentation in robots")
  print(get_response)
  return "Hello Py"




if __name__ == "__main__":
  app.run(debug=True)