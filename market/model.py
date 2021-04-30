from market import db
from market import bcrypt
from market import login_manager
# To inherit import required flask_login classes
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=24), nullable=False, unique=True)
    email = db.Column(db.String(length=70), nullable=False, unique=True)
    hash_password = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    #To check if the user have enough budget to purchae the item
    def can_purchase(self,item_obj):
        return self.budget >= item_obj.price

    # Returns the username of the User
    def __repr__(self):
        return self.username

    # Decorator property to return password to instances
    @property
    def password(self):
        return self.password

    # Decorator to execute code before we set a password
    @password.setter
    # plain_text_password is the filled in password
    def password(self, plain_text_password):
        # Assign hash_password field a hashed password generated from bcrypt instance
        self.hash_password = bcrypt.generate_password_hash(
            plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.hash_password, attempted_password)

    #To format the user budget
    @property
    def format_budget(self):
        temp_lis = list(str(self.budget))
        start = 2
        if len(temp_lis)>3:
            if len(temp_lis)%2==0:
                start = 1
            inc = 0
            for i in range(start,len(temp_lis)-1,2):
                temp_lis.insert(i+inc,',')
                inc+=1
        return "₹"+"".join(temp_lis)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(length=1024),
                            nullable=False, unique=True)
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))

    # To get the string representation of the database
    # Returns the name of the item
    def __repr__(self):
        return f'Item: {self.name}'

    #Function to assign ownership to a user
    def assign_owner(self,user_obj):
        self.owner = user_obj.id
        user_obj.budget -= self.price
        db.session.commit()
