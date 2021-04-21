from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__) # __name__ is a special variable of python describing the name of the module
app.config['SECRET_KEY'] = '6bf85e90939d48fab99c45f1f2e6010f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes

"""
.
├── Dockerfile
├── flaskblog
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── routes.py
|   ├── site.db
│   ├── static
│   │   └── main.css
│   └── templates
│       ├── about.html
│       ├── gimmemore.html
│       ├── home.html
│       ├── layout.html
│       ├── login.html
│       └── register.html
└── site.db

"""