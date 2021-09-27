from .logging.logging import setup_logger

from datetime import datetime
from os import getenv
from pathlib import Path

import pytz
from loguru import logger
from flask import Flask, render_template, make_response

TIME_ZONE = 'Europe/Moscow'
DEBUG = getenv('DEBUG')
VISITS_FILE = Path('data/visits.json')

setup_logger()

app = Flask(__name__)

def dump_time(time):
    with open(VISITS_FILE, 'a') as f:
        f.write(f'Reqested at: {time}\n')


@app.route('/', methods=['GET'])
def main_page():
    now = datetime.now(tz=pytz.timezone(TIME_ZONE)).strftime('%H:%M:%S')
    logger.info('Request with %s', now)
    dump_time(now)
    return render_template('index.html', time=now)

@app.route('/visits', methods=['GET'])
def visits_page():
    if not (VISITS_FILE.exists() and VISITS_FILE.is_file()):
        return make_response({"msg": "Nott found"}, 404)
    with open(VISITS_FILE, 'r') as f:
        content = f.read()
        return {"file-content": content}, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=DEBUG)

