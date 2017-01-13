from flask import Flask, render_template, request, redirect, url_for, \
    make_response
from os import urandom
import binascii


app = Flask(__name__)
app.config.from_object('config')


from models import db, Articles


@app.route('/')
def form():
    return render_template('form.html')


@app.route('/<int:article_id>')
def show_article(article_id):
    article = Articles.query.get_or_404(article_id)
    article_data = {'header': article.header,
                    'signature': article.signature,
                    'body': article.body,
                    'article_id': article_id,
                    'edit': request.cookies.get('user_id') == article.user_id,
                    }
    return render_template('article.html', **article_data)


@app.route('/save/', methods=['POST'])
@app.route('/save/<int:article_id>', methods=['POST'])
def save_article(article_id=None):
    user_id = request.cookies.get('user_id')
    if not user_id:
        user_id = str(binascii.hexlify(urandom(24)))
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
    resp = make_response(redirect(url_for('.show_article',
                                          article_id=article.id)))
    resp.set_cookie('user_id', user_id, max_age=604800)
    return resp


@app.route('/edit/<int:article_id>')
def edit_article(article_id):
    article = Articles.query.get_or_404(article_id)
    if request.cookies.get('user_id') != article.user_id:
        return redirect(url_for('.form'))
    article_data = {'header': article.header,
                    'signature': article.signature,
                    'body': article.body,
                    'article_id': article_id,
                    }
    return render_template('form.html', **article_data)


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', debug=True)
