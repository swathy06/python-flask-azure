from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  a=1
  b=2
  c=3
  if(c>b and c>a):
    
    return str(c),str(1)
  else:
    return 'I am the best'



if __name__ == '__main__':
  app.run()
