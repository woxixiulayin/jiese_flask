from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB':"tieba"}
app.config["SECRET_KEY"] = "This_sc3r3t_my~key"

db = MongoEngine(app)


if __name__ == "__main__":
    app.run()
