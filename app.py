from flask import (url_for, request, 
                   redirect, render_template)
from models import db, Project, app


@app.route('/')
def index():
    project= Project.query.all()
    return render_template('index.html', project=project)


@app.route('/detail')
def detail():
    project= Project.query.all()
    return render_template('detail.html', project=project)


@app.route('/about', methods=['GET'])
def about():
    project= Project.query.all()
    return render_template('about.html', project=project)


@app.route('/add', methods=['GET', 'POST'])
def add_project():
    if request.form:
        new_project = Project(title=request.form['title'], 
                      description=request.form['description'], skill=request.form['skill'],
                      url=request.form['url'], url_tag=request.form['alt']
                      ,)
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    project = Project.query.get_or_404(id)

    if project is None:

      
        return redirect(url_for('index'))

    if request.method == 'POST':
       
        project.title = request.form['title']
        project.created = request.form['created']
        project.description = request.form['description']
        project.skill = request.form['skill']
        project.url = request.form['url']
        project.url_tag = request.form['alt']

        db.session.commit()
        return redirect(url_for('index'))

    
    return render_template('edit.html', project=project)




@app.route('/project/<id>')
def project(id):
    project = Project.query.get_or_404(id)
    return render_template('projectform.html', project=project)


@app.route('/delete/<id>')
def delete_project(id):
    project=Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', msg=error), 404



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8080, host='127.0.0.1')