from flask import Blueprint
import datetime
import requests

app1 = Blueprint('app1', __name__)


@app1.route('/time')
def time():
    current_time = datetime.datetime.now().date().isoformat()
    return current_time

@app1.route('/quote')
def quote():
    random_quote = requests.get('https://api.kanye.rest').json()['quote']
    return random_quote