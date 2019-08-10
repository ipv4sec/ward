# coding: utf-8

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# api
from admin import apis as admin_blueprint
from literature import apis as literature_blueprint
from author import apis as author_blueprint
from category import apis as category_blueprint
from organization import apis as organization_blueprint

# ui
from dashboard import views as dashboard_blueprint

app = Flask(__name__)

# orm
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:passwd@localhost/ward'
orm = SQLAlchemy(app)

# api register
app.register_blueprint(admin_blueprint.admin, url_prefix='/admin')
app.register_blueprint(literature_blueprint.literature, url_prefix='/literature')
app.register_blueprint(author_blueprint.author, url_prefix='/author')
app.register_blueprint(category_blueprint.category, url_prefix='/category')
app.register_blueprint(organization_blueprint.organization, url_prefix='/organization')

# ui register
app.register_blueprint(dashboard_blueprint.dashboard, url_prefix='/')


@app.route("/")
def index():
    return render_template('index.html')





if __name__ == "__main__":
    app.run(port=3000)
