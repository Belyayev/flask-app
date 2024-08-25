from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def home():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['POST'])
def add_user():
    email = request.form['email']
    name = request.form['name']
    new_user = User(email=email, name=name)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete_user/<int:id>')
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update_user/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.email = request.form['email']
        user.name = request.form['name']
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('update_user.html', user=user)
