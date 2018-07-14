from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  a= 1
  b= 2
  c= a+b
  
  return 'Hey its Python Flask application!'


if __name__ == '__main__':
  app.run()
