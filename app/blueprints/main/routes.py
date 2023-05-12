from flask import render_template, g

from . import bp 

from app import app
from app.forms import UserSearchForm


@app.before_request
def before_request():
    g.user_search_form = UserSearchForm()



@bp.route('/')
def home():
    matrix={
        'cars': ['Ford Mustang', 'Chevrolet Corvette', 'Audi R8', 'Porsche-911'],
        'drivers':['Jeff Gordon', 'Alain Prost', 'Jimmie Johnson', 'Richard Petty', 'Nigel Mansell', 'Michael Schumacher']
    }
    return render_template('index.jinja', title='Home', cars=matrix['cars'], drivers=matrix['drivers'],user_search_form=g.user_search_form)


@bp.route('/about')
def about():
    return render_template('about.jinja', user_search_form=g.user_search_form)
