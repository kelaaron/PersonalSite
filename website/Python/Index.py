"""
Website index (main) view.

URLs include:
/
"""
import flask
import website

@website.app.route('/', methods=["GET", "POST"])
def showIndex():

    
    context = {}
    return flask.render_template("index.html", **context)
