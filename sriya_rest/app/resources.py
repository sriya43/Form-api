from flask_restx import Resource, Namespace 

from .api_models import Form1_model, Form2_model, Form1_input_model, Form2_input_model
from .extensions import db
from .models import Form1, Form2

ns = Namespace("api")

@ns.route("/submission")
class submission(Resource):
    def get(self):
        return {"submission": "restx"}

@ns.route("/Forms1")
class Form1ListAPI(Resource):
    @ns.marshal_list_with(Form1_model)
    def get(self):
        return Form1.query.all()

    @ns.expect(Form1_input_model)
    @ns.marshal_with(Form1_model)
    def post(self):
        Form1 = Form1(name=ns.payload["name"])
        db.session.add(Form1)
        db.session.commit()
        return Form1, 201

@ns.route("/Forms1/<int:id>")
class Form1API(Resource):
    @ns.marshal_with(Form1_model)
    def get(self, id):
        Form1 = Form1.query.get(id)
        return Form1

    @ns.expect(Form1_input_model)
    @ns.marshal_with(Form1_model)
    def put(self, id):
        Form1 = Form1.query.get(id)
        Form1.name = ns.payload["name"]
        db.session.commit()
        return Form1

    def delete(self, id):
        Form1 = Form1.query.get(id)
        db.session.delete(Form1)
        db.session.commit()
        return {}, 204


@ns.route("/Forms2")
class Form2ListAPI(Resource):
    @ns.marshal_list_with(Form2_model)
    def get(self):
        return Form2.query.all()

    @ns.expect(Form2_input_model)
    @ns.marshal_with(Form2_model)
    def post(self):
        Form2 = Form2(name=ns.payload["name"], Form1_id=ns.payload["Form1_id"])
        db.session.add(Form2)
        db.session.commit()
        return Form2, 201


@ns.route("/Forms2/<int:id>")
class Form2API(Resource):
    @ns.marshal_with(Form2_model)
    def get(self, id):
        Form2 = Form2.query.get(id)
        return Form2

    @ns.expect(Form2_input_model)
    @ns.marshal_with(Form2_model)
    def put(self, id):
        Form2 = Form2.query.get(id)
        Form2.name = ns.payload["name"]
        Form2.Form1_id = ns.payload["Form1_id"]
        db.session.commit()
        return Form2

    def delete(self, id):
        Form2 = Form2.query.get(id)
        db.session.delete(Form2)
        db.session.commit()
        return {}, 204