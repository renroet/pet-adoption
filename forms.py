from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators, BooleanField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """form for user to add pet for adoption"""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired(),
                        AnyOf(values=['dog', 'cat', 'porcupine'])])
    photo = StringField("Photo URL",
                        validators=[URL(), Optional()])
    age = IntegerField("Age in Years",
                        validators=[NumberRange(min=0), Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])
    
    
class EditPetForm(FlaskForm):
    """form for user to update pet info"""

    name = StringField("Pet Name",
                        validators=[InputRequired()])
    species = StringField("Species",
                        validators=[InputRequired(),
                        AnyOf(values=['dog', 'cat', 'porcupine'])])
    photo = StringField("Photo URL",
                        validators=[URL(), Optional()])
    age = IntegerField("Age in Years",
                        validators=[NumberRange(min=0) ,Optional()])
    notes = StringField("Notes",
                        validators=[Optional()])
    available = BooleanField("Available for Adoption",
                            validators=[Optional()])
