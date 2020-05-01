from config import db, login
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
import os

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(20), index=True)
    last_name = db.Column(db.String(20), index=True)
    position = db.Column(db.Integer, index=True)
    avail_restriction = db.relationship(
        'AvailRestriction', backref='user', lazy=True)
    request_offs =  db.relationship(
        'OffDays', backref='user', lazy=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return 'User {}'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_position(self):
        if self.position: return 'manager'
        return 'crew'
    def avatar(self):
        print(os.path.exists('static/images/Skull Icon.png'))
        return '/static/images/Skull Icon.png'


class AvailRestriction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    weekday = db.Column(db.Integer, index=True)
    start_time = db.Column(db.Integer)
    end_time = db.Column(db.Integer)

    def __repr__(self):
        return 'Cannot Work {}'.format(self.weekday)


class OffDays(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    day = db.Column(db.Integer, index=True)
    month = db.Column(db.Integer, index=True)
    year = db.Column(db.Integer, index=True)

    def __repr__(self):
        return 'Request Off {}/{}/{}'.format(self.month, self.day, self.year)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
 