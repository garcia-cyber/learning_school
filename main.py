from flask import Flask,session,redirect,url_for, render_template,flash,request
import mysql.connector as mysql
import bcrypt as code

school = Flask(__name__)

@school.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        user   = request.form.get('email')
        login  = request.form.get('password')
        
        
        
    return render_template('home.html')

"""
*********************************************************************
    partie administration
    
*********************************************************************
""" 

@school.route('/')
@school.route('/admin')
def admin():
    return render_template('index.html')




if __name__ == '__main__':
    school.run(debug=True)
    
    
    