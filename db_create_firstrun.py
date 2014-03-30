from app import db, User, Evaluation

db.create_all()

#admin = User('admin', 'admin','admin', 'admin', -1, None)
#guest = User('guest', 'guest','guest', 'guest', -1, None)

#db.session.add (admin)
#db.session.add (guest)

with open ('ClassList.txt') as f:
    classlist= f.readlines()

status= 'ToDo'
for line in classlist:
    lin= line.strip().split(',')
    if len(lin)>1:  #empty line has len==1
        uname, pwd, fname, lname, matric, gpNo = lin
        db.session.add (User(uname, pwd, fname, lname, matric, gpNo, status) )

db.session.commit()


