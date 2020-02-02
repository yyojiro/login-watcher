# -*- coding: utf-8 -*-
from flask import Blueprint, request, redirect, url_for, render_template, flash
from log_view.util import text2data
from log_view.manager import *

app = Blueprint('views', __name__)


@app.route('/', methods=['GET'])
def show_entries():
    page = int(request.args.get('page', '1'))
    host = request.args.get('host', '')
    user = request.args.get('user', '')
    entries = get_login_list(page=page, host=host, user=user)
    filter = {'page': page, 'host': host, 'user': user}
    return render_template('show_entries.html', entries=entries, filter=filter)


# @app.route('/add', methods=['POST'])
# def add_entry():
#     raw_text = request.form['text']
#     data = text2data(raw_text)
#     if data is None:
#         flash('not matched.')
#         return redirect(url_for('views.show_entries'))
#     add_login_info(data, raw_text)
#     flash('New entry was successfully posted')
#     return redirect(url_for('views.show_entries'))
