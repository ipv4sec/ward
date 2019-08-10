# coding: utf-8

from flask import Blueprint

literature = Blueprint('literature', __name__)


@literature.route('/')
def index():
    return "kasakei"
