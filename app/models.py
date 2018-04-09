#!/usr/bin/env python3

import pymysql as sq1
from flask import Flask, render_template, request, jsonify, session
import pymysql.cursors
import traceback
from config import *

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
            cursor.execute("SELECT password FROM user WHERE password = %s", (password))
            row = cursor.fetchone()
            if (row[0] == password):
                return True
    return False    

def check_login(username, password):
    abool = False
    try:
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
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
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
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

def add_task(title, begin, end, status):
    err = {"error" : "internal error"}
    result = {"result" : "new task added"}
    try:
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
        with conn.cursor() as cursor:
            sql = "INSERT INTO task (title, begin, end, status) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (title, begin, end, status))
            conn.commit()
            conn.close()
    except:
        traceback.print_exc() 
    return jsonify(result)

def del_task(task_id, username):
    try:
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
        with conn.cursor() as cursor:
            #DEL LA TASK SI L'UTILISATEUR LA DETIEN ET SI ELLE EXISTE
            plop = "plop"
    except:
        traceback.print_exc()
    return jsonify(plop)
            
def modif_task(task_id, username):
    try:
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
        with conn.cursor() as cursor:
            plop = "plop"
        #MODIF LA TASK DE L'USER PAR SON ID SI IL DETIENT LES DROIT ET SI ELLE EXISTE
    except:
        traceback.print_exc()
    return jsonify(plop)

def get_user_data():
    _username = session.get('username')
    _user_id = 0
    _password = 0
    try:
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM user WHERE username = %s", (_username))
            rows = cursor.fetchall()
            _user_id = rows[0][0]
            _password = rows[0][2]
            conn.close()            
    except:
        traceback.print_exc()
    return (["User ID : " + str(_user_id), "Username : " + _username, "Password : " + _password])

def get_user_task():
    _username = session.get('username')
    _user_id = 0
    _fk_task_id = 0
    try:
        conn = sq1.connect(host=DATABASE_HOST,
                           user=DATABASE_USER,
                           unix_socket=DATABASE_SOCK,
                           passwd=DATABASE_PASS,
                           db=DATABASE_NAME)
        cursor = conn.cursor()
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM user WHERE username = %s", (_username))
            rows = cursor.fetchall()
            _user_id = rows[0][0]
            cursor.execute("SELECT fk_task_id FROM user WHERE fk_user_id = %s", (_username))
            rows = cursor.fetchall()
            _fk_task_id = rows
    except:
        traceback.print_exc()
