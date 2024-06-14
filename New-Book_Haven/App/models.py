from werkzeug.security import generate_password_hash, check_password_hash
from App import db
from flask_login import UserMixin
from App import login




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False) 
    
    
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


    def __repr__(self):
        return f"<User {self.username}>"
    


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
