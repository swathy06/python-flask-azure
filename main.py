from flask import Flask
app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    req = request.get_json(silent=True, force=True)
 
    print("Request:")
    print(json.dumps(req, indent=4))
 
    res = processRequest(req)
 
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r
  #return 'Hey its Python Flask application!'


if __name__ == '__main__':
  app.run()
