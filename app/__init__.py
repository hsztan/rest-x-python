from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restx import Api, Resource

# Flask
app = Flask(__name__)
app.config.from_object(Config)

# SQLAlchemy
db = SQLAlchemy(app)

# Migrate
migrate = Migrate(app, db)

# Marshmallow
ma = Marshmallow(app)

# FlaskRestX
api = Api(app,
          version='0.1',
          title='IDAT Api',
          description='Documentación RESTAPI Semana 12',
          prefix='/api/',
          doc='/docs/',
          contact='Henry Nawrocki',
          contact_email='hdev@sztanski.com')
