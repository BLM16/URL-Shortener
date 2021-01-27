from config import app
from routes import routes

# Register the app's routes
app.register_blueprint(routes, url_prefix = "")

if __name__ == "__main__":
    app.run(debug = True)