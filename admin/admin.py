# coding=utf-8

from manage import orm


class Admin(orm.Model):
    id = orm.Column(orm.Integer(12), primary_key=True)
    username = orm.Column(orm.String(24), unique=True, nullable=False)
    password = orm.Column(orm.String(24), nullable=False)
    create_at = orm.Column(orm.TIMESTAMP, nullable=False)
    update_at = orm.Column(orm.TIMESTAMP, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

