from flask import Blueprint, render_template, url_for, request, redirect, flash
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

        flash('User has been inserted successfully !')
    #return render_template('crud_users.html', all_users=all_users)
    return redirect(url_for('user_bp.get_all_users'))

@user_blueprint.route('/users/delete/<user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    print(user_id)
    user = utilities.get_user(user_id)
    utilities.delete_user(user)
    flash('User has been deleted successfully !')
    #return render_template('crud_users.html', all_users=all_users) // alternative solution by using slash/ path in the url
    return redirect(url_for('user_bp.get_all_users'))

@user_blueprint.route('/update/<user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    print(user_id)
    if request.method == 'POST':
        user_number = request.form.get('user_id')
        user_name = request.form.get('user_name')
        user = utilities.get_user(user_number)
        user.name = request.form['update_username']
        user.email = request.form['update_email']

        user.age = ''
        if request.form['update_age'].isdigit():
            user.age = int(request.form['update_age'])

        print(user.password)
        user.password = request.form['update_password']
        flash('User has been updated successfully !')
        print(331)
        print(user.password)


    return redirect(url_for('user_bp.get_all_users'))