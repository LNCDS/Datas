
from flask import Flask, render_template, request

from app.tasks.controllers import taskRoute
from app.config import DevConfig

app = Flask(__name__)

app.register_blueprint(taskRoute)

app.config.from_object(DevConfig)


@app.route("/")
def index():
    name = request.args.get('name')
    return render_template('index.html', name=name)
