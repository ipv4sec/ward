# coding: utf-8

from manage import orm


class Literature(orm.Model):
    id = orm.Column(orm.Integer(11), primary_key=True)
    author_id = orm.Column(orm.Integer(11), nullable=False)    #作者
    category_id = orm.Column(orm.Integer(11), nullable=False)  # 文献格式

    abstract = orm.Column(orm.Text, nullable=False) # 摘要
    ei = orm.Column(orm.String(255), nullable=False) # EI
    citations = orm.Column(orm.String(255), nullable=False) # 引用
    publish_in = orm.Column(orm.String(255), unique=True, nullable=False) # 发表期刊
    class_index = orm.Column(orm.String(255), unique=True, nullable=False)  # 分类号
    popular_word = orm.Column(orm.String(255), unique=True, nullable=False)  # 热词
    doi = orm.Column(orm.String(255), unique=True, nullable=False)  # DOI

    year = orm.Column(orm.TIMESTAMP, nullable=False)  # 年份
    create_at = orm.Column(orm.TIMESTAMP, nullable=False)
    update_at = orm.Column(orm.TIMESTAMP, nullable=False)

    def __init__(self, name):
        self.name = name
