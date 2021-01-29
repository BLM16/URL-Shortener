from flask import Blueprint, render_template, redirect, url_for, request
from sqlalchemy.sql import text
from sqlalchemy.exc import SQLAlchemyError
import re

from config import engine, db
from models.url import URL

routes = Blueprint("routes", __name__, static_folder = 'static', template_folder = 'templates')

@routes.errorhandler(404)
def PageNotFound(e):
    return redirect(url_for('routes.Error', title = "Error: 404 - page not found", msg = e))

@routes.route('/')
def Index():
    return render_template("index.html")

@routes.route('/', methods = ['POST'])
def SetURL():
    # Get the url
    url = request.form['url']

    if not url:
        return

    # Define valid url regex
    url_regex = re.compile(
        r'^(?:http)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Validate the url
    if not url_regex.match(url):
        return render_template("index.html", error = True, urlVal = url)
    
    # Connect to the DB
    with engine.connect() as con:
        # See if there is already a key for the url
        try:
            sql = text("SELECT * FROM url WHERE url = :url")
            res = con.execute(sql, url = url).fetchall()
        except SQLAlchemyError as e:
            return redirect(url_for('routes.Error', title = 'Error: Unhandled error', msg = type(e)))
        except:
            return redirect(url_for('routes.Error', title = 'Error: Unhandled error'))

        # If there is a key display that link
        if len(res) > 0:
            return render_template("index.html", short = f'{request.url_root}{res[0].key}')

        # Generate a new key
        key = URL.GenerateKey()

        try:
            # Insert the KVP into the database
            kvp = URL(key, url)
            db.session.add(kvp)
            db.session.commit()
        except:
            return redirect(url_for('routes.Error', title = 'Error: Unhandled error'))

        # Display the new link from the key
        return render_template("index.html", short = f'{request.url_root}{key}')

@routes.route('/<key>')
def KeyRedir(key):
    # Connect to the DB
    with engine.connect() as con:
        # Get the url associated with the key
        sql = text("SELECT url FROM url WHERE key = :key")
        url = con.execute(sql, key = key).scalar()

    # Redirect to the url for the key
    if url:
        return redirect(url)
    else:
        return redirect(url_for('routes.Error', title = "Error: 404 - page not found", msg = f"The key <{key}> does not exist."))

@routes.route('/error')
def Error():
    # Get the error parameters
    title = request.args.get('title')
    msg = request.args.get('msg')
    back = request.args.get('back')

    return render_template("error.html", title = title, msg = msg, back = back)
