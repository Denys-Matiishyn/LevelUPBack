from database import db

class Service(db.Model):
    __tablename__ = 'services'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Reviews', backref='service', lazy=True)
