from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError

from config import engine

routes = Blueprint("routes", __name__, static_folder = 'static', template_folder = 'templates')

@routes.errorhandler(404)
def PageNotFound(e):
    return redirect(url_for('routes.Error', title = "Error: 404 - page not found", msg = e))

@routes.route('/')
def Index():
    return render_template("index.html")

@routes.route('/<key>')
def KeyRedir(key):
    # Connect to the DB
    with engine.connect() as con:
        # Get the url associated with the key
        sql = text("SELECT url FROM url WHERE key = :key")
        url = con.execute(sql, key = key).scalar()

    # Redirect to the url for the key
    return redirect(url)

@routes.route('/error')
def Error():
    # Get the error parameters
    title = request.args.get('title')
    msg = request.args.get('msg')
    back = request.args.get('back')

    return render_template("error.html", title = title, msg = msg, back = back)
