from datetime import datetime

from flask import Flask, render_template
import pytz

app = Flask(__name__)
TIME_ZONE = 'Europe/Moscow'

@app.route('/', methods=['GET'])
def main_page():
    now = datetime.now(tz=pytz.timezone(TIME_ZONE))
    return render_template('index.html',time=now.strftime('%H:%M:%S'))
