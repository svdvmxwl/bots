from datetime import datetime
from flask import Flask, jsonify, request, make_response
from flask_json import FlaskJSON, JsonError, json_response, as_json
import urllib

from OpenSSL import SSL
import json
import requests
import yaml
import pymongo
import logging

client=pymongo.MongoClient()
db_dev=client.locdev_inc_asp_db

app = Flask(__name__)
# FlaskJSON(app)

with open('./config.yaml') as ymlf:
    yaml_out = yaml.load(ymlf)

urls = "https://slack.com/api/chat.postMessage"
Content_type = "application/json"
Authorization =yaml_out['BotUserOAuthAccessToken']
headers = {
    "Content-Type":Content_type,
    "Authorization":"Bearer" +" "+Authorization
}

@app.route('/bots/replied',methods=['GET','POST'])
def replied():
    print(request.data)
    resp =make_response()
    resp.headers['Content-type'] = 'application/json'
    return resp
@app.route('/bots',methods=['GET','POST'])
def bot():
    print(request.get_data())
    resp =make_response()
    resp.headers['Content-type'] = 'application/json'
    return resp

if __name__ == '__main__':
	app.run()
