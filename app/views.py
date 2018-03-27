#!/usr/bin/env python3
from flask import render_template
from app import app

@app.route('/' , methods=['GET'])
def route_index():
    return render_template("index.html",
                             title="Hello World",
                             myContent="My SUPER content !!" )
@app.route ('/user/<username>', methods=['GET'])
def route_user(username):
    return render_template("index.html",
                             title="Hello" + username,
                             myContent = "My SUPER content for" + username + "!!!")
