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
    #return r
def processRequest(req):
    print("Request:")
    print(json.dumps(req, indent=4))
    if req.get("result").get("action") == "yahooWeatherForecast":
        baseurl = "https://query.yahooapis.com/v1/public/yql?"
        yql_query = makeYqlQuery(req)
        if yql_query is None:
            return {}
        yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
        result = urlopen(yql_url).read()
        data = json.loads(result)
        res = makeWebhookResult(data)
    elif req.get("result").get("action") == "numbers.add":
        data = req
        res = makeWebhookResultForGetBmi(data)
    else:
        return {}
    return res
 
def makeWebhookResultForGetBmi(data):
    element1 = data.get("result").get("parameters").get("number")
    print (element1)

    element2 = data.get("result").get("parameters").get("number1")
    print(66666)
    Symbol = (element1)+(element2)
    s=sum(Symbol)
    print(s)
    speech = 'The addition of  is '+str(s)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "webhookdata"
    }
 
  #return 'Hey its Python Flask application!'


if __name__ == '__main__':
  app.run()
