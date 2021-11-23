from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/member_projects')
def member_projects():
    return render_template('member_projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contribute')
def contribute():
    return render_template('contribute.html')

@app.route('/JoeStudent')
def JoeStudent():
    return render_template('JoeStudent/index.html')

@app.route('/Francis')
def Francis():
    return render_template('Francis/index.html')

if __name__ == '__main__':
    app.run(debug=True)
