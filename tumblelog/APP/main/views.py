from flask import Flask, render_template, session, redirect, url_for, flash
from ..models import *
from . import main
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import random


class NameForm(Form):
    name = StringField('what is your name?')
    submit = SubmitField('Submit')


@main.route('/')
def index():
    form = NameForm()
    quo = Quotion_doc.objects(index=random.randint(0, 1004))[0]
    # posts = Tieba_post_doc.objects()
    posts = Post_doc.objects()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name != None and old_name != form.name.data:
            flash('you have changed your name - -')
        session['name'] = form.name.data
        # form.name.data = ''
        return redirect(url_for('index'))
    return render_template("index.html", current_time=datetime.utcnow(),
                           form=form, posts=posts, quo=quo, name=session.get('name'))


@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@main.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
