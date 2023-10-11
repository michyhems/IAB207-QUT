from flask import Blueprint, request, render_template, session,  redirect, url_for
from .models import Destination
from . import db

#Use of blue print to group routes, 
# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
mainbp = Blueprint('main', __name__)


@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination))
    return render_template('index.html', destinations = destinations)




@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        destinations = db.session.scalars(db.select(Destination).where(Destination.name.like(query)))
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))