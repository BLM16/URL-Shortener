from flask import redirect, url_for

from config import app
from routes import routes

# Register the app's routes
app.register_blueprint(routes, url_prefix = "")

@app.errorhandler(404)
def PageNotFound(e):
    return redirect(url_for('routes.Error', title = "Error: 404 - page not found", msg = e))

if __name__ == "__main__":
    app.run(debug = True)
