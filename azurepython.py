from flask import Flask
from flask import request
import json
import os
from flask import make_response
app = Flask(__name__)

@app.route('/',methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)

    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return 'apple'
'''
def processRequest(req):
    print("Request:")
    print(json.dumps(req, indent=4))
    if req.get("result").get("action") == "getBmi":
        data = req
        res = makeWebhookResultForGetBmi(data)
    else:
        return {}
    return res
def makeWebhookResultForGetBmi(data):
    element1 = data.get("result").get("parameters").get("number")
    print (element1)
    element2 = data.get("result").get("parameters").get("number-integer")
    element2 = int(element2)/100
    print (element2)
    bmi = float(element1)/(float(element2*element2))
    bmi =round(bmi,2)
    print(bmi)
    if (bmi<=18.5):
        a = 'underweight'
    elif (bmi>18.5 and bmi<24.9):
        a = 'healthy'
    elif (bmi>25.0 and bmi<29.9):
        a ='overweight'
    else:
        a = 'obese'
    #speech = 'Your bmi is {}' +str(bmi)'and you are'+str(a)
    speech = 'Your bmi is {} and you are {}' .format(bmi,a)

    return {
        "speech": speech,
        "displayText": speech,
        "source": "webhookdata"
    }
'''
if __name__ == '__main__':
  app.run()
