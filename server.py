from flask import Flask, render_template, request, json, make_response
from os import urandom
import binascii
from config import site_title

app = Flask(__name__)
app.config.from_object('config')

from models import db, Articles

db.create_all()


def get_article_data(article):
    return {'title': site_title,
            'article_id': article.id,
            'header': article.header,
            'signature': article.signature,
            'body': article.body,
            'author': request.cookies.get('user_id') == article.user_id,
            }


@app.route('/')
def form():
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = str(binascii.hexlify(urandom(24)))
    resp = make_response(render_template('telegraph.html', title=site_title))
    resp.set_cookie('user_id', user_id, max_age=604800)
    return resp


@app.route('/<int:article_id>')
def show_article(article_id):
    article = Articles.query.get_or_404(article_id)
    article_data = get_article_data(article)
    return render_template('telegraph.html', **article_data)


@app.route('/save/', methods=['POST'])
@app.route('/save/<int:article_id>', methods=['POST'])
def save_article(article_id=None):
    user_id = request.cookies.get('user_id')
    if article_id:
        article = Articles.query.get_or_404(article_id)
        article.header = request.form['header']
        article.signature = request.form['signature']
        article.body = request.form['body']
    else:
        article = Articles(request.form['header'],
                           request.form['signature'],
                           request.form['body'],
                           user_id
                           )
    db.session.add(article)
    db.session.commit()
    article_data = get_article_data(article)
    return json.dumps(article_data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False)
