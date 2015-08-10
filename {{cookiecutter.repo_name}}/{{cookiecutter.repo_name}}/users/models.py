from muffin.utils import (
    generate_password_hash,
    check_password_hash
)
import peewee

from .. import app


@app.ps.peewee.register
class User(peewee.Model):
    email = peewee.CharField(primary_key=True)
    name = peewee.CharField()
    password = peewee.CharField()

    @classmethod
    def generate_password(cls, raw_password):
        return generate_password_hash(raw_password)

    def check_password(self, raw_password):
        return check_password_hash(raw_password, self.password)


@app.ps.session.user_loader
def get_user(user_email):
    return User.get(User.email == user_email)
