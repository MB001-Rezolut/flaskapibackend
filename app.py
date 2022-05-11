from dis import dis
from flask import Flask, request
from flask import jsonify
import os
from google.cloud import dialogflow_v2beta1 as dialogflow
from google.api_core.exceptions import InvalidArgument
import requests

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./tarushwhatsappbot-rivt-eee43ee7aa97.json"
DIALOGFLOW_PROJECT_ID = "tarushwhatsappbot-rivt"
DIALOGFLOW_LANGUAGE_CODE = "en-US"
SESSION_ID = "me"

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "HELLO"

@app.route("/api/getMessages", methods=["POST"])
def home():
    message = request.form.get('Body')
    mobum = request.form.get('From')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)
    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
    except InvalidArgument:
        raise
    print("Ouery Text:", response.query_result.query_text)
    print("Detected Intent:", response.query_result.intent.display_name)
    print("Detected Intent confidence:", response.query_result.intent_detection_confidence)
    print("Fulfillment Text:", response.query_result.fulfillment_text)
    sendMessage(mobum, response.query_result.fulfillment_text)
    return response.query_result.fulfillment_text    


def sendMessage(mobum, message):
    url = "https://api.twilio.com/2010-04-01/Accounts/AC8795e41c7086e1df6a82062131d2dcb1/Message.json"
    payload={"from":'whatsapp:+14155238886',
    'Body':message,
    'to':mobum}
    headers={
        'Authoriziation' :'Basic ea5fb8efedc902a897db9f79e4507d97'
    }
    reponse = requests.request("POST", url, data=payload, headers=headers)
    print(reponse.text)
    return reponse.text
    # account_sid = 'AC8795e41c7086e1df6a82062131d2dcb1' 
    # auth_token = 'ea5fb8efedc902a897db9f79e4507d97' 
   
    
    print(message.sid)