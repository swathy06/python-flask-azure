from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'first page'

#@app.route('/hello')
#def hello_world():
 # return 'second page'


if __name__ == '__main__':
  app.run()
