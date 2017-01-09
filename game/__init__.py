from flask import Flask, render_template


class Config():
    COMPOSER_NAMES = ['bach', 'bartok', 'beethoven', 'brahms', 'liszt', 'puccini', 'rachmaninov', 'tchaikovsky']


app = Flask(__name__)


app.config.from_object(Config)


@app.route('/')
def index():
    context = {
        'names': app.config['COMPOSER_NAMES']
    }
    return render_template('index.html', **context)


