from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

# routes module
# route handles different URLs that the application supports

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Phil'}
    posts = [ # a list containing dictionaries
        {
            'author': {'username': 'sauceleak'},
            'body': 'The weather feels perfect today, darling.'
        },
        {
            'author': {'username': 'Sad-Cornball'},
            'body': 'The coffee shop was so cute! The girls would love this place.'
        },
        {
            'author':  {'username': 'DarkCrepes'},
            'body': 'Feeling nefarious tbh... xoxo'
        },
        {
            'author': {'username': 'Pieprincess'},
            'body': 'need cream'
        },
        {
            'author': {'username': 'lostSanity'},
            'body': 'can someone help me understand cryptocurrency???'
        },
        {
            'author': {'username': 'L0$TT&C0NfuZD'},
            'body': 'should i double text her lmk!!!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data,  form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)