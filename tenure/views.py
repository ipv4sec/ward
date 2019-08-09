# coding: utf-8

from flask import Blueprint

tenure = Blueprint('tenure', __name__)


@tenure.route('/')
def index():
    return "kasakei"

