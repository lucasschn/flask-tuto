from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
   user = User.query.get(int(user_id))
   return user

class User(db.Model, UserMixin):
   """ Tablename will be automatically set to user """
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(20), unique=True, nullable=False)
   email = db.Column(db.String(120), unique=True, nullable=False)
   image_file = db.Column(db.String(20), nullable=False, default='default.jpeg')
   password = db.Column(db.String(60), nullable=False)
   posts = db.relationship('Post', backref='author', lazy=True) # one-to-many relationship. Not really a column but its call will run an additional query on the posts table.

   def __repr__(self):
      """ How our object is printed out when using the print method."""
      return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
   """ Tablename will be automatically set to post """
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(100), nullable=False)
   date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
   content = db.Column(db.Text, nullable=False)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

   def __repr__(self):
      """ How our object is printed out when using the print method."""
      return f"Post('{self.title}', '{self.date_posted}')"