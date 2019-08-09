# coding: utf-8

from flask import Blueprint

organization = Blueprint('organization', __name__)


@organization.route('/')
def index():
    return "kasakei"
