from flask import Flask
from routes import webhook

# Creating our flask app
app = Flask(__name__)
# registering all the blueprints
app.register_blueprint(webhook)

if __name__ == '__main__':
    app.run(debug=True)
