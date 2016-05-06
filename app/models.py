from app import db
from hashlib import md5


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property  # Required by Flask-Login
    def is_authenticated(self):
        return True

    @property  # Required by Flask-Login
    def is_active(self):
        return True

    @property  # Required by Flask-Login
    def is_anonymous(self):
        return False

    def get_id(self):  # Required by Flask-Login
        return str(self.id)  # python 3

    def avatar(self, size):
        gravurl = 'http://www.gravatar.com/avatar/{}?d=mm&s={:d}'
        return gravurl.format(md5(self.email.encode('utf-8')).hexdigest(),
                              size)

    def __repr__(self):
        """How obijects of the class are printed"""
        return '<User {}>'.format(self.nickname)


class Post(db.Model):
    """Represents a content post by one author"""
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        """How posts are printed to the screen"""
        return '<Post {}>'.format(self.body)
