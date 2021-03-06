#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
####################################################################
#    Animus AI Developed by Kuldeep Paul Dated 4th November 2018   #
#    Animus Core                                                   #
#    Copyright 2018 Kuldeep Paul and Quinch Systems Pvt. Ltd.      #
####################################################################
####################################################################
# Main Entry File for the API

from animus import detected_callback
import os
import sys
import json
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    # when the endpoint is registered as a webhook, it must echo back
    # the 'hub.challenge' value it receives in the query arguments
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "VERIFY_TOKEN":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200

    return "API is active", 200


@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events
  try:
    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing

    if data["object"] == "page":

        for entry in data["entry"]:
            for messaging_event in entry["messaging"]:

                if messaging_event.get("message"):  # someone sent us a message

                    sender_id = messaging_event["sender"]["id"]        # the facebook ID of the person sending you the message
                    #recipient_id = messaging_event["recipient"]["id"]  # the recipient's ID, which should be your page's facebook ID
                    try:
                        message_text = messaging_event["message"]["text"]  # the message's text

                        reply=detected_callback(message_text)
                        send_message(sender_id, str(reply))
                    except:
                        send_message(sender_id,str("Sorry! I didn't get that."))
                if messaging_event.get("delivery"):  # delivery confirmation
                    pass

                if messaging_event.get("optin"):  # optin confirmation
                    pass

                if messaging_event.get("postback"):  # user clicked/tapped "postback" button in earlier message
                    pass

    return "ok", 200
  except:
    pass


def send_message(recipient_id, message_text):

    log("sending message to {recipient}: {text}".format(recipient=recipient_id, text=message_text))

    params = {
        "access_token": "EAAhZB4FUE1s8BAKD3tVfJyesjAToxJxXfufKAVoLFkQ8aZBnn0JTgmRUteuSEXVsV9RhseyWYVHnRIx1kblR99upSkovZArJLssc1Ow4JmERTF9FykM2q5AZBxQZCbZAZBBAu1oDjxXTzdyRZA6HBFTLUwUZBqRdVhNN41Et39zL0j2YSZCjB90hZCgw2tC1L9XwTUZD"
    }
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "text": message_text
        }
    })
    r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)
    if r.status_code != 200:
        log(r.status_code)
        log(r.text)


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(host = 'localhost', port = 3000)
