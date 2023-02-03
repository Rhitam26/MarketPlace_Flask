# from crypt import methods
from re import X
from webbrowser import get
from market import app
from flask import render_template, flash
from market.forms import RegisterForm, LogInForm
from market import mongo
from market.model import Users
from flask import request
@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/market')
def market_place():
    
    db= mongo["items"]
    dictItems= db["items"].find()
    items=[]
    print(dictItems)
    for i in dictItems:
        i['id'] = str(i['_id'])
        i.pop('_id')
        print(i)
        items.append(i)

    return render_template('market.html', items= items)

@app.route('/register', methods=['POST','GET'])
def register_form():
    form = RegisterForm()
    print("**********before validate on submit*********")
    print(form.validate_on_submit())
    if request.method == 'POST' :
        if(form.validate_on_submit()):
            if form.errors!= {}:
                for err_message in form.errors.values():
                    print(err_message)
                    flash("There was an error while creting user : "+str(err_message), category='danger')
                return render_template('register.html', form = form)
            else:
                print("************after submit***********")
                print(form.email_id.data)
                print(form.password1.data)
                Users(username=form.username.data, email=form.email_id.data, password=form.password1.data)
                print("************ onj created ***********")
                # user_to_create()
                print("************done***********")
                # return redirect
    return render_template('register.html', form = form)


@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LogInForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        db = mongo['DbUsers']
        collection= db['users']
        print(form.username.data)
        userdict={}
        userdict= collection.find_one({"username":str(form.username.data)})
        userlst=[]
        print(len(userdict))
        for i in userdict:
            print(i)
            userlst.append(i)
        print(userlst)
        print(Users.check_pasword_correction(attempedPassword=form.password.data))
        if(len(userlst)==0 and Users.check_pasword_correction(attempedPassword=form.password.data)):
            print("User Not there")
        else:
            print("User Is Present") 
            

    return render_template('login.html', form= form)

