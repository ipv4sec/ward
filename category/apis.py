# coding: utf-8

from flask import Blueprint

category = Blueprint('category', __name__)


@category.route('/')
def index():
    return "kasakei"

