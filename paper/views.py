# coding: utf-8

from flask import Blueprint

paper = Blueprint('paper', __name__)


@paper.route('/')
def index():
    return "kasakei"
