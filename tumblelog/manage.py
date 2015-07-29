# Set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server, Shell
from flask.ext.moment import Moment
from APP import app, db, models

manager = Manager(app)
moment = Moment(app)

def make_context():
	return dict(app=app, db=db, User=models.User)
# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

manager.add_command("shell", Shell(make_context = make_context))
if __name__ == "__main__":
    manager.run()