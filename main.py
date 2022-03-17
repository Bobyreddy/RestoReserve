from msilib.schema import tables
from flask import Flask, json, redirect, render_template, flash, request
from flask.globals import request, session
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import login_required, logout_user, login_user, login_manager, LoginManager, current_user

from flask_mail import Mail
import json


# mydatabase connection
local_server = True
app = Flask(__name__)
app.secret_key = "damara"


with open('config.json', 'r') as c:
    params = json.load(c)["params"]


app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail-user'],
    MAIL_PASSWORD=params['gmail-password']
)
mail = Mail(app)


# this is for getting the unique user access
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# app.config['SQLALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databsename'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/restaurant'
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) or Restouser.query.get(int(user_id))


class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email_id = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))


class Restouser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email_id = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(1000))


class Restodata(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_code = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    tables = db.Column(db.Integer)
    dishes = db.Column(db.Integer)


class Trig(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    r_code = db.Column(db.String(20))
    tables = db.Column(db.Integer)
    dishes = db.Column(db.Integer)
    querys = db.Column(db.String(50))
    date = db.Column(db.String(50))


class Bookinguser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    r_code = db.Column(db.String(50))
    ph = db.Column(db.Integer)
    address = db.Column(db.String(100))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/trigers")
def trigers():
    query = Trig.query.all()
    return render_template("trigers.html", query=query)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        name = request.form.get('name')
        email_id = request.form.get('email_id')
        password = request.form.get('password')
        encpassword = generate_password_hash(password)
        user = User.query.filter_by(name=name).first()
        emailUser = User.query.filter_by(email_id=email_id).first()
        if user or emailUser:
            flash("User Name or Email is already taken", "warning")
            return render_template("usersignup.html")
        new_user = db.engine.execute(
            f"INSERT INTO `user` (`name`,`email_id`,`password`) VALUES ('{name}','{email_id}','{encpassword}') ")

        flash("SignUp Success Please Login", "success")
        return render_template("userlogin.html")

    return render_template("usersignup.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        user = User.query.filter_by(name=name).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Success", "info")
            return render_template("index.html")
        else:
            flash("Invalid Credentials", "danger")
            return render_template("userlogin.html")

    return render_template("userlogin.html")


@app.route('/restologin', methods=['POST', 'GET'])
def restologin():
    if request.method == "POST":
        email_id = request.form.get('email_id')
        password = request.form.get('password')
        user = Restouser.query.filter_by(email_id=email_id).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login Success", "info")
            return render_template("index.html")

        else:
            flash("Invalid Credentials", "danger")
            return render_template("restologin.html")

    return render_template("restologin.html")


@app.route('/admin', methods=['POST', 'GET'])
def admin():

    if request.method == "POST":
        name = request.form.get('name')
        password = request.form.get('password')
        if(name == params['user'] and password == params['password']):
            session['user'] = name
            flash("login success", "info")
            return render_template("addRestoUser.html")
        else:
            flash("Invalid Credentials", "danger")

    return render_template("admin.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul", "warning")
    return redirect(url_for('login'))


@app.route('/addRestoUser', methods=['POST', 'GET'])
def restoUser():
    if('user' in session and session['user'] == params['user']):
        if request.method == "POST":
            r_code = request.form.get('r_code')
            name = request.form.get('name')
            email_id = request.form.get('email_id')
            password = request.form.get('password')
            encpassword = generate_password_hash(password)
            r_code = r_code.upper()
            emailUser = Restouser.query.filter_by(email_id=email_id).first()
            RUser = Restouser.query.filter_by(r_code=r_code).first()
            if emailUser or RUser:
                flash("Email or Resto Code is already taken", "warning")
                return render_template("addRestoUser.html")
            db.engine.execute(
                f"INSERT INTO `restouser` (`r_code`, `name`, `email_id`,`password`) VALUES ('{r_code}', '{name}', '{email_id}','{encpassword}') ")
            mail.send_message('Resto Reserve', sender=params['gmail-user'], recipients=[
                              email_id], body=f"Welcome thanks for choosing us\n\nYour Login Credentials Are:\n\n Email Address: {email_id}\nPassword: {password}\nResto Code: {r_code}\n\n Do not share your password\n\n\nThank You...")

            flash("Data Sent and Inserted Successfully", "warning")
            return render_template("addRestoUser.html")
    else:
        flash("Login and try Again", "warning")
        return render_template("addRestoUser.html")


# testing wheather db is connected or not
# @app.route("/test")
# def test():
#     try:
#         a = Test.query.all()
#         print(a)
#         return f'MY DATABASE IS CONNECTED'
#     except Exception as e:
#         print(e)
#         return f'MY DATABASE IS NOT CONNECTED {e}'


@app.route("/logoutadmin")
def logoutadmin():
    session.pop('user')
    flash("logout Success", "primary")

    return redirect('/admin')


@app.route("/addrestoinfo", methods=['POST', 'GET'])
def addrestolinfo():
    email_id = current_user.email_id
    posts = Restouser.query.filter_by(email_id=email_id).first()
    code = posts.r_code
    postsdata = Restodata.query.filter_by(r_code=code).first()

    if request.method == "POST":
        r_code = request.form.get('r_code')
        name = request.form.get('name')
        tables = request.form.get('tables')
        dishes = request.form.get('dishes')
        r_code = r_code.upper()
        ruser = Restouser.query.filter_by(r_code=r_code).first()
        rduser = Restodata.query.filter_by(r_code=r_code).first()
        if rduser:
            flash("Data is already Present you can update it..", "primary")
            return render_template("Restodata.html")
        if ruser:
            db.engine.execute(
                f"INSERT INTO `restodata` (`r_code`,`name`,`tables`,`dishes`) VALUES ('{r_code}','{name}','{tables}','{dishes}')")
            flash("Data Is Added", "primary")
            return redirect("/addrestoinfo")
        else:
            flash("Hospital Code not Exist", "warning")

    return render_template("restodata.html", postsdata=postsdata)


@app.route("/redit/<string:id>", methods=['POST', 'GET'])
@login_required
def redit(id):
    posts = Restodata.query.filter_by(id=id).first()
    if request.method == "POST":
        r_code = request.form.get('r_code')
        name = request.form.get('name')
        tables = request.form.get('tables')
        dishes = request.form.get('dishes')
        r_code = r_code.upper()
        rduser = Restodata.query.filter_by(r_code=r_code).first()
        code = rduser.r_code
        db.engine.execute(
            f"UPDATE `restodata` SET `r_code` ='{r_code}',`name`='{name}',`tables`='{tables}',`dishes`='{dishes}' WHERE `restodata`.`id`={id}")
        flash("Details Updated", "info")
        return redirect("/addrestoinfo")
    return render_template("redit.html", posts=posts)


@app.route("/rdelete/<string:id>", methods=['POST', 'GET'])
@login_required
def rdelete(id):
    db.engine.execute(
        f"DELETE FROM `restodata` WHERE `restodata`.`id`={id}")
    flash("Date Deleted", "danger")
    return redirect("/addrestoinfo")


@app.route("/userdetails", methods=['GET'])
@login_required
def userdetails():
    code = current_user.name
    print(code)
    data = Bookinguser.query.filter_by(name=code).first()

    return render_template("detials.html", data=data)


@app.route("/tablebooking", methods=['POST', 'GET'])
@login_required
def tablebooking():
    query = db.engine.execute(f"SELECT * FROM `restodata` ")
    if request.method == "POST":
        name = request.form.get('name')
        r_code = request.form.get('r_code')
        nop = request.form.get('nop')
        ph = request.form.get('ph')
        address = request.form.get('address')
        check2 = Restodata.query.filter_by(r_code=r_code).first()
        if not check2:
            flash("Resto Code not exist", "warning")
            return redirect("/tablebooking")

        code = r_code
        dbb = db.engine.execute(
            f"SELECT * FROM `restodata` WHERE `restodata`.`r_code`='{code}' ")

        for d in dbb:
            seat = d.tables
            ar = Restodata.query.filter_by(r_code=code).first()
            ar.tables = seat-1
            db.session.commit()

        check = Restodata.query.filter_by(r_code=r_code).first()
        if(seat > 0 and check):
            res = Bookinguser(name=name, r_code=r_code,
                              ph=ph, address=address)
            db.session.add(res)
            db.session.commit()
            flash("Table is Booked kindly Visit Restaurant!", "success")
            return redirect("/tablebooking")
        else:
            flash("Something Went Wrong", "danger")

    return render_template("booking.html", query=query)


app.run(debug=True)
