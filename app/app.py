from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .config import Config

flask_app = Flask(__name__)
flask_app.config.from_object(Config)
db = SQLAlchemy(flask_app)
migrate = Migrate(flask_app, db)

from .models import Category, Product, Basket, BasketStorage
# from app.views import *

if __name__ == "__main__":
    flask_app.run(host='localhost', port=8000)
