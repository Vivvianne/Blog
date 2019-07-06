from flaskblog import create_app, db
from flask_script import Manager, Server
from flaskblog.models import User,Post

from flask_migrate import Migrate, MigrateCommand

from app import app, db

app = create_app('development')
#app = create_app('production')
app.config.from_object(os.environ['APP_SETTINGS'])

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)
    