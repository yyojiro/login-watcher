# -*- coding: utf-8 -*-

from flask import Blueprint, request, jsonify, make_response
from log_view.manager import *
from log_view.util import text2data

app = Blueprint('api', __name__)


@app.route("/info/", methods=['POST'])
def add_info():
    req_obj = request.json
    raw_text = u'%s' % req_obj['text']
    print(raw_text)
    data = text2data(raw_text)
    if data is None:
        import datetime
        data ={"timestamp": datetime.datetime.now(),
               "remote_addr": request.remote_addr}
        add_login_info(data, raw_text)
        return make_response(jsonify({'result': 'BAD DATA'}))
    else:
        data["remote_addr"] = request.remote_addr
        add_login_info(data, raw_text)
        return make_response(jsonify({'result': 'OK'}))
