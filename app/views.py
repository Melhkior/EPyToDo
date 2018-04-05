#!/usr/bin/env python3

from flask import render_template, request, abort, url_for, redirect, session, escape
from app import app
from app.models import register

@app.route('/' , methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'    

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        error = 'Invalid username/password'
    return render_template('register.html', error=error)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def client_register():
    form = "PLOP"
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        register(username, password)
        return redirect(url_for('signin'))
    return render_template('register.html', form=form)

@app.route('/user', methods=['GET', 'POST'])
def user_account():

@app.route('/user/task', methods=['GET', 'POST'])
def user_account():

@app.route('/user/task/idfe', methods=['GET', 'POST'])
def user_account():

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

