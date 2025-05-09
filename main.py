from flask import Flask
from flask_restx import Api, Resource
from database.exts import db
from config import DevConfig
from database.db_init import db

app = Flask(__name__)
api = Api(app, doc="/docs", prefix="/api")

app.config.from_object(DevConfig)

#initialize the database
db.init_app(app)

@api.route("/hello")
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello My Fucking World"}

@app.route("/")
def home():
    return "Hello My Fucking World"

if __name__ == "__main__":
    app.run(debug=True)