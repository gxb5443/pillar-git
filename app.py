import os
import request
from flask import Flask, redirect, url_for, flash, session, g, jsonify
from flask_github import GitHub

app = Flask(__name__, static_url_path='')
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['GITHUB_CLIENT_ID'] = 'Iv1.cd673e23f77ee90d'
app.config['GITHUB_CLIENT_SECRET'] = 'ef74916831c17308d2a9e54fe239ace484caac72'

github = GitHub(app)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# @app.before_request
# def before_request():
#    g.user = None
#

@github.access_token_getter
def token_getter():
    user = g.user
    if user is not None:
        return user


@app.route('/login')
def login():
    return github.authorize()


@app.route('/hello')
def hello_world():
    return 'Hello, World!'


@app.route('/index')
def index():
    return redirect("http://lvh.me/", code=302)


@app.route('/stats/<owner>/<repo>')
def github_stats(owner, repo):
    g.user = session['token']
    return jsonify(github.get('/repos/' + owner + '/' + repo))


@app.route('/github-callback')
@github.authorized_handler
def authorized(oauth_token):
    if oauth_token is None:
        flash("Authorization failed.")
        return redirect("http://lvh.me/", code=302)
    session['token'] = oauth_token
    #g.user = oauth_token
    return redirect("http://lvh.me/", code=302)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0')
