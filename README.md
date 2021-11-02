# jcs-comp-club-site
The github repository for the John Cooper school computer club website<br>
<code>jcscomp.xyz</code>

### dependencies
* install python-flask via <code>pip install flask</code>
* to run locally, use <code>python index.py</code>

## How to contribute your work to the website (jcscomp.xyz/tutorial_video)
1. Place your css under the static folder within a folder with your name on it
   with in a css folder
2. Place your javascript in the same folder with your name on it
3. Place your html into a folder with your name under the templates folder

After submitting your code you will have to do one more thing. You will have to
add a function in the main index.py file and templates/index.html file.

<!--
index.html link<br>
<a href="/projectName"><h2>Name</h2></a><br>
-->

index.py link<br>
@app.route('/projectName')<br>
def projectName():<br>
    return render_template('FolderName/index.html')<br>

### directory structure example
static<br>
->Joe_Student<br>
--->css<br>
----->main.css<br>
--->main.js<br>
templates<br>
->Joe_Student<br>
--->index.html<br>
