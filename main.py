# from dis import dis
# from flask import Flask, request
# from flask import jsonify
# import os
# from google.cloud import dialogflow
# from google.api_core.exceptions import InvalidArgument


# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "./tarushwhatsappbot-rivt-eee43ee7aa97.json"
# DIALOGFLOW_PROJECT_ID = "dialogflow-python-quickstart"
# DIALOGFLOW_LANGUAGE_CODE = "en-US"
# SESSION_ID = "me"

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "HELLO"

# @app.route("/api/getMessages", methods=["POST"])
# def home():
#     message = request.form.get('Body')
#     mobum = request.form.get('From')
#     session_client = dialogflow.SessionsClient()
#     session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
#     text_input = dialogflow.types.TextInput(text=message, language_code=DIALOGFLOW_LANGUAGE_CODE)
#     query_input = dialogflow.types.QueryInput(text=text_input)
#     try:
#         response = session_client.detect_intent(session=session, query_input=query_input)
#     except InvalidArgument:
#         raise
#     print("Ouery Text:", response.query_result.query_text)
#     print("Detected Intent:", response.query_result.intent.display_name)
#     print("Detected Intent confidence:", response.query_result.intent_detection_confidence)
#     print("Fulfillment Text:", response.query_result.fulfillment_text)
#     sendMessage(mobum, response.query_result.fulfillment_text)
#     return jsonify({"message": response.query_result.fulfillment_text})    


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"