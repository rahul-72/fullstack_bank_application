from flask import Flask, render_template, request
app=Flask(__name__)
location_bank= "D:\\data_science\\github\\fullstack_projects\\bank\\static\\data\\bank"
location_bank_log=" D:\\data_science\\github\\fullstack_projects\\bank\\static\\data\\bank_log"


"""                 ********************************************************************** """

import json,time,os,sys         #importing useful libraries....
from random import randint
from getpass import getpass


@app.route('/')
def index():
    return render_template('index.html', title='XYZ Bank')

@app.route('/login/', methods=["POST"])
def login():
    """1st we will get username and password from
    request module and then we will check them in
    our database."""
    username=request.form["username"].strip().lower()
    password=request.form["password"]
    for user in os.listdir(location_bank):
                if username==user:
                    f=open(os.path.join(location_bank,username))
                    data=json.load(f)
                    f.close()
                    if password== data['password']:
                        return render_template("login.html", title="Login", data=data)
                    else:
                        error="Invalid Password"
                        return render_template("index.html", title="XYZ Bank", error=error)
    else:
        error="Username does not exits"
        return render_template("index.html", title="XYZ Bank", error=error)                      
            

                       
@app.route('/debit/')
def debit():
    return render_template('debit.html', title='Debit'data=data)
@app.route('/debit_amount/')
def debit_amount:
    amount=request.form['amount']
    if data['bal']>amount:
        msg=f'Amount Rs {amount} are debited from your account'
        return render_template('login.html',title='Login',msg=msg)
    else:
        msg='You does not have sufficient amount.'
        return render_template('login.html',title='Login',msg=msg)

if __name__=="__main__":
    app.run('localhost',5000,debug=True)