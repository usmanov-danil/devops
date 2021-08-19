from datetime import datetime
from os import getenv

import pytz
from flask import Flask, render_template

TIME_ZONE = 'Europe/Moscow'
DEBUG = getenv('DEBUG')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    now = datetime.now(tz=pytz.timezone(TIME_ZONE))
    return render_template('index.html', time=now.strftime('%H:%M:%S'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)
