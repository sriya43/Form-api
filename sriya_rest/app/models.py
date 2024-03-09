from .extensions import db 

class Form1(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    
    Forms2 = db.relationship("Form2", back_populates="Form1")


class Form2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    Form1_id = db.Column(db.ForeignKey("Form1.id"))

    Form1 = db.relationship("Form1", back_populates="Forms1")