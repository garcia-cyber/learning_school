from flask import Flask,session,redirect,url_for, render_template,flash
import mysql.connector as mysql
import bcrypt as code

school = Flask(__name__)

@school.route('/')
def home():
    return render_template('home.html')











if __name__ == '__main__':
    school.run(debug=True)