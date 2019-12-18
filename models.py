from app import db

class Result(db.Model):
    __tablename__ = "LinRegResults"

    id = db.Column(db.Integer, primary_key = True)
    YearsExperience = db.Column(db.Float)
    Prediction = db.Column(db.Float)

    def __init__(self, YearsExperience, Prediction):
        self.YearsExperience = YearsExperience
        self.Prediction = Prediction

    def __repr__(self):
        return '<id {}>'.format(self.id)
