from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if (request.method == 'POST'):
    x = request.get_json()
    return jsonify({'you sent' : x}), 201
  else:
    return jsonify({'key':' pair'})


if __name__=='__main__':
  app.run(debug=True)