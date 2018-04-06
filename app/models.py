#!/usr/bin/env python3

import pymysql as sq1
from flask import Flask, render_template, request, jsonify, session
import pymysql.cursors
import traceback

def has_connect():
    if 'username' in session:
        return True
    return False

def user_exist(username, cursor):
    cursor.execute("SELECT username FROM user")
    row = cursor.fetchone()
    for row in cursor:
        if (row[0] == username):
            return True
    return False

def password_exist(username, password, cursor):
    nb = 0
    cursor.execute("SELECT username FROM user")
    row = cursor.fetchone()
    for row in cursor:
        nb += 1
        if (row[0] == username):
            print('OUI')
            cursor.execute("SELECT password FROM user WHERE password = %s", (password))
            row = cursor.fetchone()
            if (row[0] == password):
                print('OK')
                return True
    return False    

def check_login(username, password):
    abool = False
    try:
        print('HELLO')
        conn = sq1.connect(host='localhost',
                           user='root',
                           unix_socket='/var/lib/mysql/mysql.sock',
                           passwd='El_000_153',
                           db='epytodo')
        with conn.cursor() as cursor:
            if user_exist(username, cursor) == True and password_exist(username, password, cursor) == True:
                abool = True
        conn.close()
    except :
        traceback.print_exc()
    return (abool)

def register(username, password):
    err = {"error" : "account already exists"}
    res = {"result" : "account created"}
    result = {"error" : "internal error"}
    try:
        conn = sq1.connect(host='localhost',
                           user='root',
                           unix_socket='/var/lib/mysql/mysql.sock',
                           passwd='El_000_153',
                           db='epytodo')
        with conn.cursor() as cursor:
            if user_exist(username, cursor) == False:
                sql = "INSERT INTO user (username, password) VALUES (%s, %s)"
                cursor.execute(sql, (username, password))
                conn.commit()
                result = res
            else:
                result = err
            conn.close()
    except :
        traceback.print_exc()
    return jsonify(result)
