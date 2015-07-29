from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.bootstrap import Bootstrap
from flask.ext.login import LoginManager
app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB':"tieba"}
app.config["SECRET_KEY"] = "This_sc3r3t_my~key"

bootstrap = Bootstrap()
bootstrap.init_app(app)
db = MongoEngine(app)
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from .main import main as main_blueprint
app.register_blueprint(main_blueprint)

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix="/auth")


if __name__ == "__main__":
    app.run()
