from flask import Blueprint, render_template, request, redirect, url_for
from models import db, User

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@bp.route('/add', methods=['POST'])
def add_user():
    name = request.form.get('name')
    email = request.form.get('email')
    new_user = User(name=name, email=email)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/update/<int:id>', methods=['POST'])
def update_user(id):
    user = User.query.get(id)
    user.name = request.form.get('name')
    user.email = request.form.get('email')
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('main.index'))
