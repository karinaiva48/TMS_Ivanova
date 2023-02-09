from flask import Blueprint, request, abort, render_template
import requests
import datetime
from .validation import Validator, Validation

app1 = Blueprint('app1',__name__)

@app1.route('/time')
def time():
    current_time = datetime.datetime.now().date().isoformat()
    return current_time


@app1.route('/quote')
def get_qoute():
    number = int(request.args.get('number', 1))
    quotes = ''
    for i in range(number):
        response = requests.get('http://api.kanye.rest')
        quotes += f"Цитата № {i+1}: {response.json()['quote']}<br>"
    return quotes



@app1.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':  
        src = dict(request.form)  
        try:
            username, password, email = request.form['username'], request.form['password'], request.form['email']
        except KeyError as e:
            return f'Поле {e} не было передано'
        validator_1 = Validator(username, password, email)  
        try:
            if validator_1.validation():  
                abort(405)
        except Validation:  
            abort(406) 
    return render_template('register.html')


@app1.errorhandler(405)
def valid_accept(error):
    return  'Вы успешно зарегистрированы'


@app1.errorhandler(406)
def valid_error(error):
    return 'Ошибка регистрации'