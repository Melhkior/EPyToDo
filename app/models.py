#!/usr/bin/env python3

import pymysql as sq1
from flask import Flask, render_template, request, jsonify
import pymysql.cursors
import traceback

def insert_value(id, username, password):
    
    cursor.execute("INSERT INTO user (username) VALUES(%s)"("Oh no"))
    connect.commit()
    
def check_user_exsit(username, cursor):
    cursor.execute("SELECT * FROM user")
    rows = cursor.fetchall()
    for i in rows:
        if (rows[i] == username):
            return True
        return False

def register(username, password):
    result = ""
    try:
        conn = sq1.connect(host='localhost',
                           user='root',
                           unix_socket='/var/lib/mysql/mysql.sock',
                           passwd='El_000_153',
                           db='epytodo')
        with conn.cursor() as cursor:
            sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
            cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
            conn.commit()
        conn.close()
        return "Error"       
#        return "Saved successfully"
    except :
        traceback.print_exc()
    return jsonify(result)
