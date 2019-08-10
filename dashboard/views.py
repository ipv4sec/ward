# coding: utf-8

from flask import Blueprint, render_template, redirect, url_for

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def index_ui():
    return render_template('index.html')


@dashboard.route("/dashboard/")
def dashboard_ui():
    return render_template('dashboard.html')


@dashboard.route("/dashboard/admin/")
def admin_ui():
    return render_template('admin.html')


@dashboard.route("/dashboard/admin/quit")
def admin_quit():
    return redirect(url_for('index'))


@dashboard.route("/dashboard/author/")
def author_ui():
    return render_template('author.html')


@dashboard.route("/dashboard/category/")
def category_ui():
    return render_template('category.html')


@dashboard.route("/dashboard/literature/")
def literature_ui():
    return render_template('literature.html')


@dashboard.route("/dashboard/organization/")
def organization_ui():
    return render_template('organization.html')