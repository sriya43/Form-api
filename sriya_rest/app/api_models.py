from flask_restx import fields

from .extensions import api 

Form2_model = api.model("Form2", {
    "id": fields.Integer,
    "name": fields.String,
    #"Form1": fields.Nested(Form1_model)
})

Form1_model = api.model("Form1", {
    "id": fields.Integer,
    "name": fields.String,
    "Form2s": fields.List(fields.Nested(Form2_model))
})

Form1_input_model = api.model("Form1Input", {
    "name": fields.String,
})

Form2_input_model = api.model("Form2Input", {
    "name": fields.String,
    "Form1_id": fields.Integer
})