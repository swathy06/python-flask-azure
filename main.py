from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hey its Python Flask application!'
def hai('/hai'):
  return 'this is hai'

if __name__ == '__main__':
  app.run()
