from .logging.logging import setup_logger

from datetime import datetime
from os import getenv

import pytz
from loguru import logger
from flask import Flask, render_template

TIME_ZONE = 'Europe/Moscow'
DEBUG = getenv('DEBUG')

setup_logger()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main_page():
    now = datetime.now(tz=pytz.timezone(TIME_ZONE)).strftime('%H:%M:%S')
    logger.info('Request with %s', now)
    return render_template('index.html', time=now)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)
