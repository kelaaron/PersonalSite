"""
Website about (main) view.

URLs include:
/
"""
import flask
import website

@website.app.route('/about/', methods=["GET", "POST"])
def showAbout():

    
    context = {}
    return flask.render_template("about.html", **context)