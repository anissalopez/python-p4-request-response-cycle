#!/usr/bin/env python3
import os
from flask import Flask, request, current_app, g

app = Flask(__name__)

# Query Parameters
# @app.route('/query_example')
# def query_example():
#     language = request.args.get('language')
#     framework = request.args.get('framework')
#     website = request.args.get('website')
#     return """<h1> the language is {}</h1>
#     <h1>The Framework is {}</h1>
#    <h1> The website is {}</h1>""".format(language, framework, website)

# Form Example

# @app.route('/form_example', methods=['POST', 'GET'])
# def form_example():
#     if request.method == 'POST':
#         language = request.form.get('language')
#         framework = request.form.get('framework')
#         return f"""<h1> Submitted Form 
#         Language is {language}, Framework = {framework}</h1> """
#     elif request.method == 'GET':
#         return """
#             <form method="POST">
#             Language <input type="text" name="language">
#             Framework <input type="text" name="framework">
#             <input type="submit">
#             """
    

@app.before_request
def app_path():
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''

    status_code = 200
    headers = {}

    return make_response(response_body, status_code, headers)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
