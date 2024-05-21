from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    appointments = db.relationship("Appointment")


class Appointment(db.Model):

    __tablename__ = "appointments"

    appointment_id = db.Column(db.Integer, autoincrement=True,primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.user_id'),nullable=False)
    mani_type = db.Column(db.String(200), nullable=False)
    mani_color = db.Column(db.String(200), nullable=False)
    mani_shape = db.Column(db.String(200), nullable=False)
    pedi = db.Column(db.String(200), nullable=False)
    pedi_color = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(200), nullable=False)
    time = db.Column(db.String(200), nullable=False)

    user = db.relationship("User")







def connect_to_db(app):
    """Connect the database to our Flask app."""

    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///salon'
    app.config["SQLALCHEMY_ECHO"] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    db.app = app   
    db.init_app(app)

    

if __name__ == "__main__":
   
    from server import app
    connect_to_db(app)
    print("Connected to DB.")
