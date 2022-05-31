from flask import Flask, redirect, render_template, request,session
from flask_debugtoolbar import DebugToolbarExtension
from stories import story_list

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'
debug = DebugToolbarExtension(app)


picked_idx=None

@app.route('/')
def home():
    return render_template("story_choice.html", story_list=story_list)


@app.route('/story')
def show_query():
    idx= request.args.get("story_id",None)
    if not int(idx) or not idx or int(idx)>len(story_list):
        return redirect ("/")
    picked_idx=int(idx)-1
    session["story_idx"] = picked_idx
    prompts = story_list[picked_idx]["story"].prompts
    return render_template("queries.html", prompts=prompts)


@app.route('/result')
def show_story():
    if not session["story_idx"]:
        return redirect ("/")
    picked_idx=session["story_idx"]
    text = story_list[picked_idx]["story"].generate(request.args)
    return render_template("story.html", text=text)
