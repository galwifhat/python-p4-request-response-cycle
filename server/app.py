#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response, redirect, abort
import os

app = Flask(__name__)

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

'''Request Hooks
@app.before_request: runs a function before each request.
@app.before_first_request: runs a function before the first request (but not subsequent requests).
@app.after_request: runs a function after each request.
@app.teardown_request: runs a function after each request, even if an error has occurred.

'''
    
@app.route("/")
def index():
    host = request.headers.get("Host")
    appname = current_app.name
    response_body = f"""
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    """

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)


# @app.route("/reginald-kenneth-dwight")
# def names():
#     return redirect("names.com/elton-john")


# @app.route("/<stage_name>")
# def get_name(stage_name):
#     match = session.query("StageName").filter(StageName.name == stage_name)[0]
#     if not match:
#         abort(404)
#     return make_response(f"<h1>{stage_name} is an existing stage name!</h1>")


"""
GET / HTTP/1.1
Host: localhost:5000
User-Agent: Mozilla/5.0
Accept: text/html
"""


if __name__ == "__main__":
    app.run(port=5555, debug=True)
