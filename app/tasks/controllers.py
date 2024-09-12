from flask import Blueprint

taskRoute = Blueprint('task',__name__,url_prefix='/tasks')


@taskRoute.route('/')
def index() -> str:
    return 'index'

@taskRoute.route('/show/<int:id>')
def show(id:int):
    return f'show {id}'

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return f'delete {id}'

@taskRoute.route('/create', methods = ['GET','POST'])
def create():
    return 'create'

@taskRoute.route('/update/<int:id>', methods = ['GET','POST'])
def update(id:int):
    return f'update xs {id}'