# coding=utf-8

from manage import orm


class Category(orm.Model):
    id = orm.Column(orm.Integer(12), primary_key=True)
    name = orm.Column(orm.String(255), unique=True, nullable=False)
    create_at = orm.Column(orm.TIMESTAMP, nullable=False)
    update_at = orm.Column(orm.TIMESTAMP, nullable=False)

    def __init__(self, name):
        self.name = name

