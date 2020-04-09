from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
  x = "hello"
  return jsonify({"about" : x})
  #return "hello"




if __name__=="__main__":
  app.run(debug=True)