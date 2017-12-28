from application import db
from datetime import datetime

ROLE_USER = 0
ROLE_ADMIN = 1

class Post(db.Model):
    # __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Post: title: {}".format(self.title)


class User(db.Model):
    # __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role = db.Column(db.SmallInteger, default=ROLE_USER)

    def __init__(self, nickname, email, password):
        self.nickname = nickname
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def is_active(self):
        return True

    def get_id(self):
        return unicode(self.id)

    def is_authenticated(self):
        return True