from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
debug = DebugToolbarExtension(app)


@app.route('/')
def show_query():
    prompts = story.prompts
    return render_template("queries.html", prompts=prompts)


@app.rout('/story')
def show_story():
    text = story.generate(request.args)
    return render_template("story.html", text=text)
