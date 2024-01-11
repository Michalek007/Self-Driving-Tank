from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow

from configuration import Config

app = Flask(__name__)

app.config.from_object(Config)

jwt = JWTManager(app)
bcrypt = Bcrypt(app)
ma = Marshmallow(app)

from app.views import *
from app.acc_views import *
from app.position_views import *
from app.velocity_views import *
from app.controls_views import *
from app.gui_views import *
from database.cli_commands import *
