from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/JoeStudent')
def JoeStudent():
    return render_template('JoeStudent/index.html')

@app.route('/tutorial_video')
def tutorialVideo():
    return render_template('tutorial_video.html')

@app.route('/Francis')
def Francis():
    return render_template('Francis/index.html')

if __name__ == '__main__':
    app.run(debug=True)
