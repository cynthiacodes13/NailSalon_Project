from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined

from model import connect_to_db, db, User, Appointment


app = Flask(__name__)



app.secret_key = "ABC"


app.jinja_env.undefined = StrictUndefined


@app.route('/') 
def index():
    """Homepage."""
  
    return render_template("homepage.html")


@app.route('/register', methods=['GET'])
def register_form():
    
    return render_template("register_page.html")    


@app.route('/register', methods=['POST'])
def registeration_process():

    username = request.form["username"]
    password = request.form["password" ]

    new_user = User(username=username,password=password)
    db.session.add(new_user)
    db.session.commit()
    
    flash(f"User has been registered")
    return redirect("/")   

@app.route('/signin', methods=['GET'])
def sign_form():
    
    return render_template("signin_page.html") 


@app.route('/signin', methods=['POST'])
def registeration_check():

    username = request.form["username"]
    password = request.form["password" ]

    user = User.query.filter_by(username=username).first()

    if not user:
        flash("User does not exist")
        return redirect("/register")

    if user.password != password:
        flash("Invalid password")
        return redirect ("/register")

    session["user_id"] = user.user_id


    flash("Signed In")
    return redirect(f"/users/{user.user_id}") 

@app.route("/users/<int:user_id>")
def user_page(user_id):

    user = User.query.get(user_id)
    

    return render_template("user_page.html",user=user) 


@app.route('/appointment', methods=['GET'])
def appointment_page():
    user_id = session["user_id"]
    user = User.query.filter_by(user_id=user_id).first()



    return render_template("appointment_page.html", user_name=user.username)    


@app.route('/appointment', methods=['POST'])
def appointment_process():
    user_id = session["user_id"]
    user = User.query.filter_by(user_id=user_id).first()
    

    mani_type = request.form["manitype"]
    mani_color = request.form["manicolor"]
    mani_shape = request.form["manishape"]
    pedi = request.form["pedi"]
    pedi_color = request.form["pedicolor"]
    date = request.form["date"]
    time = request.form["time"]

    new_appointment = Appointment(user_id=user_id,mani_type=mani_type,mani_color=mani_color,mani_shape=mani_shape,pedi=pedi,pedi_color=pedi_color,date=date,time=time)
    db.session.add(new_appointment)
    db.session.commit()
    
    return render_template("user_appointment_page.html",user = user)









if __name__ == '__main__':
   
    app.debug = True
   
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

 

    app.run(debug=True, host="0.0.0.0")