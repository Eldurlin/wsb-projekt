from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///variables.db"
app.config["SECRET_KEY"] = "e2d591d71c884e551ab61f48"

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from calc import routes
