from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  a= 1
  b= 2
  c= a+b
  
  return 'Apple a day'

@app.route('/hello')
def hello():
    return ', World'


if __name__ == '__main__':
  app.run()
