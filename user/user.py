from flask import Blueprint, render_template, url_for, request, redirect
import user.services as utilities

user_blueprint = Blueprint('user_bp', __name__)

@user_blueprint.route('/users', methods=['GET'])
def get_all_users():
    all_users = utilities.get_all_users()
    return render_template('crud_users.html', all_users=all_users)

@user_blueprint.route('/users/insert', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['username']
        email = request.form['email']
        age = request.form['age']
        password = request.form['password']

        utilities.add_user(name, email, age, password)
    all_users = utilities.get_all_users()
    return redirect(url_for('user_bp.get_all_users',all_users=all_users))

@user_blueprint.route('/users/delete', methods=['GET', 'POST'])
def delete_user(user_id):
    user = utilities.get_user(user_id)
    utilities.delete_user(user)
    all_users = utilities.get_all_users()
    return redirect(url_for('user_bp.get_all_users', all_users=all_users))