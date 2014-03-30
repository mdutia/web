from flask import render_template, flash, redirect, session, url_for, g, request
from flask.ext.login import login_user , logout_user , current_user , login_required

from app import app
from forms import LoginForm, SelectGroupMemberForm, EvaluationForm
from app import db, Criteria

#import os, sys


@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    from app import User
    #user= os.getenv("USERNAME")
    #session['username']=user
    form = LoginForm()
    if form.validate_on_submit():
        username= form.uname.data
        password= form.pwd.data
        registered_user = User.query.filter_by(username=username,pwd=password).first()
        if registered_user is None:
            return redirect(url_for('login'))
        login_user(registered_user)
        session ['this_user_matric']= registered_user.matric
        user_group_members = User.query.filter_by(groupnumber=current_user.groupnumber).all()
        s=''
        for m in user_group_members:
            s= s + ' ' + str(m.id)
        session ['user_group_members'] = s.strip()
        #flash('Logged in successfully')
        return redirect( url_for('index'))
    return render_template('login.html', title = 'Sign In', form = form)


@app.route('/finished', methods = ['GET', 'POST'])
@login_required
def finished():
    logout_user()
    return render_template ('finished.html')


@login_required
@app.route('/index', methods = ['GET', 'POST'])
def index():
    from app import User
    #retrieve the names of current_user's group members
    s= session ['user_group_members']
    s=s.split(' ')
    user_group_members=[]
    for id in s:
        user_group_members.append (User.query.get(int(id)))
    #use these names as choice list for radio buttons
    choicelist=[]
    for ind, u in enumerate(user_group_members) :
        s= u.firstname+' '+u.lastname+' ('+u.matric+')    '#+u.status
        choicelist.append ( (str(ind), s) )
    #offer and validate form to select the student to mark
    form= SelectGroupMemberForm()
    form.selected.choices= choicelist
    if (request.method=='POST'):
        print request.form ['Button']
        if (request.form ['Button']!=' Select '):
            return redirect(url_for('finished'))
    #if form.validate_on_submit():
        elif form.selected.data != 'None':
            session ['selected_user']= user_group_members[int(form.selected.data)].id
            return redirect(url_for('evaluser'))
    form.selected.data='0'  #default select first name in the list
    return render_template("index.html", title = 'Home', user=current_user, form=form)


@app.route('/evaluser', methods = ['GET', 'POST'])
@login_required
def evaluser():
    from app import User, Evaluation
    this_user_matric= session ['this_user_matric']
    su = int(session ['selected_user'])
    selected_user= User.query.get (su)
    selected_user_name= selected_user.firstname + ' ' + selected_user.lastname \
        + ' (' + selected_user.matric + ')'
    selected_evaluation= Evaluation.query.filter_by (
        markee_matric= selected_user.matric,
        marker_matric= this_user_matric).first()
    form= EvaluationForm(method= 'POST', obj=selected_evaluation)
    if not form.validate_on_submit():
        #selected_user.status='ToDo'
        #db.session.commit()
        return render_template('evaluser.html', title = 'Evaluate', selecteduser= selected_user_name,
                               criteria= Criteria, form=form)
    selected_user.status='Completed'
    if selected_evaluation==None:  #new evaluation, did not exist before
        selected_evaluation= Evaluation (
            selected_user.matric, this_user_matric,
            int(form.m1.data), int(form.m2.data), int(form.m3.data),
            int(form.m4.data), int(form.m5.data), form.j1.data )
        db.session.add (selected_evaluation)
    else:
        form.populate_obj (selected_evaluation)
    db.session.commit()
    return redirect(url_for('index'))


