# coding: utf-8

from flask import Blueprint

author = Blueprint('author', __name__)


@author.route('/')
def index():
    return "kasakei"
