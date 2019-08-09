# coding: utf-8

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from admin import views as admin_blueprint
from literature import views as literature_blueprint
from author import views as author_blueprint
from category import views as category_blueprint
from organization import views as organization_blueprint

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:passwd@localhost/ward'

orm = SQLAlchemy(app)

app.register_blueprint(admin_blueprint.admin, url_prefix='/admin')
app.register_blueprint(literature_blueprint.literature, url_prefix='/literature')
app.register_blueprint(author_blueprint.author, url_prefix='/author')
app.register_blueprint(category_blueprint.category, url_prefix='/category')
app.register_blueprint(organization_blueprint.organization, url_prefix='/organization')


@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(port=3000)
