from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

from config import engine

routes = Blueprint("routes", __name__, static_folder = 'static', template_folder = 'templates')

@routes.route('/')
def Index():
    return render_template("index.html")
