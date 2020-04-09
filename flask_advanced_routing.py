from flask import Flask

app = Flask(__name__)

#below is a sample of multiple routes rendering the same function

@app.route('/')
@app.route('/home')
@app.route('/new')
def index():
  return "Hello"

#take an input and display it
#pass your value to a variable defined as send_your_name
@app.route('/home/<string:send_your_name>')
def name_dis(send_your_name):
  return "Hello : " + send_your_name


if __name__ == "__main__":
  app.run(debug=True)