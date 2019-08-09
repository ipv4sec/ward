# coding=utf-8

from manage import orm


class Tenure(orm.Model):
    id = orm.Column(orm.Integer(12), primary_key=True)
    author_id = orm.Column(orm.Integer(11), nullable=False)
    organization_id = orm.Column(orm.Integer(11), nullable=False)
    create_at = orm.Column(orm.TIMESTAMP, nullable=False)
    update_at = orm.Column(orm.TIMESTAMP, nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password

