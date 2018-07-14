from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  a=1
  return 'Hey its Python Flask application!',a

@app.route('/hai')
def hai():
  return 'this is hai'

if __name__ == '__main__':
  app.run()
