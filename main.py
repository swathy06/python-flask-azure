from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  a=1
  return str(a)



if __name__ == '__main__':
  app.run()
