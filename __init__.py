from flask import Flask, render_template
from adapters.memory_repository import MemoryRepository
import adapters.repository as repo

app = Flask(__name__)
repo.repo_instance = MemoryRepository()


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/base')
def base():
    return render_template('base.html')

with app.app_context():
    from user import user
    from task import task
    app.register_blueprint(user.user_blueprint)
    app.register_blueprint(task.task_blueprint)


if __name__ == "__main__":
    app.run(debug=True)