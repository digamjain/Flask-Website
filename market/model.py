from market import db
from market import bcrypt

class User(db.Model):
	id = db.Column(db.Integer(),primary_key = True)
	username = db.Column(db.String(length = 24),nullable=False,unique = True)
	email = db.Column(db.String(length = 70),nullable = False,unique = True)
	hash_password = db.Column(db.String(length = 60),nullable=False)
	budget = db.Column(db.Integer(), nullable = False, default = 1000)
	items = db.relationship('Item', backref = 'owned_user', lazy = True)

    #Returns the username of the User
	def __repr__(self):
		return f'username {self.hash_password}'

	#Decorator property to return password to instances
	@property
	def password(self):
		return self.password

	#Decorator to execute code before we set a password
	@password.setter
	#plain_text_password is the filled in password
	def password(self, plain_text_password):
		#Assign hash_password field a hashed password generated from bcrypt instance
		self.hash_password = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

class Item(db.Model):
    id = db.Column(db.Integer(),primary_key = True)
    name = db.Column(db.String(length = 30),nullable = False, unique = True)
    price = db.Column(db.Integer(), nullable = False)
    barcode = db.Column(db.String(length = 12), nullable = False, unique = True)
    description = db.Column(db.String(length = 1024), nullable = False, unique = True)
    owner = db.Column(db.Integer(),db.ForeignKey('user.id'))

    #To get the string representation of the database
    #Returns the name of the item
    def __repr__(self):
        return f'Item: {self.name}'
