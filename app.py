from flask import (
    url_for,
    request,
    redirect,
    render_template,
    flash,
)

from models import db, Project, app
from datetime import datetime
from forms import AddProjectForm


app.secret_key = '@!#@!effR@$#%tY^%&5785675654ygG$#Q:GP6*P&'


@app.route('/')
def index():
    projects = Project.query.all()
    return render_template('index.html', projects=projects)


@app.route('/detail')
def detail():
    projects = Project.query.all()
    return render_template('detail.html', projects=projects)


@app.route('/about', methods=['GET'])
def about():
    projects = Project.query.all()
    return render_template('about.html', projects=projects)


@app.route('/add', methods=['GET', 'POST'])
def add_project():
    form = AddProjectForm()

    if request.method == 'POST' and form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        skills = form.skills.data
        url = form.url.data
        url_tag = form.url_tag.data
        completion_date = form.completion_date.data

        new_project = Project(
            title=title,
            description=description,
            skills=skills,
            url=url,
            url_tag=url_tag,
            completion_date=completion_date
        )

        try:
            db.session.add(new_project)
            db.session.commit()
            flash("Project added successfully", 'success')
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error adding project to the database: {e}")
            flash("Error adding project to the database", 'danger')

    return render_template('add.html', form=form, index_url=url_for('index'))


@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)

    if project is None:
        return redirect(url_for('index'))

    if request.method == 'POST':

        project.title = request.form['title']
        project.completion_date = datetime.strptime(request.form['date'], '%Y-%m')
        project.description = request.form['description']
        project.skills = request.form['skills']
        project.url = request.form['url']
        project.url_tag = request.form['url_tag']
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit.html', project=project)


@app.route('/project/<id>')
def project(id):
    single_project = Project.query.get_or_404(id)
    return render_template('projectform.html', project=single_project)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_project(id):
    project = Project.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(project)
        db.session.commit()
        flash("Project deleted successfully", 'success')
        return redirect(url_for('index'))

    return render_template('delete_confirmation.html', project=project)


@app.errorhandler(404)
def not_found(error):
    custom_message = "Sorry, i am not working fast enough, this page was not yet coded"
    return render_template('404.html', msg=custom_message), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080, host='127.0.0.1')
