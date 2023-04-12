from . import db



class Hospital(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200))
    hospital_name = db.Column(db.String(150), unique=True)
    beds = db.Column(db.Integer)


