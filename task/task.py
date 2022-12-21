from flask import Blueprint, render_template, url_for, request, redirect, flash
import task.services as utilities

task_blueprint = Blueprint('task_bp', __name__)

@task_blueprint.route('/tasks', methods=['GET'])
def get_all_tasks():
    all_tasks = utilities.get_all_tasks()
    return render_template('crud_tasks.html', all_tasks=all_tasks)

@task_blueprint.route('/tasks/insert', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        time = request.form['time']
        print(name)
        print(time)
        utilities.add_task(name, description, time)
        flash('Task has been inserted successfully !')
    all_tasks = utilities.get_all_tasks()
    print(len(all_tasks))
    for task in all_tasks:
        print(task)
        print(task.time)
    return redirect(url_for('task_bp.get_all_tasks',all_tasks=all_tasks))

@task_blueprint.route('/tasks/delete/<task_id>', methods=['GET', 'POST'])
def delete_task(task_id):
    task = utilities.get_task(task_id)
    utilities.delete_task(task)
    flash('Task has been deleted successfully !')
    #return render_template('crud_users.html', all_users=all_users) // alternative solution by using slash/ path in the url
    return redirect(url_for('task_bp.get_all_tasks'))


@task_blueprint.route('/update', methods=['GET', 'POST'])
def update_task():
    if request.method == 'POST':
        task_number = request.form.get('task_id')
        task = utilities.get_task(task_number)
        task.name = request.form['update_taskname']
        task.description = request.form['update_description']
        task.status = request.form['update_status']
        flash('User has been updated successfully !')


    return redirect(url_for('task_bp.get_all_tasks'))