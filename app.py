from flask import Flask, render_template, request
from service import create_summarization

app = Flask(__name__)


@app.route('/', methods=["GET"])
def menu():
    return render_template('menu.html')


@app.route('/summary', methods=["POST"])
def summary():
    article_url = request.form['article-url']
    article_summary, heading = create_summarization(article_url)
    if article_summary:
        return render_template('summary.html', summary=article_summary, heading=heading)
    else:
        return "Unsuccessful"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
