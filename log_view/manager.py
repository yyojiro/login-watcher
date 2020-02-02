# -*- coding: utf-8 -*-

from log_view import db
from log_view.models import LoginInfo


def add_login_info(info, raw_text=None):
    entry = LoginInfo(
        remote_addr=info['remote_addr'],
        timestamp=info['timestamp'],
        host=info['host'],
        user=info['user'],
        event_type=info['event_type'],
        raw_text=raw_text
    )
    db.session.add(entry)
    db.session.commit()


def get_login_list(page=1, host=None, user=None):
    # TODO: config化
    perpage = 10
    entries = LoginInfo.query.\
        filter(LoginInfo.host.like('%' + host + '%')). \
        filter(LoginInfo.user.like('%' + user + '%')). \
        order_by(LoginInfo.timestamp.desc()).\
        paginate(page, perpage)
    return entries


def get_login_info(id):
    return LoginInfo.query.get(id)

