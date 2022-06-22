from flask import Flask,session,redirect,url_for, render_template,flash,request
import mysql.connector as mysql
import bcrypt as code

school = Flask(__name__)
school.secret_key = 'mukoko mbala gracia'


"""
*********************************************************************
    partie de la connection avec mon data
    
*********************************************************************
""" 


sql = mysql.connect(host='localhost',user = 'linux',password = 'data',database = 'school')


"""

*********************************************************************

    page d'accueil du plate-forme 
    
*********************************************************************
""" 


@school.route('/')
@school.route('/index')
def index():
    return render_template('school.html')



@school.route('/about')
def about():
    return render_template('about.html')

@school.route('/events')
def events():
    return render_template('events.html')




"""

*********************************************************************

    page login admin
    
*********************************************************************
""" 

@school.route('/home',methods=['GET','POST'])
def home():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        user   = request.form.get('email')
        login  = request.form.get('password')
        
        cur = sql.cursor()
        cur.execute("SELECT * FROM userAdmin where email_admin = %s AND password_admin = %s ",
                    (user,login,))
        
        query = cur.fetchone()
        b = query[1]
        cur.close()
        
        
        
        if len(query) > 0:
            session['nameAdm'] = query[1]
            session['adminUserLogin'] = True
            
            
            # session['username_admin'] = query['username_admin']
            return redirect(url_for('admin'))
        
        
    return render_template('home.html')

"""
*********************************************************************
    partie parents_form
    
*********************************************************************
""" 

"""
*********************************************************************
    partie administration
    
*********************************************************************
""" 


@school.route('/admin')
def admin():
    
    if 'nameAdm' in session:
        v = session['nameAdm']
        return render_template('index.html',user = session['nameAdm']) 
    else:
        return redirect(url_for('home'))


@school.route('/deco')

def deco():
    session.clear()
    return redirect(url_for('home'))




if __name__ == '__main__':
    school.run(debug=True)
    
    
    