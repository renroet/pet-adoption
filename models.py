from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet info"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(30),
                     nullable=False)
    species = db.Column(db.String(20), 
                    nullable=False)
    photo_url = db.Column(db.Text,
                    default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ80L0Mdn36yMy2cSqdmkQPHjuTaUx3bgcQLx6Kpx3Omw&usqp=CAU&ec=48600113")
    age = db.Column(db.Integer)
    notes = db.Column(db.String)
    available = db.Column(db.Boolean,
                        nullable=False,
                        default=True)