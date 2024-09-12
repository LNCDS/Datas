
from flask import Flask

from app.tasks.controllers import taskRoute
from app.config import DevConfig

app = Flask(__name__)
app.register_blueprint(taskRoute)
app.config.from_object(DevConfig)
app.config.from_object(object)
#@app.route("/")
#def index():
#    return "es"
