#!/usr/bin/env python3

from flask import render_template, request, abort, url_for, redirect, session, escape, jsonify
from app import app
from app.models import register, has_connect, check_login, get_user_data

@app.route('/' , methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'    

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    result = {"error" : "internal error"}
    if request.method == 'POST' and has_connect() == False:
        username = request.form['username']
        password = request.form['password']
        if check_login(username, password) == True:
            session['username'] = username
            result = {"result" : "signin successful"}
            return redirect(url_for('index'))
        else:
            result = {"error" : "login or password does not match"}
    return render_template('login.html',
                           title="Connexion Page",
                           subtitle="Login in",
                           result=result)

@app.route('/signout', methods=['GET', 'POST'])
def signout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def client_register():
    result = {"error" : "internal error"}
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = register(username, password)
    return render_template('register.html',
                           title="Register Page",
                           subtitle="Create account",
                           result=result)

@app.route('/user', methods=['GET', 'POST'])
def user_account():
    result = {"error" : "internal error"}
    user_res = {"error" : "internal error"}
    if has_connect() == True:
        user_res = get_user_data()
    else:
        result = {"error" : "you must be logged in"}
    return render_template('user.html',
                           title="User Page",
                           subtitle="User's informations",
                           result=result,
                           user_res=user_res)

@app.route('/user/task', methods=['GET', 'POST'])
def user_task():
    result = {"error" : "internal error"}
    if has_connect() == True:
        return ('register.html')
    else:
        result = {"error" : "you must be logged in"}
    return render_template('register.html',
                           result=result)

@app.route('/user/task/id', methods=['GET', 'POST'])
def user_task_id():
    plop = 'plop'
    #View specific task of the use using specific id
    #Update specific task with the id

@app.route('/user/task/add', methods=['GET', 'POST'])
def user_task_add():
    result = {"error" : "internal error"}
    if has_connect() == True:
        title = request.form['title']
        begin = request.form['begin']
        end = request.form['end']
        status = request.form['status']
        result = add_task(title, begin, end, status)
    else:
        result = {"error" : "you must be logged in"}
    return render_template('register.html', result=result)

@app.route('/user/task/del/id', methods=['GET', 'POST'])
def user_task_del_id():
    error = 0
    #Delete a task with the id
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

