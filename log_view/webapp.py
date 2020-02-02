#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from log_view import app, controller, api

app.register_blueprint(controller.app, url_prefix="/list")
app.register_blueprint(api.app, url_prefix="/api")

@app.route("/")
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
