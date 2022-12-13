from flask import Blueprint, render_template, url_for, request, redirect
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

        utilities.add_task(name, description)
    all_tasks = utilities.get_all_tasks()
    return redirect(url_for('task_bp.get_all_tasks',all_tasks=all_tasks))