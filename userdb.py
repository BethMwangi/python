#RESTful authentfication with flask
#storing the users using Flask-SQLAlchemy
from passlib.apps import custom_app_context as pwd_context

class User(db.Model):

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        
    def verify_password(self, password): # verify method takes a plain pswd as argument and returns True if pswd is correct or False if pswd is wrong 
        return pwd_context.verify(password, self.password_hash) #hash_password() takes a plain argument of the pswd and stores a hash of it 
        
        
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column (db.String(32), index = True)
    password_hash = db.Column(db.String(123))
