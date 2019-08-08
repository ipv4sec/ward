# coding: utf-8

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from admin import views as admin_blueprint
from paper import views as paper_blueprint

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:passwd@localhost/ward'

orm = SQLAlchemy(app)

app.register_blueprint(admin_blueprint.admin, url_prefix='/admin')
app.register_blueprint(paper_blueprint.paper, url_prefix='/paper')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=3000)
